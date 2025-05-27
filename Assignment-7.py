"""
Assigment 7: Creating a Sensor List and Filter List
Submitted by Zainab Abdulhasan
Submitted: November 7, 2024

Assignment 6: Bubble sort using recursion

Assignment 5:Reverse a List using Recursion

Assignment 4: Creating a Sensor List and Filter List

Assignment 3: Implementing a Menu

Assignment 2: This assignment adds code to prompt the user for a temperature in Celsius and
then converts that temperature to a specified different temperature unit.

Assigment 1: This program demonstrates printing lines of text to the screen
"""


def recursive_sort(list_to_sort, key=0):
    """
    Recursively sorts a list of tuples using bubble sort.

    Args:
    list_to_sort (list): The list of tuples to be sorted.
    key (int): The index to sort by (0 for room number, 1 for room name).

    Returns:
    list: The sorted list.
    """
    if len(list_to_sort) <= 1:
        return list_to_sort

    swapped = False
    for i in range(len(list_to_sort) - 1):
        if list_to_sort[i][key] > list_to_sort[i + 1][key]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            swapped = True

    if not swapped:
        return list_to_sort

    return recursive_sort(list_to_sort[:-1], key) + [list_to_sort[-1]]


def print_header():
    print("STEM Center Temperature Project")
    print("Zainab Abdulhasan")


def print_menu():
    print("""
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
""")


def print_filter(sensor_list, filter_list):
    """Prints the list of sensors with their active/inactive status."""
    for room_number, room_name, sensor_id in sensor_list:
        status = "[ACTIVE]" if sensor_id in filter_list else ""
        # Display "Out: Outside" in exact required format
        if room_number == "OUT":
            print(f"Out: {room_name} {status}")
        else:
            print(f"{room_number}: {room_name} {status}")


def change_filter(sensors, sensor_list, filter_list):
    """Allows the user to toggle sensors on and off in the filter."""
    while True:
        print_filter(sensor_list, filter_list)
        room_number = input("\nType the sensor to toggle (e.g., 4201) or x to end: ").strip()

        if room_number.lower() == 'x':
            break

        # Normalize input to handle "Out" consistently
        normalized_room = "OUT" if room_number.lower() == "out" else room_number

        if normalized_room in sensors:
            sensor_id = sensors[normalized_room][1]
            if sensor_id in filter_list:
                filter_list.remove(sensor_id)
            else:
                filter_list.append(sensor_id)
        else:
            print("Invalid Sensor")


def new_file(dataset=None):
    print("New File Function Called, dataset:", dataset)


def choose_units():
    print("Choose Units Function Called")


def print_summary_statistics(dataset=None, active_sensors=None):
    print("Summary Statistics Function Called, dataset:", dataset, "active_sensors:", active_sensors)


def print_temp_by_day_time(dataset=None, active_sensors=None):
    print("Print Temp by Day/Time Function Called, dataset:", dataset, "active_sensors:", active_sensors)


def print_histogram(dataset=None, active_sensors=None):
    print("Print Histogram Function Called, dataset:", dataset, "active_sensors:", active_sensors)


def main():
    # Dictionary with sensor information
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "OUT": ("Outside", 5)
    }

    # a list of tuples (room number, room name, sensor ID)
    sensor_list = [(room_number, sensors[room_number][0], sensors[room_number][1]) for room_number in sensors]

    # Sort sensor_list by room number once before entering the menu
    sensor_list = recursive_sort(sensor_list, key=0)

    # Dynamic filter list that can be modified by the user
    filter_list = [sensor[2] for sensor in sensor_list]  # Initially, all sensors are active

    print_header()

    # Main program loop to display the menu and handle user input
    while True:
        print_menu()
        try:
            choice = int(input("What is your choice? "))
            if choice == 1:
                new_file()
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(sensors, sensor_list, filter_list)
            elif choice == 4:
                print_summary_statistics()
            elif choice == 5:
                print_temp_by_day_time()
            elif choice == 6:
                print_histogram()
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice, please enter an integer between 1 and 7.")
        except ValueError:
            print("*** Please enter a number only ***")
        print()


if __name__ == "__main__":
    main()



"""
"C:\\Users\\zandu\\python projects\\Assignment-7\\.venv\\Scripts\\python.exe" "C:\\Users\\zandu\\python projects\\Assignment-7\\Assignment-7.py" 
STEM Center Temperature Project
Zainab Abdulhasan

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 3
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g., 4201) or x to end: 4201
4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g., 4201) or x to end: 4205
4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g., 4201) or x to end: out
4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside 

Type the sensor to toggle (e.g., 4201) or x to end: out
4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g., 4201) or x to end: 4201
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g., 4201) or x to end: 4000
Invalid Sensor
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g., 4201) or x to end: x


Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 
"""
