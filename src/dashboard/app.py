import dash
from dash import html, dcc
from flask import Flask, request, jsonify
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv("data/raw/data.csv")

df.columns = df.columns.str.strip()

#Flask server
server = Flask(__name__)
server.config["latest_data"] = "No data yet"

#Dash app
app = dash.Dash(__name__, server = server)

# Custom theme
theme = {
    'backgroundColor': '#1c1c1c',
    'textColor': '#FFA500',
    'fontFamily': 'Segoe UI, sans-serif',
    'fontWeight': '500',  # Semi-bold
}

#Setting layout
app.layout = html.Div([
    html.Link(href="https://fonts.googleapis.com/css2?family=Segoe+UI&display=swap", rel="stylesheet"), # text font

     html.H1("Live Sensor Dashboard", style={
        'fontSize': '40px',
        'textAlign': 'center',
        'color': theme['textColor'],
        'fontFamily': theme['fontFamily'],
        'fontWeight': theme['fontWeight']
    }), 
     html.Div(id="live-reading", style={
        "fontSize": "24px",
        "marginTop": "20px",
        "color": theme['textColor'],
        "fontFamily": theme['fontFamily'],
        "fontWeight": theme['fontWeight']
    }),
    dcc.Store(id="row-index", storage_type = "session", data=0),
    dcc.Interval(id="interval-update", interval=5000, n_intervals=0) #Updates latest data every 15 minutes
], style={'backgroundColor': theme['backgroundColor'], 'height': '100vh', 'padding': '40px'})

@app.callback(
        Output("live-reading", "children"),
        Output("row-index", "data"),
        Input("interval-update", "n_intervals"),
        State("row-index", "data")
        
)
def update_dashboard(n, row_index):
   if row_index is None:
        row_index = 0
   if row_index >= len(df):
       return html.Div("Reached the end of the dataset."), row_index
   current_row = df.iloc[row_index]
   row_index += 1
   return html.Div([
       html.P(f"Date: {current_row['Quarter_DDMMYYYY']}"),
       html.P(f"Temp: {current_row['Temp']}°C"),
       html.P(f"pH: {current_row['pH']}"),
       html.P(f"Turbidity: {current_row['Turbidity']}"),
       html.P(f"DO: {current_row['DO']} mg/L"),
    ], style={
       'color': theme['textColor'],
       'fontFamily': theme['fontFamily'],
       'fontWeight': theme['fontWeight']
    }), row_index
   
"""
@server.route("/post-sensor-data", methods = ["POST"])
def post_sensor_data():
    latest_data = request.get_json() #gets JSON from request
    server.config["latest_data"] = latest_data

    print("POST data successfully recieved", latest_data)
    return jsonify({"status": "received", "data": latest_data}), 200
"""

if __name__ == "__main__":
    app.run(debug=True, port=8049)

