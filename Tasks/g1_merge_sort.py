from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    """
    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния
    4. Берем два отсортированных массива сравниваем первые элементы из каждого массива и в итоговый 
    массив записываем наименьшее в массиве, в котором был наименьший элемент, переходим к следующему 
    когда один из массивов закончится, остаток второго «сливаем» в итоговый массив 
    """

    if len(container) == 1:
        return container
    else:
        mid = len(container) // 2
        left_part = sort(container[:mid])
        right_part = sort(container[mid:])

        new_list = []

        while len(left_part) > 0 and len(right_part) > 0:
            if left_part[0] < right_part[0]:
                new_list.append(left_part.pop(0))
            else:
                new_list.append(right_part.pop(0))
        if left_part:
            new_list += left_part
        else:
            new_list += right_part

        return new_list
