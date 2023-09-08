import string, random, datetime, json

def generate_file() -> None:
    with open('test25.txt', 'w') as file:
        file.write(''.join(random.choice(string.ascii_letters) for _ in range(25)))


def dict_generate(names:list) -> None:
    current_date = datetime.datetime.now().strftime('%d;%m;%y')

    lst = [{"name":name, "age": random.randrange(1,100)} for name in names]

    result = {
        "data":lst, 
        "created_at": current_date}


    with open(f'users_data_{current_date}.json', 'w') as file:
        json.dump(result, file, indent=3, ensure_ascii=False)


generate_file()
dict_generate(names = ['Артур', 'Кейт', 'Аліса', 'Майк'])