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


def update_status(status):
    # функция реализует возможность изменения статуса заметки
    dict_status = {'1': 'Создана', '2': 'В работе', '3': 'На паузе', '4': 'Завершена'}
    print("\nВыберите новый статус заметки")
    print('1.Создана\n2.В работе\n3.На паузе\n4.Завершена')
    input_status = input("Новый статус заметки: ")
    input_status = input_status.strip().capitalize()
    while True:
        if input_status in dict_status.keys():  # проверяем введенный номер статуса
            if status != dict_status[input_status]:
                print(f"Статус заметки изменен на '{dict_status[input_status]}'")
                return dict_status[input_status]
            else:
                print(f"Заметка уже в статусе '{status}'")
                return status
        elif input_status in dict_status.values():  # проверяем введенный текстом статус
            if status != input_status:
                print(f"Статус заметки изменен на '{input_status}'")
                return input_status.capitalize()
            else:
                print(f"Заметка уже в статусе '{status}'")
                return status
        else:  # запрашиваем новый ввод при некорректном вводе данных
            print("Некорректный статус заметки")
            print("\nВыберите новый статус заметки")
            print('1.Создана\n2.В работе\n3.На паузе\n4.Завершена')
            input_status = input("Новый статус заметки: ")
            input_status = input_status.strip().capitalize()


def output_note():
    print("\nВы ввели следующие данные:")
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")


# создаем словарь и заполняем его данными
note = {"username": input("Введите имя пользователя: "), "content": input("Введите описание заметки "),
        "status": "Создана", "created_date": datetime.today().strftime("%d-%m-%Y"),
        "issue_date": check_valid_date("Введите дедлайн в формате день-месяц-год "), "titles": []}
add_titles()  # добавляем заголовки
output_note()  # выводим введенные данные
note["status"] = update_status(note["status"])  # меняем статус заметки
output_note()  # выводим обновленные данные
