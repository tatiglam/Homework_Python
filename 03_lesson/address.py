class Address:
    """
    Класс для хранения почтового адреса
    """

    def __init__(self, index, city, street, house, apartment):
        """
        Конструктор класса Address
        Принимает индекс, город, улицу, дом, квартиру
        """
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
