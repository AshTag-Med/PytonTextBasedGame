print('Hello, and welcome to \x1B[3mThe Long Road Home.\x1B[0m')
print('You are a weakened warrior who has just slain a dragon and want to make your way home to rest.')
print('You would like to pick up some food on your way back, but also hear that the bridge to you house is broken and is guarded by a troll.')
print('Unable to fight at the moment, you look for a way to overcome the problem in front of you.')
print()
print('Objective: Obtain the 6 items in the area from various locations before engaging the troll.')
print('Instructions:')
print('Move across different areas with "go" + "North/South/East/West".')
print('Obtain items with "get" + "item".')
print('To quit, type "Exit".')
print('Pay attention to capitalization!')
# Introduction

def get_item(current_room, move, rooms, inventory):
    # Function to add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']

def room_move(current_room, move, rooms):
    # Function to move to corresponding room
    current_room = rooms[current_room][move]
    return current_room

def main():
    # Primary gameplay function
    rooms = {
        'Starting Path': {'East': 'Wizard Shop', 'South':'Forest'},
        'Forest': {'South': 'General Store', 'East': 'Bakery', 'North': 'Starting Path','item': 'Lumber'},
        'General Store': {'East':'Blacksmith Shop', 'North':'Forest',  'item': 'Hammer'},
        'Blacksmith Shop': {'West': 'General Store' , 'East': 'Fisher Wharf' , 'North': 'Bakery', 'item': 'Anchor'},
        'Fisher Wharf':{'West':'Blacksmith Shop', 'item': 'Fish'},
        'Bakery':{'West':'Forest','North':'Wizard Shop','South': 'Blacksmith Shop', 'item': 'Bread'},
        'Wizard Shop':{'West':'Starting Path','East':'Troll Bridge' , 'South' : 'Bakery', 'item':'Sleeping Potion'},
        'Troll Bridge':{'West':'Wizard Shop'}
    }
    # Room dictionary

    current_room ='Starting Path'
    inventory = []

    while True:

        if current_room == 'Troll Bridge':
            if len(inventory) == 6:
                print('You have slept the Troll, fixed the bridge and made your way home!')
                print('Thank you for playing.')
                break
                # Win scenario
            else:
                print('You did not obtain all the needed items, and are now filled with despair')
                print('Game Over')
                break
                # Lose scenario
        print('You are in: '+ current_room)
        print('You currently have:', inventory)
        if 'item' in rooms[current_room].keys() and current_room != 'Troll Bridge':
            print('There is: ' + rooms[current_room]['item'] + ' here.')
        # Current character status
        move = input('What would you like to do?  ').title().split()
        # Player action input
        if move[0] == 'Exit':
            print('Thanks for playing, goodbye!')
            break
        # Quitting game scenario
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = room_move(current_room, move[1], rooms)
            continue
        # Moving between rooms

        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            get_item(current_room, move, rooms, inventory)
            continue
        # Obtaining items
        else:
            print('\033[1;31;40mCannot go there / No such item exists, make another move!\033[1;31;0m')
            continue
        # Invalid inputs

main()



