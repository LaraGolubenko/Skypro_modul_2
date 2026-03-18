def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, для фильтрации по state"""
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, для сортировки по дате"""
    return sorted(data, key=lambda item: item.get("date"), reverse=reverse)
