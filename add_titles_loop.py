from datetime import datetime


def check_valid_date(text):
    # функция check_valid_date проверяет правильность введенных данных и запрашивает их снова, если данные невалидны
    while True:
        try:
            data = datetime.strptime(input(text), "%d-%m-%Y").strftime("%d-%m-%Y")
            return data
        except ValueError:
            print("Данные некорректны. Введите дату в формате день-месяц-год. Например, 01-01-2025")


def add_titles():
    # функция add_titles реализует ввод и проверку на уникальность введенных заголовков
    # получение первого заголовка заметки
    title = input("Введите заголовок заметки или оставьте пустым для завершения ввода ")
    while title.strip() != "":
        # проводим проверку на уникальность заголовка и добляем в список в случае успешного прохождения проверки
        if title.strip().capitalize() not in note["titles"]:
            note["titles"].append(title.strip().capitalize())
        title = input(
            "Введите следующий заголовок заметки или оставьте поле пустым для завершения ввода ")  # заголовок заметки


# создаем словарь и заполняем его данными
note = {"username": input("Введите имя пользователя: "), "content": input("Введите описание заметки "),
        "status": "Создана", "created_date": datetime.today().strftime("%d-%m-%Y"),
        "issue_date": check_valid_date("Введите дедлайн в формате день-месяц-год "), "titles": []}

# считываем заголовки
add_titles()

# выводим данные
print("\nВы ввели следующие данные:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
