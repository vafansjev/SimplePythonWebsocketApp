import asyncio
import websockets

# Пустой словарь для изоляции каналов-получателей сообщения
server_connections = {}


async def server(websocket, path):
    """server, который получает на вход подключение и канал и удаляет вебсокет из словаря после отключения"""
    async for message in websocket:
        # Сообщение для отладки
        print(f'User {websocket.remote_address} sends message: {message} to {path}')

        # Если такого канала/пути не существует, то создать его
        if path not in server_connections:
            server_connections[path] = set()

        # По имени канала добавить новый вебсокет (объект-подключение)
        server_connections[path].add(websocket)

        # Переслать сообщение всем подключенным вебсокетам-получателям
        try:
            for conn in server_connections[path]:
                await conn.send(message)
        except websockets.exceptions.ConnectionClosedOK:
            break

    # Удалить текущий вебсокет из словаря на разрыве соединения
    for connections in server_connections.values():
        connections.discard(websocket)


async def main():
    """main, который бесконечно ждет клиентов"""
    async with websockets.serve(server, "0.0.0.0", 8765):
        print("WebSocket server started")
        await asyncio.Future()  # run forever


asyncio.run(main())



