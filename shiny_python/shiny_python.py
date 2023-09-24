from shiny import App, render, ui
import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets  # Import ipywidgets

# Load the dataset
def load_data():
    url = "https://raw.githubusercontent.com/Alyssasorensen/datasci_4_web_viz/main/datasets/PLACES__Local_Data_for_Better_Health__County_Data_2023_release%20(1).csv"
    return pd.read_csv(url)

df = load_data()

# Filter for 'OBESITY' as measureid and 'Crude prevalence' as data_value_type
df = df[(df['MeasureId'] == 'OBESITY') & (df['Data_Value_Type'] == 'Crude prevalence')]

# Group by 'LocationName' and get the average (or sum) 'Data_Value'
grouped = df.groupby('LocationName').Data_Value.mean().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 7))
grouped.plot(kind='bar', color='lightcoral')
plt.ylabel('Average Data Value (Crude prevalence) - Percent')
plt.xlabel('Location (County)')
plt.title('Obesity Crude Prevalence by County in Alabama')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("obesity_per_location.png")  # Saving the plot as an image
plt.show()

# Compute the average data value across all counties
avg_data_value = df['Data_Value'].mean()

# Sort the counties in ascending order for the dropdown list
sorted_counties = sorted(df['LocationName'].unique())

# Interactive selection of county for visualization using ipywidgets
@widgets.interact(County=sorted_counties)
def plot_data(County):
    county_value = df[df['LocationName'] == County]['Data_Value'].values[0]

    # Labels for bars
    labels = [County, 'Average across all counties']

    # Data values for bars
    values = [county_value, avg_data_value]

    plt.figure(figsize=(8, 6))

    # Plot the bars
    colors = ['lightcoral', 'lightblue']
    plt.bar(labels, values, color=colors)

    plt.ylabel('Data Value (Crude prevalence) - Percent')
    plt.title(f'Obesity Crude Prevalence in {County} vs Average across all counties')

    plt.tight_layout()
    plt.show()

