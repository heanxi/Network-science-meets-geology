import pandas as pd

# Read the Excel file without specifying column names
file_path = 'E:/network/du/Modularity/tong2.0/CUTA0.3.5-0.297-5.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Display the first few rows and column names
print("File preview (first few rows):")
print(df.head())
print("Column names:")
print(df.columns)

# Attributes to be analyzed
attributes = ['c_3', 'd_2', 'e_1', 'f_3', 'g_2', 'h_2', 'i_2', 'j_4']

# Column for community classification
modularity_class_column = 'modularity_class'

# Check if the classification column exists
if modularity_class_column not in df.columns:
    print(f"Column {modularity_class_column} not found. Skipping classification.")
else:
    # Group the data by modularity class
    grouped = df.groupby(modularity_class_column)

    # Dictionary to store the final statistics
    stats = {}

    # Iterate through each community
    for modularity_class, group in grouped:
        print(f"Processing class {modularity_class}:")

        # Dictionary to store statistics for the current class
        modularity_stats = {}

        # Loop through each attribute
        for attr in attributes:
            print(f"Processing attribute {attr}:")

            # Check if the attribute exists in the DataFrame
            if attr in df.columns:
                print(f"Found attribute {attr} in columns")

                # Retrieve the column data for this group
                col_data = group[attr]
                print(f"Preview of {attr} column:\n{col_data.head()}\n")

                # Count the frequency of each unique value in the column
                value_counts = col_data.value_counts().sort_values(ascending=False)

                if value_counts.empty:
                    print(f"No data in column {attr}")
                else:
                    print(f"Statistics for {attr} (Top 5):\n{value_counts.head()}\n")

                # Save the statistics
                modularity_stats[attr] = value_counts
            else:
                print(f"Attribute {attr} not found in data. Skipping.\n")

        # Save the class statistics
        stats[modularity_class] = modularity_stats

    # Print all results
    print("All statistical results:")
    for modularity_class, modularity_results in stats.items():
        print(f"Statistics for class {modularity_class}:")
        for attr, result in modularity_results.items():
            print(f"Statistics for {attr}:\n{result}\n")

    # Export results to a new Excel file
    output_path = 'E:/network/du/Modularity/tong2.0/Statistics_Result.xlsx'

    if stats:
        with pd.ExcelWriter(output_path) as writer:
            for modularity_class, modularity_results in stats.items():
                # Combine all attribute statistics into one sheet
                all_results = pd.concat(modularity_results, axis=1)
                all_results.to_excel(writer, sheet_name=f"{modularity_class}_stats", index=True)
    else:
        # If no statistics, write a default sheet
        with pd.ExcelWriter(output_path) as writer:
            pd.DataFrame({"Message": ["No attribute data was found."]}).to_excel(writer, sheet_name="Empty")

    print(f"Statistics have been saved to: {output_path}")
