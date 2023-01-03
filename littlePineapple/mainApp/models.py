from django.db import models


class Skillers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    special_skill = models.CharField(max_length=100)
    skill_decs = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name
