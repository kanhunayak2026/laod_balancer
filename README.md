
# Mini Load Balancer

A Python-based learning project to understand how load balancers distribute incoming HTTP requests across multiple backend servers using different load-balancing algorithms.

The project uses FastAPI and HTTPX to build a simple HTTP load balancer that forwards client requests to one of three backend servers.

## Project Architecture

Client Request
      |
      v
Load Balancer (Port 8000)
      |
      |------ Server A (Port 8001)
      |
      |------ Server B (Port 8002)
      |
      |------ Server C (Port 8003)

## Technologies Used

- Python
- FastAPI
- HTTPX
- Uvicorn

## Project Structure

    load_balance/
    |
    |-- server_a.py
    |-- server_b.py
    |-- server_c.py
    |-- load_balancer.py
    |-- test_load.py
    |-- README.md

## Installation

Install the required dependencies:

    pip install fastapi uvicorn httpx

## Running the Project

Start each backend server in a separate terminal.

**Server A:**

    uvicorn server_a:app --port 8001

**Server B:**

    uvicorn server_b:app --port 8002

**Server C:**

    uvicorn server_c:app --port 8003

Start the load balancer:

    uvicorn load_balancer:app --port 8000

Send requests to:

    http://127.0.0.1:8000/products

## Load Balancing Algorithms Implemented

### 1. Round Robin

Distributes incoming requests sequentially across available servers.

Example:

    Request 1 -> Server A
    Request 2 -> Server B
    Request 3 -> Server C
    Request 4 -> Server A

### 2. Weighted Round Robin

Assigns different weights to backend servers based on their capacity.

Example:

    Server A -> Weight 3
    Server B -> Weight 2
    Server C -> Weight 1

Request distribution:

    A -> A -> A -> B -> B -> C

Servers with higher weights receive more requests.

### 3. Least Connections

Selects the server with the lowest number of active connections.

Example:

    Server A -> 10 connections
    Server B -> 2 connections
    Server C -> 1 connection

Next request goes to Server C.

Note: The current implementation demonstrates the server-selection logic. Live connection tracking is not yet implemented.

### 4. Random Load Balancing

Selects a backend server randomly using Python's random.choice().

Example:

    Request 1 -> Server B
    Request 2 -> Server A
    Request 3 -> Server C

It does not consider the current workload of servers.

### 5. IP Hash

Uses the client's IP address and a hash function to determine which backend server receives the request.

The same IP generally maps to the same backend when the server list remains unchanged.

Useful for maintaining consistent routing for clients.

## Learning Objectives

- Understand how load balancers work.
- Learn different load-balancing algorithms.
- Understand how HTTP requests are forwarded between servers.
- Explore asynchronous programming using async and await.
- Understand the differences between request distribution strategies.

## Future Improvements

- Least Response Time algorithm.
- Server health checks.
- Better failure handling.
- Live connection tracking.
- Performance comparison between algorithms.

## Project Status

Currently implemented and studied:

- Round Robin
- Weighted Round Robin
- Least Connections (selection logic)
- Random
- IP Hash

This project is intended for learning and understanding load-balancing concepts rather than production deployment.
