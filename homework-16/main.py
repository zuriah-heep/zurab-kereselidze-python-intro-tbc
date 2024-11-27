from admin import *
from common import *


def list_menu_items():
    print("User menu")
    print("1. list sessions")
    print("2. search movie")
    print("3. my tickets")
    print("4. admin")
    return process_user_input()

def greetings():
    print("Welcome to the movie ticket booking system")
    print("Please enter EXIT to exit")

def search_movie():
    print("Searching movie")
    if not sessions:
        print("No movies found")
        return

    film_input0 = input("Enter movie name: ")
    film_input = film_input0.lower().strip()
    session_ids = []
    for key, val in sessions.items():
        if film_input == val["film_name"].lower().strip():
            session_ids.append(key)

    if session_ids:
        print(f"{len(session_ids)} sessions for {film_input0} found:")
        for key in session_ids:
            print(f"\tSession ID: {key}")
            print(f"\tFilm name: {sessions[key]['film_name']}")
            print(f"\tStart time: {sessions[key]['start_time']}")
            print(f"\tRoom number: {sessions[key]['room_number']}")
            print(f"\tRoom length: {sessions[key]['room_length']}")
            print(f"\tRoom width: {sessions[key]['room_width']}")
            print(f"\tCapacity: {sessions[key]['capacity']}")
            print("\n")
    else:
        print("No movie found.")

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                search_movie()
            case "3":
                print("Listing tickets")
            case "4":
                admin_loop()
            case _:
                print("Invalid input")

def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                remove_sessions()
            case "3":
                add_session()
            case "4":
                edit_session()
            case "5":
                print("User menu")
                print("1. list sessions")
                print("2. search movie")
                print("3. my tickets")
                print("4. admin")
                return program_loop()
            case _:
                print("Invalid input")

def main():
    greetings()
    program_loop()


if __name__ == "__main__":
    main()
