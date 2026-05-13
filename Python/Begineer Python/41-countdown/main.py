import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(today.year, 12, 25)

date_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)

else:
    print(f"Your birthday is in {date_away.days} days!")