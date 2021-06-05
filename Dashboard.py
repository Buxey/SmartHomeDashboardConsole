from Room import Room


# start building your classes this might help you build your project

# 1) get number of rooms
# 2) get number of plugs
# 3) do a for loop for each room on its own, sorting out any variables that need to be sorted out
# 4) add that room object to the end of the array of rooms at the end of each iteration
# 5) do a for loop sorting out the plugs
# 6) add each plug object to the room (however you've done this)

def main():
    number_of_rooms = int(input("How many rooms are there in this property?: "))
    number_of_smartplugs = int(input("How many plugs do you want to place in this property?: "))

    rooms = []
    for i in range(number_of_rooms):
        name_of_rooms = input("Please provide a name for your room/rooms separated by a space: ")
        rooms.append(name_of_rooms)
        print(i + 1, rooms[i])
        # Room(room_id, name_of_rooms[i])


main()
