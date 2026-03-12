import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. LOAD DATA ──────────────────────────
df = pd.read_csv('C:\\Users\\PC\\Desktop\\Student-Performance Analysis\\data\\StudentsPerformance.csv')


# ── 2. BASIC OVERVIEW ─────────────────────
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nBasic Statistics:")
print(df.describe())



# ── 3. AVERAGE SCORES BY GENDER ───────────
print("\nAverage Scores by Gender:")
print(df.groupby('gender')[['math score','reading score','writing score']].mean().round(2))

# ── 4. AVERAGE SCORES BY PARENTAL EDUCATION
print("\nAverage Scores by Parental Education:")
print(df.groupby('parental level of education')[['math score','reading score','writing score']].mean().round(2))

# ── 5. IMPACT OF TEST PREP COURSE ─────────
print("\nImpact of Test Preparation Course:")
print(df.groupby('test preparation course')[['math score','reading score','writing score']].mean().round(2))

# ── 6. ADD TOTAL & AVERAGE SCORE COLUMNS ──
df['total score'] = df['math score'] + df['reading score'] + df['writing score']
df['average score'] = (df['total score'] / 3).round(2)

# ── 7. VISUALISATION 1 — Score Distribution
plt.figure(figsize=(10,5))
sns.histplot(df['average score'], bins=20, kde=True, color='steelblue')
plt.title('Distribution of Average Student Scores')
plt.xlabel('Average Score')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('C:\\Users\\PC\\Desktop\\Student-Performance Analysis\\visuals\\score_distribution.png')
plt.show()
print("Chart 1 saved!")

# ── 8. VISUALISATION 2 — Scores by Gender ─
plt.figure(figsize=(10,5))
df.groupby('gender')[['math score','reading score','writing score']].mean().plot(kind='bar', colormap='Set2')
plt.title('Average Scores by Gender')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('C:\\Users\\PC\\Desktop\\Student-Performance Analysis\\visuals\\scores_by_gender.png')
plt.show()
print("Chart 2 saved!")

# ── 9. VISUALISATION 3 — Test Prep Impact ─
plt.figure(figsize=(10,5))
df.groupby('test preparation course')[['math score','reading score','writing score']].mean().plot(kind='bar', colormap='Set1')
plt.title('Impact of Test Preparation Course on Scores')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('C:\\Users\\PC\\Desktop\\Student-Performance Analysis\\visuals\\test_prep_impact.png')
plt.show()
print("Chart 3 saved!")

# ── 10. VISUALISATION 4 — Parental Education
plt.figure(figsize=(12,6))
df.groupby('parental level of education')['average score'].mean().sort_values().plot(kind='barh', color='coral')
plt.title('Average Student Score by Parental Education Level')
plt.xlabel('Average Score')
plt.tight_layout()
plt.savefig('C:\\Users\\PC\\Desktop\\Student-Performance Analysis\\visuals\\parental_education_impact.png')
plt.show()
print("Chart 4 saved!")

print("\n✅ Analysis Complete! All charts saved to visuals folder.")