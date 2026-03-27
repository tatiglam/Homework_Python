# Импортируем класс User из файла user.py
from user import User

# Создаем новый экземпляр User
my_user = User("Иван", "Петров")

# Вызываем все методы
print("Имя:")
my_user.print_first_name()

print("Фамилия:")
my_user.print_last_name()

print("Полное имя:")
my_user.print_full_name()
