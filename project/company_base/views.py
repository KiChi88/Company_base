from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Employee, Department
from . alpha_calc import current_alpha


class EmployeesList(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Список всех отделов
        context['departments'] = Department.objects.all()
        # Выбранный отдел
        try:
            context['department_title'] = Department.objects.get(id=self.kwargs['id'])
        except KeyError:
            context['department_title'] = 'Все отделы'
        # Выбранный фильтр по работающим / не работающим сотрудникам
        try:
            context['is_working_title'] = 'Не работает в компании' if self.kwargs['number'] == 0 else 'Работает в компании'
        except KeyError:
            context['is_working_title'] = 'Все сотрудники' 
        return context

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            try:
                # Запрашиваемый список сотрудников по отделам
                return Employee.objects.filter(department_id=self.kwargs['id'])
            except KeyError:
                # Списки работающих / не работающих сотрудников
                return Employee.objects.exclude(data_end=None) if self.kwargs['number'] == 0 else Employee.objects.filter(data_end=None)          
        # Если никаких параметров нет, возращаем весь список
        return Employee.objects.all()


class EmployeesAlphaList(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'alpha.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Список всех групп фамилий отредактированный от начальной до конечной в группе
        context['groups'] = [str.split('-')[0] + '-' + str.split('-')[len(str.split('-'))-1] if len(str.split('-')) > 1          
                            else str for str in current_alpha()]
        # Визуализация выбранной группы фамилий
        if self.kwargs:
            context['active_group'] = self.kwargs['group']
        else:
            # Первая группа фамилий по умолчанию
            context['active_group'] = context['groups'][0] if context['groups'] else ''
        return context

    def get_queryset(self, *args, **kwargs):
        if current_alpha():
            # Список групп фамилий и букв, в них входящих
            current_alpha_list = current_alpha()
            # Выбранная группа фамилий (начальное значение = первая группа)
            current_group = current_alpha()[0]
            # Получаем все буквы в выбранной группе фамилий
            if self.kwargs:
                for group in current_alpha_list:
                    if group[0] == self.kwargs['group'][0]:
                        current_group = group
                query = Employee.objects.filter(last_name__startswith=current_group.split('-')[0])
            else:
                # Выводим первую группу фамилий по умолчанию
                query = Employee.objects.filter(last_name__startswith=current_group.split('-')[0])
            # В query находится queryset фамилий на первую букву группы. Добавляем остальные.
            for letter in current_group.split('-')[1:]:
                query |= Employee.objects.filter(last_name__startswith=letter)
            return query
        return Employee.objects.none()

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee.html'