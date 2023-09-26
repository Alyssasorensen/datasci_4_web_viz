# datasci_4_web_viz
## HHA 507 Homework Assignment 4
### Challenges 
#### Shiny R
The first challenge I encountered occured when I was filtering the dataset. I had written "obesity" instead of "OBESITY" and this resulted in the counties not appearing in the drop-down box for the graph. The graph and the drop-down box appeared, but when trying to use the drop-down, to display the different counties to choose from, none of the counties were there. Once I changed the word "obesity," the drop-down box displayed all of the counties from my dataset. However, this is where I encountered my second challenge. The graph would not populate when setting the drop-down to a specific county. I tried each county and nothing would appear on the graph indicating a data point. My third challenge was the error code I kept receiving when trying to deploy my Shiny app on shinyapps.io.
```
rsconnect deploy shiny ~/datasci_4_web_viz --name datasci_4_web_viz --title "My Shiny App"
```
This code kept giving me the error message, "[WARNING] 2023-09-25T03:04:03+0000 Can't determine entrypoint; defaulting to 'app'
    Warning: Capturing the environment using 'pip freeze'.
             Consider creating a requirements.txt file instead.
Error: The nickname, "datasci_4_web_viz", does not exist." I was getting confused because the nickname for my Shiny R code is "datasci_4_web_viz."
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
#### Flask 
The first challenge I encountered was when using Google Colab. I was using the code below and I kept getting an error message that stated "AssertionError: View function mapping is overwriting an existing endpoint function: index." Initially, I had the code in seperate code blocks and the error messaged continued to appear. Once I put the code altogether, the error message no longer appeared.  
```
app = Flask(__name__)

# Load the dataset
url = "https://raw.githubusercontent.com/Alyssasorensen/datasci_4_web_viz/main/datasets/PLACES__Local_Data_for_Better_Health__County_Data_2023_release%20(1).csv"
df = pd.read_csv(url)
df_obesity = df[(df['MeasureId'] == 'OBESITY') & (df['Data_Value_Type'] == 'Crude prevalence')]

@app.route('/', methods=['GET', 'POST'])
def index():
    counties = sorted(df_obesity['LocationName'].unique())
    selected_county = request.form.get('county') or counties[0]
    img = create_plot(selected_county)
    
    return render_template("index.html", counties=counties, selected_county=selected_county, img=img)

def create_plot(county):
    overall_avg = df_obesity['Data_Value'].mean()
    selected_county_avg = df_obesity[df_obesity['LocationName'] == county]['Data_Value'].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['Selected County', 'Overall Average'], [selected_county_avg, overall_avg], color=['lightcoral', 'dodgerblue'])
    ax.axhline(selected_county_avg, color='gray', linestyle='dashed', alpha=0.7)
    ax.set_ylabel('Data Value (Crude prevalence) - Percent')
    ax.set_ylim(0, 30)
    ax.set_title('Obesity Crude Prevalence Comparison')
    
    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True)
```
