from django.db import models

# Create your models here.

from django.db import models

class StaffBase(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"Manager: {self.full_name}"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='interns')
    internship_end = models.DateField()

    def __str__(self):
        return f"Intern: {self.full_name}"
