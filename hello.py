from datetime import datetime

name = input("Как тебя зовут? ")
now = datetime.now()
print(f"Привет, {name}! Сегодня {now.strftime('%d.%m.%Y')}, а ты уже кодишь на Python")
