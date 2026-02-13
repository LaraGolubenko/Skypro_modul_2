from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_number: str) -> str:
    """Функция принимающая имя и номер и маскирует"""
    if "счет" in name_number.lower():
        return f"Счет {get_mask_account(name_number)}"
    else:
        return f"{name_number[:-16]} {get_mask_card_number(name_number[-16:])}"


def get_date(date: str) -> str:
    """Функция форматирует дату из строки в формат ДД.ММ.ГГГГ"""
    return date[8:10] + "." + date[5:7] + "." + date[:4]
