from smartphone import Smartphone

catalog = [
    Smartphone("Sony", "Xperia xz1 compact", "+79855322351"),
    Smartphone("Samsung", "Galaxy Z Flip7", "79855822351"),
    Smartphone("Xiaomi", "Redmi Note 14 Pro", "79555822351"),
    Smartphone("Nokia", "Nokia G22", "79155822351"),
    Smartphone("Apple", "iPhone 16e", "79105822351")
]

for smartphone in catalog:
    print(f"{smartphone.car_brand}, {smartphone.car_model}, {smartphone.subscriber_number}")