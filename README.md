# Виджет банковских операций клиента

Проект реализует бэкенд-логику для виджета, который отображает последние успешные банковские операции клиента.

## 📌 Описание

В рамках проекта реализуются функции для:
- фильтрации операций по статусу
- сортировки операций по дате
- маскировки номеров карт и счетов
- форматирования даты

## ⚙️ Функциональность

- `get_mask_card_number()` — маскировка номера карты  
- `get_mask_account()` — маскировка номера счета  
- `mask_account_card()` — объединённая маска карты/счета  
- `get_date()` — форматирование даты  
- `filter_by_state()` — фильтрация операций по статусу  
- `sort_by_date()` — сортировка операций по дате  

## 🚀 Установка

1. Клонировать репозиторий:
git clone git@github.com:LaraGolubenko/Skypro_modul_2.git
2. Перейти в папку проекта:
cd Skypro_modul_2.git
3. Установить зависимости:
pip install -r requirements.txt

## 🧪 Использование

Пример:

```python
from src.processing import filter_by_state, sort_by_date

data = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2022-01-01T10:00:00"}
]

filtered = filter_by_state(data)
sorted_data = sort_by_date(data)


