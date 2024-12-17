from datetime import datetime


def check_valid_date(text):
    # функция check_valid_date проверяет правильность введенных данных и запрашивает их снова, если данные невалидны
    while True:
        try:
            data = datetime.strptime(input(text), "%d-%m-%Y").strftime("%d-%m-%Y")
            return data
        except ValueError:
            print("Данные некорректны. Введите дату в формате день-месяц-год. Например, 01-01-2025")


note = {}
# узнаем и добавляем в словарь имя
note["username"] = input("Введите имя пользователя: ")

# запрашиваем и добавляем в словарь описание заметки
note["content"] = input("Введите описание заметки ")  # описание заметки

# добавляем в словарь статус заметки
note["status"] = "Создана"

# добавляем в словарь дату создания заметки
note["created_date"] = datetime.today().strftime("%d-%m-%Y")

# запрашиваем и добавляем в словарь дедлайн
note["issue_date"] = check_valid_date("Введите дедлайн в формате день-месяц-год ")

# запрашиваем и добавляем в словарь заголовки
note["titles"] = []
for i in range(3):
    title = input(f"Введите заголовок {i + 1} заметки ")  # заголовок заметки
    note["titles"].append(title)

print("\nВы ввели следующие данные:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
