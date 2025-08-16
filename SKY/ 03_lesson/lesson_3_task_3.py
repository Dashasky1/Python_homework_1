from address import Address
from mailing import Mailing


to_address = Address("692184", "село Дальний Кут", "улица Победы", 1, "-")
from_address = Address("692001",  "село Красный Яр", "улица Арсеньева",
                       "9а", "-")

my_mailing = Mailing(to_address, from_address, 128, "ТРК1235544")

print(my_mailing)
