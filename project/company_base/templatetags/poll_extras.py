from django import template

register = template.Library()

#Создадим два шаблонных тега для равного распределения сотрудников по двум колонкам на последней странице.

def middle_before(value):
    return value[:int(len(value)/2)]

def middle_after(value):
    return value[int(len(value)/2):]

register.filter('middle_before', middle_before)
register.filter('middle_after', middle_after)