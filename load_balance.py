
from fastapi import FastAPI,Request
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


def get_server(client_ip):

    server_index = hash(client_ip) % len(servers)

    return servers[server_index]




@app.get("/products")
async def load_balance(request:Request):
    client_ip = request.client.host
    backend = get_server()

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{backend}/products"
        )

    return response.json()
