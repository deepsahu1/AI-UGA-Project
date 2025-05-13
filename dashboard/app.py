import dash
from dash import html, dcc
from flask import Flask, request, jsonify
from dash.dependencies import Input, Output


#Flask server
server = Flask(__name__)

#Flash app
app = dash.Dash(__name__, server = server)

#Setting layout
app.layout = html.Div([
    html.H1("Live Sensor Dashboard", style = {'fontSize' : '40px', 'textAlign' : 'center'}), 
    html.Div(id="live-reading", style={"fontSize": "24px", "marginTop": "20px"}),
    dcc.Interval(id="interval-update", interval=3000, n_intervals=0) #Updates latest data every 3 seconds
])

@app.callback(
        Output("live-reading", "children"),
        Input("interval-update", "n_intervals")
)
def update(n):
    return f"Latest Data: {latest_data}"


@server.route("/post-sensor-data", methods = ["POST"])
def post_sensor_data():
    global latest_data
    latest_data = request.get_json() #gets JSON from request

    print("POST data successfully recieved", latest_data)
    return jsonify({"status": "received", "data": latest_data}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8051)

