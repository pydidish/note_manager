from datetime import datetime

created_date = "13-12-2024"  # дата создания заметки в формате "день-месяц-год"
issue_date = "31-12-2024"  # дата истечения заметки (дедлайн) в формате "день-месяц-год"

temp_created_data = datetime.strptime(created_date, "%d-%m-%Y")
temp_issue_data = datetime.strptime(issue_date, "%d-%m-%Y")

print("Дата создания:", temp_created_data.strftime("%d-%m"))
print("Дедлайн:", temp_issue_data.strftime("%d-%m"))
