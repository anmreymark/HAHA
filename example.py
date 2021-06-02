# Import the library
from playerio import *

# Connect to the game
client = Client('hello-world-f8wdei2ucusdudkhbayw9g', '_Kami', 'presepio')

# Count the number of players online
players_online = 0

for room in client.list_rooms('MyCode'):
    print(f"{room.data['name']} - {room.players_online} players online")
    print()
    players_online += room.players_online

print(f'Total: {players_online} users\n')


# Join a room
lol = client.create_join_room('test', 'MyCode', True)

username = 'Jarsu'

#run = "pip3 install \"protobuf>=3.4.0,<3.7\" && pip3 install discord && pip3 install flask && pip3 install asyncio && pip3 install requests && pip3 install datetime && pip3 install db-sqlite3 && python3 test.py"


print(client.bigdb_load('messageTable','CuzinXTosmaIILarge' 'receiver'))

#print(client.bigdb.deleteKeys('PlayerObjects', 'simple' + 'Jarsu'))


# Print all the incoming events from the room
@EventHandler.add()
def on_message(room, message):
    print(message)

# Handle disconnection
@EventHandler.add('playerio.disconnect')
def on_disconnect(room, message):
    print('Disconnected :(')

#pip3 install "protobuf>=3.4.0,<3.7"