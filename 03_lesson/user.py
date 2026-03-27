class User:

    def __init__(self, first_name, last_name):
        """
        Конструктор класса User
        Принимает имя и фамилию
        """
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """Печатает имя"""
        print(self.first_name)

    def print_last_name(self):
        """Печатает фамилию"""
        print(self.last_name)

    def print_full_name(self):
        """Печатает имя и фамилию"""
        print(f"{self.first_name} {self.last_name}")
