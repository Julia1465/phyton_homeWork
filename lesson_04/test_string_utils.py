from string_utils import StringUtils

utils = StringUtils()

# --- Позитивные тесты ---


def test_capitalize_normal():
    """Позитивный: обычная строка, первая буква становится заглавной."""
    assert utils.capitalize("hello world") == "Hello world"


def test_trim_spaces_at_start():
    """Позитивный: удаление пробелов в начале."""
    assert utils.trim("   skypro") == "skypro"


def test_contains_true():
    """Позитивный: символ найден в строке."""
    assert utils.contains("SkyPro", "S") is True


# --- Негативные тесты и тесты на граничные случаи ---
def test_trim_no_spaces():
    """Негативный: в строке нет пробелов в начале, она не должна измениться."""
    assert utils.trim("skypro") == "skypro"


def test_contains_false():
    """Негативный: символ не найден, должен вернуть False."""
    assert utils.contains("SkyPro", "U") is False


# ---Тесты на дефекты ---
def test_trim_multiple_spaces():
    """Проверка на удаление нескольких пробелов подряд."""
    # В оригинальном коде цикл while мог работать некорректно или медленно.
    # lstrip справляется идеально.
    assert utils.trim("    skypro") == "skypro"


def test_delete_symbol_multiple_occurrences():
    """Удаление всех вхождений символа."""
    assert utils.delete_symbol("banana", "a") == "bnn"


def test_delete_symbol_substring():
    """Удаление подстроки, а не одного символа."""
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_contains_empty_symbol():
    """Пограничный случай: поиск пустой строки."""
# (В Python "abc".index("") возвращает 0. Contains должен вернуть True.)
    assert utils.contains("abc", "") is True
