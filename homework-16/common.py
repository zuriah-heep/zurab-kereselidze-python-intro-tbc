from db import sessions

def process_user_input():
    user_input = input("->: ").lower()
    if user_input not in ["1", "2", "3", "4", "exit"]:
        print("Invalid input")
        return process_user_input()
    if user_input == "exit":
        print("Goodbye")
        exit()
    return user_input

def process_admin_input():
    user_input = input("->: ").lower()
    if user_input not in ["1", "2", "3", "4", "5", "exit"]:
        print("Invalid input")
        return process_admin_input()
    if user_input == "exit":
        print("Goodbye")
        exit()
    return user_input

def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return

    for key, val in sessions.items():
        print(f"\tSession ID: {key}")
        print(f"\tFilm name: {val['film_name']}")
        print(f"\tStart time: {val['start_time']}")
        print(f"\tRoom number: {val['room_number']}")
        print(f"\tRoom length: {val['room_length']}")
        print(f"\tRoom width: {val['room_width']}")
        print(f"\tCapacity: {val['capacity']}")
        print("\n")