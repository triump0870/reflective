from django.db import models
from django_extensions.db.fields import AutoSlugField
from reflective.users.models import User


# Create your models here.
# class EmployeeObjectManager(models.Manager):
#     def average_by_dept(self, dept):
#         avg_salary = self.objects.filter(department_id=dept).aggregate(models.Avg('salary'))
#         print("avg: ", avg_salary)
#         return avg_salary

class EffectiveDate(models.Model):
    effective_date = models.DateField()

    def __str__(self):
        return str(self.effective_date)


class Department(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True, unique=True, db_index=True)
    salary = models.PositiveIntegerField()
    effective_date = models.ManyToManyField(EffectiveDate)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)

    # object = EmployeeObjectManager()

    def __str__(self):
        return "#%s-%s" % (str(self.employee_id), self.user)
