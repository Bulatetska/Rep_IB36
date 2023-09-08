from typing import Tuple

def remove_pairs(lst: list[int]) -> Tuple[list, list]:
    new_list, duplicates = [], []

    for i in lst:
        if i not in new_list:
            new_list.append(i)
        elif i not in duplicates:
            duplicates.append(i)

    print(f'Оригінальний список: {lst}\nСписок без дублікатів: {new_list}\nДублікати: {duplicates}\n')
    return new_list, duplicates    


def square_list(lst: list[int]) -> list:
    result = [x*x for x in lst]

    print(f'Оригінальний список: {lst}\nУсі елементи в квадараті: {result}\n')
    return result

def max_element(lst: list[int]) -> int:
    max_elem = max(lst)

    print(f'Максимальний елемент списку {lst}: {max_elem}\n')
    return max_elem


remove_pairs([1,2,7787,32,1,4,321,321,312,2,2,2,2,2,2,3,4,5,6,7,8,9])
square_list([1,2,3,4,5,6,7,8,9,10])
max_element([1,2,3,4,-21331])
