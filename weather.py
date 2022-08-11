"""Does operations from the data set of weather stats from O'hare international airport at Chicago."""


import sys

from csv import DictReader

from typing import List

from matplotlib import pyplot


def main() -> None:
    """Entrypoint of the program."""
    command_list: List[float] = list_command()
    min: float = find_min()
    max: float = find_max()
    average: float = find_average()
    if sys.argv[3] == "List" or sys.argv[3] == "list":
        print(command_list)
        exit()
    if sys.argv[3] == "min" or sys.argv[3] == "Min":
        print(min)
        exit()
    if sys.argv[3] == "max" or sys.argv[3] == "Max":
        print(max)
        exit()
    if sys.argv[3] == "avg":
        print(average)
        exit()
    if sys.argv[3] == "char":
        draw_char()
        exit()
    else:
        print("Invalid operation: " + sys.argv[3])
        exit()


def list_command() -> List[float]:
    """Given column, it changes it to a float list."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    else:
        file_handle = open(sys.argv[1], "r", encoding="utf8")
        csv_reader = DictReader(file_handle)
        row_list: List[float] = []
        for row in csv_reader:       
            for column in row:            
                if sys.argv[2] not in row:
                    print("Invalid column: " + sys.argv[2])
                    exit()
                elif row[column] == "SOD  ":
                    try:
                        row_list.append(float(row[sys.argv[2]]))
                    except ValueError: 
                        ValueError
                        
    return(row_list) 


def find_min() -> float:
    """Finds the minimum of a given column."""
    min_list: List[float] = list_command()
    i: int = 0
    min: float = 0.0
    min = min_list[0]
    while i < len(min_list):
        if min > min_list[i]:
            min = min_list[i]
        i += 1
    return min


def find_max() -> float:
    """Finds the maximum of a given column."""
    max_list: List[float] = list_command()
    i: int = 0
    max: float = 0.0
    max = max_list[0]
    while i < len(max_list):
        if max < max_list[i]:
            max = max_list[i]
        i += 1
    return max


def find_average() -> float:
    """Finds the average of a given column."""
    avg: float = 0.0
    avg_list: List[float] = list_command()
    for item in avg_list:
        avg += item
    new_avg: float = avg / len(avg_list)
    return new_avg


def draw_char() -> None:
    """Creates data chart with dates and the given column."""
    import matplotlib.pyplot as plt
    Data: List[float] = list_command()
    file_handle = open(sys.argv[1], "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    row_list: List[str] = []
    update_list: List[str] = []
    for row in csv_reader:       
        for column in row:
            if row[column] == "SOD  ":
                row_list.append(str(row["DATE"]))
    for items in row_list:
        items = items.split("T")
        update_list.append(str(items[0]))
    pyplot.xlabel("Dates")
    pyplot.ylabel(sys.argv[2])
    plt.scatter(update_list, Data)
    plt.show()


if __name__ == "__main__":
    main() 
