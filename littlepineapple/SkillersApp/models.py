from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    contact_no = models.CharField(max_length=12)
    business_email = models.EmailField(blank=True)
    business_contact_no = models.CharField(max_length=12,verbose_name="Contact number")

    def __str__(self):
        return self.username

class Skiller(models.Model):
    userId = models.ForeignKey(User, verbose_name="pk", on_delete=models.CASCADE)

class SkliierPost(models.Model):
    skillerID = models.ForeignKey(Skiller, verbose_name="pk", on_delete=models.CASCADE)
    SkillTitle = models.CharField(verbose_name="Title",max_length=50)
    SkillImage = models.ImageField(verbose_name="Skill Image", upload_to="upload/skillImages",null=True)
    SkillDescription = models.CharField(verbose_name="Description", max_length=1200)
    SkillerWages = models.FloatField(verbose_name="Avg Wages Rate",null=True)
    skillerContact = models.CharField(max_length=12,verbose_name="Contact number",null=True)
    class Meta:
        verbose_name = ("skliierpost")
        verbose_name_plural = ("skliierposts")

    def __str__(self):
        return self.SkillTitle

class ClientModel(models.Model):
    projectStatusLst = {
        (0,"searching"),
        (1,"started"),
        (2,"pending"),
        (3,"completed")
    }
    userId = models.ForeignKey(User, verbose_name="pk", on_delete=models.CASCADE)
    projectStatus = models.PositiveSmallIntegerField(default=0,choices=projectStatusLst)
    projectBudget = models.FloatField(verbose_name="Project Budget",default=0)

    class Meta:
        verbose_name = ("clientmodel")
        verbose_name_plural = ("clientmodels")

class Tags(models.Model):
    tagName = models.CharField(verbose_name="Tag",max_length=20)

    class Meta:
        verbose_name = ("tags")
        verbose_name_plural = ("tagss")

    def __str__(self):
        return self.tagName

class ProjectRequestModel(models.Model):
	projectId = models.AutoField(primary_key=True)
	clientId = models.ForeignKey("ClientModel", verbose_name="Client ID", on_delete=models.CASCADE)
	skillerId = models.ForeignKey("Skiller", verbose_name="Skiller ID", on_delete=models.CASCADE)
	projectDesc = models.CharField(verbose_name="Project desvription", max_length=1200)
	tagModel = models.ForeignKey("Tags", verbose_name="Tags", on_delete=models.CASCADE)
