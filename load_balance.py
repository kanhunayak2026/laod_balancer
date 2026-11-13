
from fastapi import FastAPI
import httpx

app = FastAPI()

servers = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002",
    "http://127.0.0.1:8003"
]

current_index = 0


def get_server():
    global current_index

    server = servers[current_index]

    current_index = (current_index + 1) % len(servers)

    return server


@app.get("/products")
async def load_balance():

    backend = get_server()

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{backend}/products"
        )

    return response.json()
