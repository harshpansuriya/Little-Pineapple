from django.contrib import admin
from .models import User, Skiller, SkliierPost, ClientModel, Tags, ProjectRequestModel

# Register your models here.
admin.site.register(User)
admin.site.register(Skiller)
admin.site.register(SkliierPost)
admin.site.register(ClientModel)
admin.site.register(Tags)
admin.site.register(ProjectRequestModel)
