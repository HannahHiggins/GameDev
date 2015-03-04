""" Movement """

#Basic
def movement(command):
    if (command == "North"):
        x_change = 0
        y_change = 1
        return x_change, y_change
    if (command == "South"):
        x_change = 0
        y_change = -1
        return x_change, y_change
    if (command == "East"):
        x_change = 1
        y_change = 0
        return x_change, y_change
    if (command == "West"):
        x_change = -1
        y_change = 0
        return x_change, y_change
    else:
        print("Not a valid response (North, South, East, West")