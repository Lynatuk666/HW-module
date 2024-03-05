from colorama import Fore, Back, Style
import application.db.people as people
from application.salary import calculate_salary
import datetime


if __name__ == '__main__':
    print(f"Сегодня {datetime.date.today()}")
    calculate_salary()
    Vanya = people.emloyee("Ваня", "Продавец")
    Vanya.hire_date = datetime.date(2022, 10, 30)
    Vanya.get_employees()
    print(Fore.RED + 'делаем текст красным')
    print(Back.GREEN + 'и добавляем зеленый фон под текст')
    print(Style.RESET_ALL)#обнуляем изменения
    print('Теперь все как обычно')
