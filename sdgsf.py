def main_menu():
    # Print instructions and intro
    print("Vampire Adventure Game")
    print("Collect 6 items to win the game, or be slain by the vampire.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of connecting rooms with items
    rooms = {
        'Main Cellar': {'South': 'Butlers Quarters', 'North': 'Old Armory', 'East': 'Chapel', 'West': 'Mess Hall'},
        'Butlers Quarters': {'North': 'Main Cellar', 'East': 'Tool Room', 'item': 'Wooden Stake'},
        'Tool Room': {'West': 'Butlers Quarters', 'item': 'Hammer'},
        'Old Armory': {'South': 'Main Cellar', 'West': 'Vampires Lair', 'East': 'Blacksmith', 'item': 'Plate Armor'},
        'Blacksmith': {'West': 'Old Armory', 'item': 'Silver Sickle'},
        'Mess Hall': {'East': 'Main Cellar', 'item': 'Garlic'},
        'Chapel': {'West': 'Main Cellar', 'item': 'Unholy Symbol'},
        'Vampires Lair': ''
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    # starting room
    current_room = "Main Cellar"
    # show the player the main menu
    main_menu()

    while True:
        # handle the case when player encounters the 'villain'
        if current_room == 'Vampires Lair':
            # winning case
            if len(inventory) == 6:
                print('Congratulations you have defeated Lord Drakan and saved the town!')
                print('Thank you for playing!')
                break
            # losing case
            else:
                print('\nOh dear! You did not collect all of the items!')
                print('You were vanquished by Lord Drakan and the town was destroyed!')
                print('Thank you for playing!')
                break
        # Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print(inventory)
        # tell the user if there is an item in the room
        if current_room != 'Vampires Lair' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # handle if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()