""" Movement """

#Basic
def movement(command):
    #just adds 1 unit onto the current location co-ords
    if (command == "N"):
        x_change = 0
        y_change = 1
        return x_change, y_change
    if (command == "S"):
        x_change = 0
        y_change = -1
        return x_change, y_change
    if (command == "E"):
        x_change = 1
        y_change = 0
        return x_change, y_change
    if (command == "W"):
        x_change = -1
        y_change = 0
        return x_change, y_change
    else:
        print("Not a valid response (N, S, E, W")