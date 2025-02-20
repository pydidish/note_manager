from datetime import datetime


def check_valid_date(text):
    # функция check_valid_date проверяет правильность введенных данных и запрашивает их снова, если данные невалидны
    while True:
        try:
            data = datetime.strptime(input(text), "%d-%m-%Y").strftime("%d-%m-%Y")
            return data
        except ValueError:
            print("Данные некорректны. Введите дату в формате день-месяц-год. Например, 01-01-2025")


username = input("Введите имя пользователя: ")  # имя пользователя
title = input("Введите заголовок заметки ")  # заголовок заметки
content = input("Введите описание заметки ")  # описание заметки
status = "Создана"  # описание заметки при создании автоматически устанавливается в состояние "Создана"
created_date = datetime.today().strftime(
    "%d-%m-%Y")  # дата создания заметки в формате "день-месяц-год" создается автоматически
issue_date = check_valid_date(
    "Введите дедлайн в формате день-месяц-год ")  # дата истечения заметки (дедлайн) в формате "день-месяц-год"

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
