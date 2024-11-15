search = []

counter = 0

search_string = input("Строка для поиска: ")

with open("text.txt", 'r', encoding='utf-8') as file:# чтение файла text
    for line in file:
        if search_string in line:  # Проверка, содержится ли подстрока в строке
            search.append(line)  
            counter += 1

print(f"Найдено строк: {counter}")
print(f"Сортированые строки {sorted(search)}")