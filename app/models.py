from django.db import models


# Create your models here.
class RobotCategory(models.Model):
    robot_category_name = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.robot_category_name}"


class Manufacturer(models.Model):
    robot_category_name = models.ForeignKey(RobotCategory, on_delete=models.CASCADE, related_name='made_in', null=True)
    
    manufacturer = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.manufacturer}"


class Robot(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='robot', null=True)

    robot_id = models.CharField(max_length=100, null=True)
    robot_name = models.CharField(max_length=100, null=True)
    ram = models.CharField(max_length=150, null=True)
    speed = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    manufacturing_date = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.robot_name}"
