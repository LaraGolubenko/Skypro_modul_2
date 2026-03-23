def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, для фильтрации транзакций по значению state"""
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: list[dict], is_descending: bool = True) -> list[dict]:
    """Функция, для сортировки транзакций по дате"""
    return sorted(data, key=lambda item: item.get("date", ""), reverse=is_descending)
