try:
    number = 5 + "not a number"
except ValueError:
    print("Error : Invalid value.")
except TypeError:
    print("Error : Invalid type.")