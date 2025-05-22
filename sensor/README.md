# Sensor API Client

This is a minimal Python wrapper for reading live sensor data from the local FastAPI server running on the Raspberry Pi sensor system.

- Sends a `GET` request to the server at `/read`
- Parses the response JSON
- Converts the `last_update` timestamp string to a native `datetime` object (if present)
- Returns a Python `dict` with typed access via a `TypedDict` (`SensorData`)

## 📂 Usage

Place the `sensor/` directory in the root of your project.

```bash
your-project/
├── main.py
└── sensor/
    ├── __init__.py
    └── sensor.py
```

Then import and use it like this:

```python
from sensor import read

# Use local=True if calling from the Raspberry Pi (default value)
# Use local=False if calling from another device on the Tailnet
data = read(local=True)

print(data["temperature"])
```

## 📘 API Reference

### `read(local: bool = True) -> SensorData`

Reads the current sensor state.

Arguments:
- `local` (`bool`, default `True`) — whether to connect to the local server (`localhost`) or use the Tailscale address.

Returns:
- `sensor_ready`: `bool` — whether the sensor has been initialized and is providing meaningful data
- `last_update`: `datetime | None` — when the last sensor reading was taken (UTC)
- `uptime`: `float | None` — seconds since system start
- `turbidity`, `temperature`, `total_dissolved_solids`, `pH`: `float | None`

If `sensor_ready` is `False`, the other fields will be `None`.

## 🧪 Example Output

```json
{
  "sensor_ready": true,
  "last_update": "2025-05-21T20:30:38.471Z",
  "uptime": 4.21,
  "turbidity": 2.31,
  "temperature": 21.4,
  "total_dissolved_solids": 412.7,
  "pH": 7.0
}
```

## 🌐 Connectivity

- By default, the wrapper targets `http://localhost:8000` (`127.0.0.1:8000`), which is optimal for programs running **directly on the Raspberry Pi**.
- The FastAPI server binds to `0.0.0.0:8000`, meaning it **listens on all network interfaces**. This includes:
  - `http://localhost:8000` (`127.0.0.1:8000`)
  - `http://geologypi.elephant-city.ts.net:8000` (`100.68.5.52:8000`), the Raspberry Pi’s **Tailscale** address.
- To use the API from **another device on the same Tailnet**, call `read(local=False)` to connect via the Raspberry Pi’s Tailscale address.

[Read more about Tailscale here.](../tailscale/README.md)