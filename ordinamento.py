# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element


def sorted_list(lista):
    sorted_list = sorted(lista, reverse=True)
    return sorted_list
