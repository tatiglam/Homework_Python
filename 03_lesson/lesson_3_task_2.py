# Импортируем класс Smartphone
from smartphone import Smartphone

# Создаем пустой список для каталога
catalog = []

# Наполняем список пятью экземплярами класса Smartphone
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79161234567"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79269876543"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79351112233"))
catalog.append(Smartphone("Google", "Pixel 8", "+79504445566"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79777778899"))

# Печатаем каталог в заданном формате
print("Каталог смартфонов:")
print("-" * 30)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
