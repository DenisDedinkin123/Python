from Adress import Address
from Mailing import Mailing

to_addr = Address("123456", "Москва", "Тверская", "10", "5")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "12")
mailing = Mailing(to_addr, from_addr, 350.0, "TRACK12345")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
        f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
        f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
        f"{mailing.to_address.house} -{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
