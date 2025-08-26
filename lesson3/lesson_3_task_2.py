from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'S30', '+79251234567'),
    Smartphone('Nokia', 'N50', '+73256548795'),
    Smartphone('Poco', 'F6', '+79269876543'),
    Smartphone('Xiaomi', 'RedMi', '+79249876542'),
    Smartphone('iphon', '13', '+79326543214')
    ]

for smartphone in catalog:
    print(f"{smartphone.name_phone}-{smartphone.model_phone}.{smartphone.number_phone}")
