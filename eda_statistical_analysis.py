

import pandas as pd
import numpy as np
from scipy import stats

# ---------------------------------------------------------------------------
# 1. Load & clean
# ---------------------------------------------------------------------------
df = pd.read_csv("../data/patient_readmission_sample.csv")

df.drop_duplicates(subset="PatientID", inplace=True)
df["LengthOfStay"] = df["LengthOfStay"].clip(lower=1)
df["Readmit_Flag"] = df["Readmitted_30Days"].map({"Yes": 1, "No": 0})

print("Shape:", df.shape)
print("30-Day Readmission Rate: {:.1%}".format(df["Readmit_Flag"].mean()))
print(df.describe(include="number").T)

# ---------------------------------------------------------------------------
# 2. Correlation analysis
# ---------------------------------------------------------------------------
numeric_cols = ["Age", "LengthOfStay", "PriorAdmissions", "MedicationCount", "Readmit_Flag"]
corr_matrix = df[numeric_cols].corr(method="pearson")
print("\nCorrelation with 30-Day Readmission:")
print(corr_matrix["Readmit_Flag"].sort_values(ascending=False))

r_los, p_los = stats.pointbiserialr(df["Readmit_Flag"], df["LengthOfStay"])
print(f"\nLengthOfStay vs Readmission -> r={r_los:.3f}, p={p_los:.4f}")

r_prior, p_prior = stats.pointbiserialr(df["Readmit_Flag"], df["PriorAdmissions"])
print(f"PriorAdmissions vs Readmission -> r={r_prior:.3f}, p={p_prior:.4f}")

# ---------------------------------------------------------------------------
# 3. Hypothesis Testing
# ---------------------------------------------------------------------------

# H1: Patients with a chronic condition are readmitted at a higher rate (Chi-Square Test)
contingency = pd.crosstab(df["ChronicCondition"], df["Readmitted_30Days"])
chi2, p_chi2, dof, expected = stats.chi2_contingency(contingency)
print(f"\n[H1] ChronicCondition vs Readmission — Chi-Square: chi2={chi2:.2f}, p={p_chi2:.4f}")
print("Reject H0 (significant association)" if p_chi2 < 0.05 else "Fail to reject H0")

# H2: Lack of a scheduled follow-up is associated with higher readmission (Chi-Square Test)
contingency2 = pd.crosstab(df["FollowUpScheduled"], df["Readmitted_30Days"])
chi2_f, p_chi2_f, dof_f, expected_f = stats.chi2_contingency(contingency2)
print(f"\n[H2] FollowUpScheduled vs Readmission — Chi-Square: chi2={chi2_f:.2f}, p={p_chi2_f:.4f}")
print("Reject H0 (significant association)" if p_chi2_f < 0.05 else "Fail to reject H0")

# H3: Average length of stay differs between readmitted and non-readmitted patients (Welch t-test)
los_readmit = df.loc[df["Readmitted_30Days"] == "Yes", "LengthOfStay"]
los_stayed = df.loc[df["Readmitted_30Days"] == "No", "LengthOfStay"]
t_stat, p_ttest = stats.ttest_ind(los_readmit, los_stayed, equal_var=False)
print(f"\n[H3] Length of Stay (Readmitted vs Not) — Welch t-test: t={t_stat:.2f}, p={p_ttest:.4f}")
print("Reject H0 (significant difference)" if p_ttest < 0.05 else "Fail to reject H0")

# H4: Prior admissions count differs across departments (One-Way ANOVA)
groups = [g["PriorAdmissions"].values for _, g in df.groupby("Department")]
f_stat, p_anova = stats.f_oneway(*groups)
print(f"\n[H4] Prior Admissions across Departments — ANOVA: F={f_stat:.2f}, p={p_anova:.4f}")
print("Reject H0 (differs by department)" if p_anova < 0.05 else "Fail to reject H0")

# ---------------------------------------------------------------------------
# 4. Department-level readmission risk summary (feeds the Power BI report)
# ---------------------------------------------------------------------------
dept_summary = (
    df.groupby("Department")
      .agg(patient_count=("PatientID", "count"),
           readmission_rate=("Readmit_Flag", "mean"),
           avg_length_of_stay=("LengthOfStay", "mean"),
           avg_prior_admissions=("PriorAdmissions", "mean"))
      .sort_values("readmission_rate", ascending=False)
)
print("\nDepartment Readmission Risk Summary:")
print(dept_summary)

dept_summary.to_csv("department_readmission_summary.csv")
