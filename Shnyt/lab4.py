from typing import Tuple

def difference(A: set, B: set) -> set:
    result = A.difference(B)
    print(f'Множина A: {A}, Множина B: {B}\n Елементи які належать A, але не належать B: {result}')
    return result

def intersection(A: set, B: set) -> set:
    result = A.intersection(B)
    print(f'Множина A: {A}, Множина B: {B}\n Елементи які належать A, та B: {result}')
    return result

def union(A: set, B: set) -> set:
    result = A.union(B)
    print(f'Множина A: {A}, Множина B: {B}\n Об`єднання множин A, та B: {result}')
    return result

def unique_elements(vari: str) -> bool:
    result = len(vari) == len(set(vari))
    
    if result:
        print(f'Усі символи в рядку: {vari} Унікальні')
    else:
        print(f'Cимволи в рядку: {vari} Не унікальні')

def count_element(lst: list) -> dict:
    result = {x:lst.count(x) for x in lst}

    print(result)
    return result

def pair_key(dct: dict) -> list[str]:
    #return [result.append(dct[key]) for key in dct.keys() if len(key) == 2]
    result = []

    for key in dct.keys():
        if len(key) == 2:
            result.append(dct[key])
    
    print(f'Усі значення з словнику {dct}, які мають парний ключ: {result}')

def remove_a_key(dct:dict) -> dict:
    dct_2 = {}

    for key, value in dct.items():
        if key.startswith('a'):
            continue
        
        dct_2[key] = value

    print(dct_2)
    return dct_2


A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
lst = [1,2,2,2,2,3,4,1,321,321,321,312,21,321,2,31,321]
dct = {'a1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'11','12':'12'}

