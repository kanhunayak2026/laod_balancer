
from fastapi import FastAPI
import httpx

app = FastAPI()



servers = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002",
    "http://127.0.0.1:8003"
]

connections = {
    servers[0]: 10,
    servers[1]: 2,
    servers[2]: 1
}

def get_server():

    server = min(
        connections,
        key=connections.get
    )

    return server




@app.get("/products")
async def load_balance():

    backend = get_server()

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{backend}/products"
        )

    return response.json()
