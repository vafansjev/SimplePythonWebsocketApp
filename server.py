import asyncio
import websockets

# Our websocket server port
# If changed -> Don't forget to change it in Dockerfile (EXPOSE section) also if it needed
WS_PORT = 8765

# an empty dict that contains current connections
server_connections = {}


async def server(websocket, path):
    """
    Server itself. Gets connection and path (channel), add it to dict and delete when client disconnected
    """
    async for message in websocket:
        # Just a console debug message
        print(f'User {websocket.remote_address} sends message: {message} to {path}')

        # If there is no existing path (channel) then create it
        if path not in server_connections:
            server_connections[path] = set()

        # Add new websocket connection using path
        server_connections[path].add(websocket)

        # Send received message to all path listeners
        try:
            for conn in server_connections[path]:
                await conn.send(message)
        except websockets.exceptions.ConnectionClosedOK:
            break

    # Delete from dict when disconnected
    for connections in server_connections.values():
        connections.discard(websocket)


async def main():
    """
    This is main that starting new websocket server and waiting for a new client
    """
    async with websockets.serve(server, "0.0.0.0", WS_PORT):
        print("WebSocket server started")
        # Run forever
        await asyncio.Future()


asyncio.run(main())



