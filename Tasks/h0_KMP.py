from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    """
    1. Первый элемент префикс таблицы равен 0
    2. Пока не будет достигнута граница шаблона вычисляем:
    3. Если текущий символ суффикса равен текущему символу префикса, то в префикс таблицу записывается 
       размер префикса плюс один `pi[i] = j + 1`
    4. Счетчики префикса и суффикса увеличиваем на один
    5. Иначе проверяем равен ли индекс префикса 0. Если да, то увеличиваем счетчик суффикса на один. 
       Иначе переносим счетчик префикса на индекс указанный в префикс-таблице `j = pi[j-1]`
    """
    pi = [0] * len(prefix_str)
    j = 0
    for i in range(1, len(prefix_str)):
        while i < len(prefix_str):
            if prefix_str[j] == prefix_str[i]:
                pi[i] = j + 1
                j += 1
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = pi[j - 1]
        return pi


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    """
    1. Пока не дошли до конца строки
    2. Сравниваем `i-й` элемент строки и `j-й` элемент шаблона
    3. Если они равны - увеличиваем оба счетчика (и проверяем условие выхода)
    4. Если не равны – значит мы нашли несовпадение где-то в середине шаблона, нужно вычислить, 
       с какого символа шаблона нужно продолжать. `j = pi[j-1]`
    """
    prefix_fun = _prefix_fun(substr)
    i = 0
    j = 0

    while i < len(inp_string) and j < len(substr):
        if inp_string[i] == substr[j]:
            i += 1
            j += 1
            if j == len(substr):
                return i - j
        elif j == 0:
            i += 1
        else:
            j = prefix_fun[j - 1]
