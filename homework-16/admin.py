import random

from common import *
from db import sessions


def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    print("5. exit admin")
    return process_admin_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")

def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ").strip()
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    # TODO: session_id may be used already, need to check
    session_id = str(random.randint(1, 1000))
    while session_id in sessions:
        session_id = str(random.randint(1, 1000))
    sessions[session_id] = {
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")

def remove_sessions():
    print("Removing session")
    if not sessions:
        print("No sessions found")
        return

    print(f"Available sessions: {', '.join(sessions.keys())}")
    session_id = input("Session ID: ")
    if session_id in sessions:
        del sessions[session_id]
        print(f"Session {session_id} removed.\n")
    else:
        print(f"Session {session_id} not found.\n")

def edit_session():
    print("Editing session")
    if not sessions:
        print("No sessions found")
        return

    print(f"Available sessions: {', '.join(sessions.keys())}")
    session_id = input("Session ID: ")
    if session_id in sessions:
        print(f"Editing session {session_id}")
        film_name = input("Film name: ")
        start_time = input("Start time: ")
        room_number = input("Room number: ")
        room_length = int(input("Room length: "))
        room_width = int(input("Room width: "))
        capacity = room_length * room_width
        sessions[session_id] = {
            "film_name": film_name,
            "start_time": start_time,
            "room_number": room_number,
            "room_length": room_length,
            "room_width": room_width,
            "capacity": capacity
        }
        print("Session edited successfully")
    else:
        print(f"Session {session_id} not found.\n")