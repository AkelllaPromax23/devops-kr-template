def test_validate_phone():
    assert validate_phone("+79991234567") == True
    assert validate_phone("89991234567") == False
    assert validate_phone("+7999123") == False
    
def validate_inn(inn: str) -> bool:
    """TODO: валидация ИНН."""
    pass