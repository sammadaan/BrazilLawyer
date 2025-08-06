"""Input validators for BR legal document formats."""
import re

def is_valid_cnpj(value: str) -> bool:
    return bool(re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", value))

def is_valid_case_number(value: str) -> bool:
    return bool(re.match(r"^\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}$", value))