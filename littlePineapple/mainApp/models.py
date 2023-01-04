from django.db import models


class Skillers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    special_skill = models.CharField(max_length=100)
    skill_decs = models.CharField(max_length=1000)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
