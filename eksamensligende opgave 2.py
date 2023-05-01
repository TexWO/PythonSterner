

def find_max(list: list) -> int:
    """Finds the maximum value in a list of integers and returns it"""
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    print(max)  

#find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

"""The function can also be written as: max(list), This is simply just a python shortcut for the function."""


"""The function below just compares both lists and prints out if they are equal or not."""

def sammenligne(list1: list, list2: list) -> bool:

    if set(list1) == set(list2):
        return True
    else:
        return False

#print(sammenligne(['A','B',20,30], ['A','C',20,30]))
