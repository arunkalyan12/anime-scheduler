import json
import time


def add_anime():
    with open("schedule.json", 'r') as file:
        schedule = json.load(file)

    while True:
        try:
            day = input("\nEnter the day (e.g., Sunday, Monday): ")
            if day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                raise ValueError("Invalid day. Please enter a valid day.")

            airing_time = input("Enter the time (e.g., 8:00, 13:00): ")
            if not valid_time_format(airing_time):
                raise ValueError("Invalid time format. Please enter the time in HH:MM format.")

            anime = input("Enter the name of the anime: ")

            break
        except ValueError as e:
            print(f"Error: {e}")

    if day not in schedule:
        schedule[day] = {}

    schedule[day][airing_time] = anime

    with open("schedule.json", 'w') as file:
        json.dump(schedule, file, indent=4)

    print("\nNew anime added successfully!")


def edit_schedule():
    with open("schedule.json", 'r') as file:
        schedule = json.load(file)

    while True:
        try:
            day = input("\nEnter the day (e.g., Sunday, Monday): ")
            if day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                raise ValueError("Invalid day. Please enter a valid day.")

            airing_time = input("Enter the time (e.g., 8:00, 13:00): ")
            if not valid_time_format(airing_time):
                raise ValueError("Invalid time format. Please enter the time in HH:MM format.")

            anime = input("Enter the name of the anime: ")

            break
        except ValueError as e:
            print(f"Error: {e}")

    for schedule_day in schedule.values():
        if any(anime == value for value in schedule_day.values()):
            delete_anime(anime)

    if day not in schedule:
        schedule[day] = {}

    schedule[day][airing_time] = anime

    with open("schedule.json", 'w') as file:
        json.dump(schedule, file, indent=4)

    print("\nSchedule edited successfully!")


def delete_anime(anime):
    with open("schedule.json", 'r') as file:
        schedule = json.load(file)

    for day_schedule in schedule.values():
        for time, scheduled_anime in list(day_schedule.items()):
            if scheduled_anime == anime:
                del day_schedule[time]

    with open("schedule.json", 'w') as file:
        json.dump(schedule, file, indent=4)

    print(f"Deleted all instances of '{anime}' from the schedule.")


def remove_all():
    schedule = {}

    with open("schedule.json", 'w') as file:
        json.dump(schedule, file, indent=4)

    print("All animes are removed from schedule.")


def valid_time_format(time_str):
    try:
        time.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False



options = [1, 2, 3, 4]
print("Make sure that the main schedule program is not running during the time of making changes.")
option = 1
while option in options:
    option = int(
        input("\n1. Add Anime \n2. Edit schedule \n3. Delete anime \n4. Clear Schedule \nSelect your option: "))
    if option == 1:
        add_anime()
    elif option == 2:
        edit_schedule()
    elif option == 3:
        anime = input("Name the anime that you want to delete: ")
        delete_anime(anime)
    elif option == 4:
        remove_all()
