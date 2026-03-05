import pytest
from string_utils import StringUtils

utils = StringUtils()


"""capitalize"""


def test_capitalize_positive_1():
    """Позитив: обычное слово"""
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_positive_2():
    """Позитив: слово с цифрами"""
    assert utils.capitalize("123abc") == "123abc"


def test_capitalize_positive_3():
    """Позитив: строка с пробелами"""
    assert utils.capitalize("skypro 2024") == "Skypro 2024"


def test_capitalize_negative_1():
    """Негатив: пустая строка"""
    assert utils.capitalize("") == ""


def test_capitalize_negative_2():
    """Негатив: строка из пробелов"""
    assert utils.capitalize("   ") == "   "


def test_capitalize_negative_3():
    """Негатив: спецсимволы"""
    assert utils.capitalize("@#$%") == "@#$%"


def test_capitalize_none():
    """Негатив: None вместо строки"""
    with pytest.raises(AttributeError):
        utils.capitalize(None)


"""trim"""


def test_trim_positive_1():
    """Позитив: пробелы в начале"""
    assert utils.trim("   skypro") == "skypro"


def test_trim_positive_2():
    """Позитив: пробелы в начале и конце"""
    assert utils.trim("   skypro  ") == "skypro  "


def test_trim_positive_3():
    """Позитив: один пробел в начале"""
    assert utils.trim(" skypro") == "skypro"


def test_trim_negative_1():
    """Негатив: строка без пробелов"""
    assert utils.trim("skypro") == "skypro"


def test_trim_negative_2():
    """Негатив: пустая строка"""
    assert utils.trim("") == ""


def test_trim_negative_3():
    """Негатив: строка из пробелов"""
    assert utils.trim("   ") == ""


def test_trim_single_space():
    """Негатив: строка с одним пробелом"""
    assert utils.trim(" ") == ""


def test_trim_none():
    """Негатив: None вместо строки"""
    with pytest.raises(AttributeError):
        utils.trim(None)


"""contains"""


def test_contains_positive_1():
    """Позитив: символ есть в строке"""
    assert utils.contains("SkyPro", "S") is True


def test_contains_positive_2():
    """Позитив: число в строке"""
    assert utils.contains("SkyPro123", "1") is True


def test_contains_positive_3():
    """Позитив: подстрока"""
    assert utils.contains("SkyPro", "Pro") is True


# Негативные тесты
def test_contains_negative_1():
    """Негатив: символа нет в строке"""
    assert utils.contains("SkyPro", "U") is False


def test_contains_negative_2():
    """Негатив: пустая строка"""
    assert utils.contains("", "S") is False


def test_contains_negative_3():
    """Негатив: пустой символ"""
    assert utils.contains("SkyPro", "") is True


def test_contains_none_string():
    """Негатив: None вместо строки"""
    with pytest.raises(AttributeError):
        utils.contains(None, "S")


def test_contains_none_symbol():
    """Негатив: None вместо символа"""
    with pytest.raises(TypeError):
        utils.contains("SkyPro", None)


"""delete_symbol"""


def test_delete_symbol_positive_1():
    """Позитив: удалить один символ"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_positive_2():
    """Позитив: удалить подстроку"""
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_positive_3():
    """Позитив: удалить все вхождения"""
    assert utils.delete_symbol("SkyPro SkyPro", "Sky") == "Pro Pro"


# Негативные тесты
def test_delete_symbol_negative_1():
    """Негатив: удалить несуществующий символ"""
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_negative_2():
    """Негатив: пустая строка"""
    assert utils.delete_symbol("", "S") == ""


def test_delete_symbol_negative_3():
    """Негатив: удалить пустой символ"""
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"


def test_delete_symbol_none_string():
    """Негатив: None вместо строки"""
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "S")


def test_delete_symbol_none_symbol():
    """Негатив: None вместо символа"""
    with pytest.raises(TypeError):
        utils.delete_symbol("SkyPro", None)
