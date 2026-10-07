queue = [("Annie", "Dancing Power"),("Davido","Assurance"), ("Victony","Fresh"),("Asake","Joha")]

def show_queue(queue):
    """This function is going to print everyone in the queue"""
    print()
    if len(queue) == 0:
        print("there are no more individuals available")
    else:
        print("Current Queue")
        for i,q in enumerate(queue):
            name, song = q
            print(f"{i+1}). {name} - {song}")

    print()
    print("Options: add / remove / top / next / quit")

def prompt_for_singer():
    command = input("Enter a Singer of your choice: ").lower().strip().title()
    command_song = input("Enter their song of choice: ").lower().strip().title()

    return command, command_song

def next_singer(queue):
    if len(queue) == 0:
        print("Oops! There's no one")
        return

    grouped = queue.pop(0)
    name,song = grouped
    print()
    print(f"Now Up: {name} - {song}")

def move_to_top(queue):
    if len(queue) < 2:
        print("Karaoke participants have to be at least 2 individuals")
        return

    try:
        moving = int(input("Which position do you want to move? "))
        print()
        if moving>1 and moving <= len(queue):
            removed = queue.pop(moving-1)
            queue.insert(0, removed)
            print(f"{removed[0]} is now at the top!")
        else:
            print(f"your number/position was invalid, there is no artist at {moving}")
            return
    except ValueError:
        print("Please enter a number")


def add_singer(queue):
    """This function is going to add a singer in the queue"""
    artist, song = prompt_for_singer()
    value = (artist, song)
    queue.append(value)

    print(f"your artist {artist} with the song {song} was added successfully")

def remove_singer(queue):
    """This function is going to remove a singer from the queue"""
    if len(queue) == 0:
        print("Oops, There is no person on the list to remove")
        return

    command = input("Type the artist you want to remove: ").lower().strip().title()
    for artist in queue:
        if artist[0] == command :
            print(f"{command} has been removed")
            print("\n")
            queue.remove(artist)
            return

    print(f"No match for {command} was found")


def run_app(queue):
    print("="*44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)

        command = input("> ").lower().strip()

        if command == 'quit':
            is_running = False
            print("Goodnight")

        elif command == 'add':
            add_singer(queue)

        elif command == 'remove':
            remove_singer(queue)

        elif command == 'top':
            move_to_top(queue)

        elif command == 'next':
            next_singer(queue)

        else:
            print(f"Sorry, the word {command} is not present in the menu")


run_app(queue)