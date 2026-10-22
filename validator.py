# validator.py
def validate_email(email: str) -> bool:
    """Р’Р°Р»РёРґР°С†РёСЏ email-Р°РґСЂРµСЃР°."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Р’Р°Р»РёРґР°С†РёСЏ СЂРѕСЃСЃРёР№СЃРєРёС… РЅРѕРјРµСЂРѕРІ С‚РµР»РµС„РѕРЅРѕРІ."""
    import re
    pattern = r'^(\+7|8)[\s\-]?\(?[0-9]{3}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    return bool(re.match(pattern, phone))
