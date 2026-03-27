def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# Вызываем функцию с любым годом (например, 2024)
year_to_check = 2024
result = is_year_leap(year_to_check)

# Выводим результат в нужном формате
print(f"год {year_to_check}: {result}")
