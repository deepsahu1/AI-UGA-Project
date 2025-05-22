import requests
from typing import TypedDict
from datetime import datetime

class SensorData(TypedDict):
    sensor_ready: bool
    last_update: datetime | None
    uptime: float | None
    turbidity: float | None
    temperature: float | None
    total_dissolved_solids: float | None
    pH: float | None

LOCAL_URL = "http://localhost:8000"
TAILSCALE_URL = "http://geologypi.elephant-city.ts.net:8000"

def read(local=True) -> SensorData:
    """
    Reads the current sensor state from the local FastAPI backend.

    Example return:
    {
        "sensor_ready": true,
        "last_update": "2025-05-21T20:30:38.471Z",
        "uptime": 0,
        "turbidity": 0,
        "temperature": 0,
        "total_dissolved_solids": 0,
        "pH": 0
    }

    Returns:
        A dictionary representing the current sensor state.
    """

    BASE_URL = LOCAL_URL if local else TAILSCALE_URL

    response = requests.get(f"{BASE_URL}/read", timeout=2)
    response.raise_for_status()
    data = response.json()

    if data.get("last_update"):
        data["last_update"] = datetime.fromisoformat(data["last_update"].replace("Z", "+00:00"))

    return data