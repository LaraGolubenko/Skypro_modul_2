def get_mask_card_number(number: int | str) -> str:
    """Преобразует номер банковской карты в формат XXXX XX** **** XXXX"""
    mask_card_1 = ""
    mask_card_2 = []
    conv_str = str(number)
    for i in range(len(conv_str)):
        if 5 < i < 12:
            mask_card_1 += "*"
        else:
            mask_card_1 += conv_str[i]
    for i in range(0, len(mask_card_1), 4):
        mask_card_2.append(mask_card_1[i : i + 4])
    return " ".join(mask_card_2)


def get_mask_account(number: int | str) -> str:
    """Преобразует номер банковского счета в формат **XXXX"""
    conv_str = str(number)
    mask_account = "**" + conv_str[-4:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(73654108430135874305))
