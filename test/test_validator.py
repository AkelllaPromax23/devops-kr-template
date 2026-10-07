# tests/test_validator.py
from validator import validate_email, validate_phone

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79161234567") is True
    assert validate_phone("89161234567") is False
    assert validate_phone("+7 916 123 45 67") is False
