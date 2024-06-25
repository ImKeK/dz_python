import sys
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = self.validate_age(age)

    def validate_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError("Неверный возраст")
        return age

    def birthday(self):
        self.age += 1

class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, employee_id):
        super().__init__(last_name, first_name, middle_name, age)
        self.employee_id = self.validate_id(employee_id)

    def validate_id(self, employee_id):
        if not isinstance(employee_id, int) or employee_id < 100000 or employee_id > 999999:
            raise InvalidIdError("Неверный ID")
        return employee_id

    def get_level(self):
        return self.employee_id % 7

def main():
    try:
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        age = int(input("Введите возраст: "))

        person = Person(last_name, first_name, middle_name, age)
        print("Данные о человеке:")
        print(f"Фамилия: {person.last_name}")
        print(f"Имя: {person.first_name}")
        print(f"Отчество: {person.middle_name}")
        print(f"Возраст: {person.age}")

        person.birthday()
        print(f"После дня рождения возраст стал: {person.age}")

        employee_id = int(input("Введите ID сотрудника: "))
        employee = Employee(last_name, first_name, middle_name, age, employee_id)
        print("Данные о сотруднике:")
        print(f"Фамилия: {employee.last_name}")
        print(f"Имя: {employee.first_name}")
        print(f"Отчество: {employee.middle_name}")
        print(f"Возраст: {employee.age}")
        print(f"ID сотрудника: {employee.employee_id}")
        print(f"Уровень сотрудника: {employee.get_level()}")

    except (InvalidNameError, InvalidAgeError, InvalidIdError) as e:
        logging.error(str(e))
        print("Произошла ошибка. Пожалуйста, проверьте введенные данные.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Запуск из командной строки с передачей параметров
        try:
            last_name = sys.argv[1]
            first_name = sys.argv[2]
            middle_name = sys.argv[3]
            age = int(sys.argv[4])
            employee_id = int(sys.argv[5])

            person = Person(last_name, first_name, middle_name, age)
            print("Данные о человеке:")
            print(f"Фамилия: {person.last_name}")
            print(f"Имя: {person.first_name}")
            print(f"Отчество: {person.middle_name}")
            print(f"Возраст: {person.age}")

            person.birthday()
            print(f"После дня рождения возраст стал: {person.age}")

            employee = Employee(last_name, first_name, middle_name, age, employee_id)
            print("Данные о сотруднике:")
            print(f"Фамилия: {employee.last_name}")
            print(f"Имя: {employee.first_name}")
            print(f"Отчество: {employee.middle_name}")
            print(f"Возраст: {employee.age}")
            print(f"ID сотрудника: {employee.employee_id}")
            print(f"Уровень сотрудника: {employee.get_level()}")

        except (InvalidNameError, InvalidAgeError, InvalidIdError) as e:
            logging.error(str(e))
            print("Произошла ошибка. Пожалуйста, проверьте переданные параметры.")
    else:
        # Запуск в интерактивном режиме
        main()
