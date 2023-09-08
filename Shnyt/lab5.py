from typing import Union


def get_max_val(lst: list) -> Union[str, int]:
    return max(lst) if max(lst) > 0 else 'Максимальне значення менше нуля'

def get_lenght(vari: str) -> int:
    return len(vari)

def get_power(num: int, power: int) -> Union[str, int]:
    return pow(num, power) if power > 0 else 'Степінь від`ємний'

def get_numbers(num: int) -> None:
    print(*[x for x in range(1, num+1)])

def rectangle_area(widht: int, height: int) -> int:
    return widht*height


print(get_max_val([-1,0]))
print(get_lenght('Привіт'))
print(get_power(2,-8))
get_numbers(4)
print(rectangle_area(2,6))