# Generated by Django 4.1.5 on 2023-01-29 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillersApp', '0007_alter_clientmodel_projectstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='projectStatus',
            field=models.PositiveSmallIntegerField(choices=[(3, 'completed'), (2, 'pending'), (0, 'searching'), (1, 'started')], default=0),
        ),
    ]
