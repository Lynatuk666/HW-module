import datetime
class emloyee:
    def __init__(self,name, job_title):
        self.name = name
        self.job_title = job_title
        self.hire_date = datetime.date.today()

    def get_employees(self):
        delta = datetime.date.today() - self.hire_date
        print(f"{self.name} нанят {delta.days} дней назад, на должность {self.job_title}")



if __name__ == "__main__":
    print("вывод из модуля people.py")
    Petya = emloyee("Петя", "Менеджер")
    Petya.hire_date = datetime.date(2021, 10, 30)
    Petya.get_employees()
