# 1
def largest_num(num_list: list) -> int:
    assert isinstance(num_list, list)
    m = max(num_list)
    if m >= 0:
        return m
    else:
        return "Число менше 0"

nums = [2, 3, 5, 1, 10]

print(largest_num(nums))

# 2
def number_of_letters(word: str) -> int:
    assert isinstance(word, str)
    num = len(word)
    return num

print(number_of_letters("word"))

# 3 
def exponent(base: int, power: int) -> int:
    assert isinstance(base, int)
    assert isinstance(power, int)
    assert power >= 0, "Степінь має бути не від'ємний."
    return base**power

print(exponent(2, 3))

# 4
def numbers(number: int) -> list:
    assert isinstance(number, int)
    output = []
    for i in range(1, number+1):
        output.append(i)
    return output
    
print(numbers(99))

# 5
def area(a: int, b: int) -> int:
    assert isinstance(a, int)
    assert isinstance(b, int)
    return a*b

print(area(2, 5))