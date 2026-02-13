from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

if __name__ == "__main__":
#    print(get_mask_card_number(1234567890123456))
#    print(get_mask_account(73654108430135874305))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(get_date("2024-03-11T02:26:18.671407"))
