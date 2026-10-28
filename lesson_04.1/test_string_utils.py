import pytest
from string_utils import StringUtils

utils = StringUtils()

# --- 1. CAPITALIZE ---


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),            # Позитивный: нижний регистр
    ("Skypro", "Skypro"),            # Позитивный: уже с заглавной
    ("", ""),                        # Негативный: пустая строка
    ("123", "123")                   # Негативный: строка из цифр
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected


# --- 2. TRIM (Удаление пробелов в начале) ---
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),          # Позитивный: пробелы в начале
    ("  hello world", "hello world"),  # Позитивный: пробелы и несколько слов
    ("", ""),                         # Негативный: пустая строка
    ("   ", "")                       # Негативный: только пробелы
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


# --- 3. CONTAINS (Поиск символа) ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),           # Позитивный: символ есть
    ("SkyPro", "P", True),           # Позитивный: символ в середине
    ("SkyPro", "U", False),          # Негативный: символа нет
    ("", "S", False)                 # Негативный: поиск в пустой строке
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# --- 4. DELETE_SYMBOL (Удаление подстроки) ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # Позитивный: удаление буквы
    ("SkyPro", "Pro", "Sky"),    # Позитивный: удаление подстроки
    ("SkyPro", "x", "SkyPro"),  # Негативный: символа нет, строка не меняется
    ("", "a", "")              # Негативный: удаление в пустой строке
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
