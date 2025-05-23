import pandas as pd
from itertools import combinations

# File path of the Excel file
file_path = r'E:\data\network\new\tong_with_class_CUTA.xls'

# Read the Excel file
df = pd.read_excel(file_path, engine='xlrd')

# Print column names and preview the first few rows
print("Column names of the DataFrame:", df.columns.tolist())
print("First few rows of the DataFrame:\n", df.head())

# Define the attribute columns and their corresponding hierarchy levels
attributes = {
    'C_1': 0.0104,
    'C_2': 0.0414,
    'C_3': 0.0932,
    'D_1': 0.0170,
    'D_2': 0.0680,
    'E_1': 0.0376,
    'E_2': 0.1504,
    'F_1': 0.0073,
    'F_2': 0.0291,
    'F_3': 0.0656,
    'G_1': 0.101,
    'H_1': 0.0216,
    'H_2': 0.0864,
    'I_1': 0.0382,
    'I_2': 0.1528,
    'Y_1': 0.0027,
    'Y_2': 0.0107,
    'Y_3': 0.0240,
    'Y_4': 0.0426
}

edges = []

# Iterate through each attribute column
for attribute, level in attributes.items():
    if attribute in df.columns:
        print(f"Processing attribute: {attribute}")
        # Group the data by the current attribute
        grouped = df.groupby(attribute)

        # Iterate through each group to construct edges
        for group_name, group in grouped:
            if len(group) > 1:
                # Generate all combinations of nodes with the same attribute value
                for pair in combinations(group.index, 2):
                    start_index, end_index = pair
                    start_node = str(group.loc[start_index, 'ID'])  # Start node name
                    end_node = str(group.loc[end_index, 'ID'])      # End node name

                    # Ensure undirected edge: sort node names alphabetically
                    node_pair = tuple(sorted([start_node, end_node]))

                    # Store the edge information with attribute and hierarchy level
                    edges.append({
                        'Source': node_pair[0],     # Start node
                        'Target': node_pair[1],     # End node
                        'Attribute': attribute,     # Attribute column name
                        'AttributeValue': group_name,  # Value of the attribute
                        'Level': level              # Hierarchy level
                    })

# Convert the edge list to a DataFrame
edges_df = pd.DataFrame(edges)

# Preview the first few rows of the resulting edge DataFrame
print("First few rows of the Edges DataFrame:\n", edges_df.head())

# Save the edge data to a CSV file
output_path = r'E:\矿产数据\数据\network\new\output_cutA.csv'
edges_df.to_csv(output_path, index=False)
print(f"Edge data successfully generated and saved to '{output_path}'")
