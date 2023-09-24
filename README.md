# datasci_4_web_viz
## HHA 507 Homework Assignment 4
### Challenges 
#### Shiny R
The first challenge I encountered occured when I was filtering the dataset. I had written "obesity" instead of "OBESITY" and this resulted in the counties not appearing in the drop-down box for the graph. The graph and the drop-down box appeared, but when trying to use the drop-down, to display the different counties to choose from, none of the counties were there. Once I changed the word "obesity," the drop-down box displayed all of the counties from my dataset. However, this is where I encountered my second challenge. The graph would not populate when setting the drop-down to a specific county. I tried each county and nothing would appear on the graph indicating a data point.     
#### Python's Shiny 
The first challenge I encountered was Google Colab stating that within this code, the "ouput" was not defined. 
```
def server(input, output, session):

    @output
    @render.text
    def avg_data_value():
        selected_county = input.county()
        avg_value = df_obesity[df_obesity['LocationName'] == selected_county]['Data_Value'].mean()
        return f"Average Obesity Crude Prevalence for {selected_county}: {avg_value:.2f}%"
    @output
    @render.plot(alt="Average Obesity Crude Prevalence Bar Chart")
    def bar_chart():
        overall_avg = df_obesity['Data_Value'].mean()
        selected_county_avg = df_obesity[df_obesity['LocationName'] == input.county()]['Data_Value'].mean()

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(['Selected County', 'Overall Average'], [selected_county_avg, overall_avg], color=['lightcoral', 'dodgerblue'])
        
        ax.set_ylabel('Data Value (Crude prevalence) - Percent')
        ax.set_ylim(0, 30)
        ax.set_title('Obesity Crude Prevalence Comparison')
        
        return fig
```
Before putting it altogether, in one code block, I separated the code. Once I placed it altogether the code ran successfully. This is because the "output" was now defined a few lines ahead. 
