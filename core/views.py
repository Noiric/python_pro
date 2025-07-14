from django.http import JsonResponse
from django.db.models import Q
from core.models import Department, Position


def homework_querysets(request):
    departments_with_managers = Department.objects.filter(
        position__name__icontains='менеджер'
    ).order_by('name').distinct()

    active_positions_count = Position.objects.filter(is_active=True).count()

    hr_department = Department.objects.filter(name__iexact='HR').first()
    positions_active_or_hr = Position.objects.filter(
        Q(is_active=True) | Q(department=hr_department)
    )

    department_names_with_managers = Department.objects.filter(
        position__name__icontains='менеджер'
    ).values('name').distinct()

    positions_ordered = Position.objects.order_by('name').values('name', 'is_active')

    result = {
        "departments_with_managers": list(departments_with_managers.values('id', 'name')),
        "active_positions_count": active_positions_count,
        "positions_active_or_hr": list(positions_active_or_hr.values('id', 'name', 'is_active')),
        "department_names_with_managers": list(department_names_with_managers),
        "positions_ordered": list(positions_ordered),
    }

    return JsonResponse(result)
