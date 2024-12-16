from datetime import datetime


def check_valid_date(text):
    # функция check_valid_date проверяет правильность введенных данных и запрашивает их снова, если данные невалидны
    while True:
        try:
            data = datetime.strptime(input(text), "%d-%m-%Y").strftime("%d-%m-%Y")
            return data
        except ValueError:
            print("Данные некорректны. Введите дату в формате день-месяц-год. Например, 01-01-2025")


note = []
#узнаем и добавляем в список имя
username = input("Введите имя пользователя: ")
note.append(username)

#запрашиваем и добавляем в список описание заметки
content = input("Введите описание заметки ")  # описание заметки
note.append(content)

#добавляем в список статус заметки
status = "Создана"  # описание заметки при создании автоматически устанавливается в состояние "Создана"
note.append(status)

#добавляем в список дату создания заметки
created_date = datetime.today().strftime(
    "%d-%m-%Y")  # дата создания заметки в формате "день-месяц-год" создается автоматически
note.append(created_date)

#запрашиваем и добавляем в список дедлайн
issue_date = check_valid_date(
    "Введите дедлайн в формате день-месяц-год ")  # дата истечения заметки (дедлайн) в формате "день-месяц-год"
note.append(issue_date)

#запрашиваем и добавляем в список заголовки
titles = []
for i in range(3):
    title = input(f"Введите заголовок {i + 1} заметки ")  # заголовок заметки
    titles.append(title)
note.append(titles)

print("\nВы ввели следующие данные:")
print("Имя пользователя:", note[0])
print("Описание заметки:", note[1])
print("Статус заметки:", note[2])
print("Дата создания заметки:", note[3])
print("Дата истечения заметки:", note[4])
print("Заголовки заметки:", note[5])