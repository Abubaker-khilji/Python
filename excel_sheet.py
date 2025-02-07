import pandas as pd
# Read the Excel file into a DataFrame
df = pd.read_excel("INTERNAL COORDINATION DEPT.xlsx")

# Filter rows containing 'ABU BAKAR' in any column
filtered_rows = df[df.apply(lambda row: row.astype(str).str.contains('ABU BAKAR').any(), axis=1)]

# Display the filtered rows
print(filtered_rows)


# Save the filtered rows to a new Excel file
filtered_rows.to_excel('abubaker_jobs.xlsx', index=False)  # Adjust the output file name if necessary

print("Filtered rows have been saved to 'abubaker_jobs.xlsx'")
