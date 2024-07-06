import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('data.csv')

# Show unique values in 'Indicator', 'Group', 'Subgroup'
print("Unique values in 'Indicator':")
for i, indicator in enumerate(df['Indicator'].unique()):
    print(f"{i+1}. {indicator}")

indicator_num = int(input("Select an 'Indicator' by number: "))
selected_indicator = df['Indicator'].unique()[indicator_num-1]

print("\nUnique values in 'Group':")
for i, group in enumerate(df['Group'].unique()):
    print(f"{i+1}. {group}")

group_num = int(input("Select a 'Group' by number: "))
selected_group = df['Group'].unique()[group_num-1]

print("\nUnique values in 'Subgroup':")
for i, subgroup in enumerate(df['Subgroup'].unique()):
    print(f"{i+1}. {subgroup}")

subgroup_nums = list(map(int, input("Select up to 4 'Subgroup' by numbers (separated by space): ").split()))
selected_subgroups = df['Subgroup'].unique()[np.array(subgroup_nums)-1]

# Filter the data
filtered_df = df[(df['Indicator'] == selected_indicator) & 
                 (df['Group'] == selected_group) & 
                 (df['Subgroup'].isin(selected_subgroups))]

# Save the filtered data to new.csv
filtered_df.to_csv('new.csv', index=False)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size
linestyles = ['-', '--', '-.', ':']

for i, subgroup in enumerate(selected_subgroups):
    data = filtered_df[filtered_df['Subgroup'] == subgroup]
    data.reset_index(drop=True, inplace=True)  # Reset the index of the DataFrame
    ax.plot(data['Time Period Start Date'], data['Value'], linestyle=linestyles[i%4], color='black', label=subgroup)

# Set xticks to have around 7 labels
xticks = np.linspace(0, len(data['Time Period Start Date']) - 1, 7, dtype=int)
ax.set_xticks(xticks)
ax.set_xticklabels(data['Time Period Start Date'][xticks])

# Rotate x-axis labels by 90 degrees
plt.xticks(rotation=90)
plt.ylabel('Percent')
plt.title('Long COVID trends by age or by sex')

# Adjust subplot parameters for better layout
plt.tight_layout()

ax.legend()
plt.savefig('result.png',dpi=300)
plt.show()

