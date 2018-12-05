"""
Алгоритм вычисления равных групп сотрудников по фамилиям
"""

from . models import Employee

"""
Получаем список словарей, где каждый ключ - это буква алфавита, 
а значение - количество фамилий сотрудников на эту букву
"""
def get_alpha_list():
    employee_list = list(Employee.objects.all().values('last_name'))
    if employee_list:
        alpha_list  = []
        letter = employee_list[0]['last_name'][0]
        number = 0
        employee_list = list(Employee.objects.all().values('last_name'))
        for i in range(len(employee_list)):
            if i+1 == len(employee_list):
                """
                Обработка последней буквы
                """
                if letter != employee_list[i]['last_name'][0]:
                    alpha_list.append({letter: number})
                    letter = employee_list[i]['last_name'][0]
                    alpha_list.append({letter: 1})
                else:
                    alpha_list.append({letter: number+1})
            elif letter != employee_list[i]['last_name'][0]:
                alpha_list.append({letter: number})
                """
                Когда первая буква в фамилии меняется, обновляем счетчик number 
                и в letter записываем новую букву для счета
                """
                letter = employee_list[i]['last_name'][0]
                number = 0
            number += 1
        return alpha_list
    return None

"""
Получаем среднее значение количества фамилий в группе для равного распределения
"""
def get_number_list():
    # Cписок из количества фамилий на каждую букву
    number_list = [[value for value in letter.values()][0] for letter in get_alpha_list()]
    # Число выводимых групп фамилий
    nav_number = 7 if len(number_list) > 6 else len(number_list) + 1
    # Максимальное число фамилий, начинающихся на одну букву
    max_number = max(number_list)
    # Среднее значение фамилий в группе
    avg_number = int(sum(number_list)/nav_number)

    # Если есть группа фамилий с количеством, превышающим среднее значение,
    # уменьшаем nav_number на 1, чтобы уравнять группы
    while avg_number <= max_number and nav_number > 2:
        nav_number = nav_number - 1
        avg_number = int(sum(number_list)/nav_number)

    return avg_number

"""
Получаем равные группы по фамилиям сотрудников
"""
def current_alpha():

    current_alpha = []
    alpha_list = get_alpha_list()
    if alpha_list:
        avg_number = get_number_list()
        number = [i for i in alpha_list[0].values()][0] # Количество фамилий на букву (начальное значение)
        letters = '' # Буква алфавита

        for i in range(len(alpha_list)):
            letters += [j for j in alpha_list[i].keys()][0]
            if number == 0:
                number = [z for z in alpha_list[i].values()][0]
            """
            Сравниваем количество фамилий в группе со средним значением, а потом 
            сравниваем количества фамилий если добавить или не добавлять следующую букву
            """
            if number < avg_number:
                if i+1 < len(alpha_list):
                    # Определяем, добавить ли последнюю букву к последней группе или оставить ее отдельно
                    if i+2 == len(alpha_list):
                        if (number + [z for z in alpha_list[i+1].values()][0] - avg_number > avg_number - 
                           [z for z in alpha_list[i+1].values()][0]):
                            current_alpha.append(letters)
                            letters = ''
                            number = 0
                        else:
                            letters += '-'
                            number = number + [z for z in alpha_list[i+1].values()][0]
                    elif avg_number - number < number + [z for z in alpha_list[i+1].values()][0] - avg_number:
                        current_alpha.append(letters)
                        letters = ''
                        number = 0
                    else:
                        letters += '-'
                        number = number + [z for z in alpha_list[i+1].values()][0]
                else:
                    current_alpha.append(letters)
                    letters = ''
                    number = 0
            else:
                current_alpha.append(letters)
                letters = ''
                number = 0
        return current_alpha
    return []