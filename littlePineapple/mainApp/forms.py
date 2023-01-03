from django.form import ModelForm
from .models import Skillers


class SkillersForm(ModelForm):
    class Meta:
        Model = Skillers
        field = "__all__"
