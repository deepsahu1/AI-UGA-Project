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

#Flash app
app = dash.Dash(__name__, server = server)

#Setting layout
app.layout = html.Div([
    html.H1("Live Sensor Dashboard", style = {'fontSize' : '40px', 'textAlign' : 'center'}), 
    html.Div(id="live-reading", style={"fontSize": "24px", "marginTop": "20px"}),
    dcc.Store(id="row-index", storage_type = "session", data=0),
    dcc.Interval(id="interval-update", interval=5000, n_intervals=0) #Updates latest data every 15 minutes
])

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
   result = html.Div([
       html.P(f"Date: {current_row['Quarter_DDMMYYYY']}"),
       html.P(f"Temp: {current_row['Temp']}°C"),
       html.P(f"pH: {current_row['pH']}"),
       html.P(f"Turbidity: {current_row['Turbidity']}"),
       html.P(f"DO: {current_row['DO']} mg/L"),
   ])
   return result, row_index
   
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

