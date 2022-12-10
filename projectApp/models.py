from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Departments(models.Model):
    deprtName = models.CharField(max_length=100)

    def __str__(self):
        return self.deprtName

    class Meta:
        verbose_name_plural = "Departments Detail"

#employee Class
class EmployeeDetails(models.Model):
    userProfile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="EmpDetails", null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    doj = models.DateField()
    isProjectManager = models.BooleanField(default=False)
    departmentName = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name="employeeDT")

    def __str__(self):
        return self.name or "--Name Not Provided--"

    class Meta:
        verbose_name_plural = "Employees Detail"

#project class
class ProjectDetails(models.Model):
    projectName = models.CharField(max_length=1000)
    projectStartDate = models.DateField()
    projectEndDate = models.DateField()
    projectManager = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE, related_name="projectDTP", null=True, blank=True)
    employeeName = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE, related_name="projectDT", null=True, blank=True)

    def __str__(self):
        return self.projectName or "--Name Not Provided--"

    class Meta:
        verbose_name_plural = "Project Details"
