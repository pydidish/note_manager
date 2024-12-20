from datetime import datetime


def check_valid_date(text):
    # функция check_valid_date проверяет правильность введенных данных и запрашивает их снова, если данные невалидны
    input_date = ''
    while True:
        try:  # считываем и проверяем введенную строку на соответствие требуемому формату даты
            input_date = input(text)
            data = datetime.strptime(input_date, "%d-%m-%Y").strftime("%d-%m-%Y")
            return data
        except ValueError:
            try:  # проверяем не ввел ли пользователь дату в формате год-месяц-день
                data = datetime.strptime(input_date, "%Y-%m-%d").strftime("%d-%m-%Y")
                return data
            except ValueError:
                try:  # проверяем не ввел ли пользователь дату в формате месяц-день-год
                    data = datetime.strptime(input_date, "%m-%d-%Y").strftime("%d-%m-%Y")
                    return data
                except ValueError:
                    print("Данные некорректны. Введите дату в формате день-месяц-год. Например, 01-01-2025")


def output_note():
    print("\nВы ввели следующие данные:")
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")


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


def check_deadline(date):
    # проверяем сколько осталось до дедлайна
    now = today_without_time()
    d = datetime.strptime(date, "%d-%m-%Y") - now  # считаем время до дедлайна
    if d.days == 0:
        print("Внимание! Дедлайн сегодня!")
    elif d.days <= 0:
        print(f"Внимание! Дедлайн прошел {abs(d.days)} дней назад")
    else:
        print(f"До дедлайна осталось {d.days} дней")


def today_without_time():
    # данная функция возвращает нам дату сегодняшнего дня без учета времени
    now = datetime.today().strftime("%d-%m-%Y")  # узнаем сегодняшнюю дату
    now = datetime.strptime(now, "%d-%m-%Y")
    return now


# создаем словарь и заполняем его данными
note = {"username": input("Введите имя пользователя: "), "content": input("Введите описание заметки "),
        "status": "Создана", "created_date": datetime.today().strftime("%d-%m-%Y"),
        "issue_date": check_valid_date("Введите дедлайн в формате день-месяц-год "), "titles": []}

# считываем заголовки
add_titles()

# выводим данные
output_note()

# проверяем дедлайн
check_deadline(note["issue_date"])
