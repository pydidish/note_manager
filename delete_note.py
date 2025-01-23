from datetime import datetime
from nanoid import generate


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


def output_note(list_of_notes):
    # функция для вывода списка заметок
    for i in range(len(list_of_notes)):
        print(f"\n{i + 1} заметка:\n")
        n = list_of_notes[i]
        for key, value in n.items():
            print(f"{key.capitalize()}: {value}")


def add_titles(n):
    # функция add_titles реализует ввод и проверку на уникальность введенных заголовков
    # получение первого заголовка заметки
    title = input("Введите заголовок заметки: ")
    while title.strip() == "":
        title = input("Необходимо ввести хотя бы один заголовок. Введите заголовок заметки: ")
    while title.strip() != "":
        # проводим проверку на уникальность заголовка и добляем в список в случае успешного прохождения проверки
        if title.strip().capitalize() not in n["titles"]:
            n["titles"].append(title.strip().capitalize())
        title = input(
            "Введите следующий заголовок заметки или оставьте поле пустым для завершения ввода: ")  # заголовок заметки


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


def create_content():
    # считываем описание заметки и проверяем её на пустоту
    content = input("Введите описание заметки: ")
    while content.strip() == '':
        content = input("Это поле нельзя оставить пустым. Введите описание заметки: ")
    return content


def create_id(l_n):
    # генерируем и проверяем уникальность id
    while True:
        new_id = generate()
        for i in range(len(l_n)):
            n = l_n[i]
            if new_id == n["id"]:
                break
        break
    return new_id


def create_note(l_n):
    # создаем словарь и заполняем его данными
    c_n = {"username": input("Введите имя пользователя: "), "content": create_content(), "id": create_id(l_n),
           "status": "Создана", "created_date": datetime.today().strftime("%d-%m-%Y"),
           "issue_date": check_valid_date("Введите дедлайн в формате день-месяц-год: "), "titles": []}
    # считываем заголовки
    add_titles(c_n)
    return c_n


def create_list_notes():
    # создаем список для хранения заметок и заполяем его
    list_notes = []
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    flag = 'да'
    while flag.lower() != 'нет':
        if flag.lower() == 'да':
            note = create_note(list_notes)
            list_notes.append(note)
            flag = input('\nХотите добавить ещё одну заметку? (да/нет): ')
        else:
            flag = input('Некорректный ввод! Хотите добавить ещё одну заметку? (да/нет): ')
    return list_notes


def delete_notes(list_notes, gr):
    if len(list_notes) == 0:
        print("\nСписок заметок пуст")
    else:
        f = 0
        list_notes2 = list_notes.copy()
        for i in range(len(list_notes2)):
            n = list_notes2[i]
            if gr.lower() == n["username"].lower() or gr.strip().capitalize() in n["titles"]:
                print("\nВы уверены, что хотите удалить следующую заметку?\n")
                for key, value in n.items():
                    print(f"{key.capitalize()}: {value}")
                fl = input("\nДа или нет? ")
                while fl.lower() != 'нет' and fl.lower() != 'да':
                    fl = input('Некорректный ввод! Уверены, что хотите удалить эту заметку? (да/нет): ')
                if fl.lower() == 'да':
                    list_notes.pop(i-f)
                    f += 1
                    print("\nЗаметка успешно удалена")
                elif fl.lower() == 'нет':
                    print("\nУдаление заметки отменено")
        if f == 0:
            print("\nЗаметок с таким именем пользователя или заголовком не найдено.")
        else:
            if len(list_notes) != 0:
                print("\nОстались следующие заметки:")
                output_note(list_notes)
            else:
                print("\nЗаметок в списке не осталось")


notes = create_list_notes()
print('\nТекущие заметки:')
output_note(notes)
ground = input('\nВведите имя пользователя или заголовок для удаления заметки: ')
delete_notes(notes, ground)
