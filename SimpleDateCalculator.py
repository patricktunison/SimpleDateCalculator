import datetime

user_date_number = int(input('Enter number of days: '))
current_date = datetime.date.today()

date_addition = current_date + datetime.timedelta(days=user_date_number)
format_date = date_addition.strftime("%m/%d/%Y")

print(f'{user_date_number} days from now is {format_date}.')