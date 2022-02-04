#!/usr/bin/env python3

# Created by: Navin Baleko
# Created on: Feb 4 2022
# This program uses an associative array


def main():
    # this function uses an associative array

    airports = {}
    some_info = {'item1': 1,
                 'item2': 2,
    }

    # adding items
    airports['YYZ'] = "Toronto Pearson"
    airports['YOW'] = "Ottawa Canada"
    airports['DUB'] = "Dublin Ireland"
    airports['LHR'] = "London Heathrow"


    airport_name = input("Type in an airport code: ")
    if airport_name in airports.keys():
        print("The name of the airport you chose is {0}.".format(airports[airport_name]))
    else:
        print("That airport is not in the airport's dictionary.")
    print("")

    print("All the airports:")
    for key, value in airports.items():
        print("The airport code is {0} for {1}.".format(key, value))


if __name__ == "__main__":
    main()