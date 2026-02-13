from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(name_number: str) -> str:
    if "счет" in name_number.lower():
        return f"Счет {get_mask_account(name_number)}"
    else:
        return f"{name_number[:-16]} {get_mask_card_number(name_number[-16:])}"

def get_date(date: str) -> str:
    return date[8:10] + "." + date[5:7] + "." + date[:4]