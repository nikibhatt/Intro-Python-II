from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty \
passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling \
into the darkness. Ahead to the north, a light flickers in \
the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west \
to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure \
chamber! Sadly, it has already been completely emptied by \
earlier adventurers. The only exit is to the south.")
}


# Link rooms together
#
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items in the rooms
item_list = {
    'book' : Item("book", "You'll enjoy reading this book"),
    'coins' : Item("coins", "Collect coins"),
    'wand' : Item("wand", "Magic wand"),
    'weapon' : Item("weapon", "You might need it"),
    'food' : Item("food", "Incase you get hungry"),
    'water' : Item("water", "You might get thirsty"),
    'map' : Item("map", "In case you get lost")
    }

room['outside'].items.append(item_list['book'])
room['outside'].items.append(item_list['coins'])
room['foyer'].items.append(item_list['wand'])
room['foyer'].items.append(item_list['weapon'])
room['overlook'].items.append(item_list['food'])
room['narrow'].items.append(item_list['water'])
room['treasure'].items.append(item_list['map'])

player = Player(room['outside'])

play_status = 'p'
item_picked = ''
while play_status != 'q':
    print("-----------------------------")
    print(f"\nPlayer, You are in room \"{player.current_room.name}\"")
    print(f"About this room : {player.current_room.description}")
    print(f"This room has - {player.current_room.list_items()}\n")
    if (item_picked == '' or item_picked == 'None' or item_picked == 'none'):
        pass
    else:
        print(f"You have {item_picked.name}")
        print("--------------------------------\n")
        print(f"Drop your item in this room?")
        ans= input("Yes or No:")
        if (ans == 'Yes' or ans == 'yes'):
            player.current_room.items.append(item_picked)
            print(f"This room now has - {player.current_room.list_items()}\n")
            item_picked=''
    item_chosen_str = input("Enter the item you want to pick or \'None\': ")
    print(item_chosen_str)
    item_picked = item_list[item_chosen_str]
    if (item_picked == '' or item_picked == 'None' or item_picked == 'none'):
        pass
    else:
        player.current_room.items.remove(item_picked)
        pass
    print("Print n:s:e:w to move q to quit")
    direction = input("Enter your choice: ")
    if direction not in ('s','e','w','q', 'n'):
        print("Invalid input")
    elif direction == 'q':
        break
    new_room =''
    if direction == 's' and player.current_room.s_to is not None:
        player.current_room = player.current_room.s_to
    elif direction == 'n' and player.current_room.n_to is not None:
        player.current_room = player.current_room.n_to
    elif direction == 'e' and player.current_room.e_to :
        player.current_room = player.current_room.e_to
    elif direction == 'w' and player.current_room.w_to != '':
        player.current_room = player.current_room.w_to
    else:
        print("Move not allowed")
