from datetime import datetime


def check_valid_date(text):
    # функция check_valid_date проверяет правильность введенных данных и запрашивает их снова, если данные невалидны
    while True:
        try:
            data = datetime.strptime(input(text), "%d-%m-%Y").strftime("%d-%m-%Y")
            return data
        except ValueError:
            print("Данные некорректны. Введите дату в формате день-месяц-год. Например, 01-01-2025")


# создаем словарь и заполняем его данными
note = {"username": input("Введите имя пользователя: "), "content": input("Введите описание заметки "),
        "status": "Создана", "created_date": datetime.today().strftime("%d-%m-%Y"),
        "issue_date": check_valid_date("Введите дедлайн в формате день-месяц-год "), "titles": []}

for i in range(3):
    title = input(f"Введите заголовок {i + 1} заметки ")  # заголовок заметки
    note["titles"].append(title)

print("\nВы ввели следующие данные:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
