from django.dispatch import receiver
from django.db.models.signals import post_save
from reflective.users.models import User


@receiver(post_save, sender=User)
def create_employee_for_user(sender, instance, created, **kwargs):
    if not created:
        return
    from reflective.employees.models import Employee
    Employee.objects.create(
        user=instance
    )
