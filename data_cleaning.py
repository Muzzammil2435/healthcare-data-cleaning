import pandas as pd

# Load dataset
df = pd.read_csv('healthcare_dataset.csv')
print("Original Shape:", df.shape)

# Check data types
print("\nColumn Types:")
print(df.dtypes)

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Fill missing AGE with mean
mean_age = df_cleaned['AGE'].mean()
df_cleaned['AGE'].fillna(mean_age, inplace=True)

# Analysis
print("\nCleaned Shape:", df_cleaned.shape)
print(f"Average Age: {df_cleaned['AGE'].mean():.1f}")
print(f"Most Common Disease: {df_cleaned['DISEASE'].mode()[0]}")
print(f"Total Patients: {len(df_cleaned)}")

# Save cleaned file
df_cleaned.to_csv('cleaned_healthcare_data.csv', index=False)
print("\nCleaned file saved!")
