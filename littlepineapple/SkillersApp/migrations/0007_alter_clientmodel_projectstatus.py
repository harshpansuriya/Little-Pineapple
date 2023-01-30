# Generated by Django 4.1.5 on 2023-01-29 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillersApp', '0006_alter_clientmodel_projectstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='projectStatus',
            field=models.PositiveSmallIntegerField(choices=[(1, 'started'), (0, 'searching'), (2, 'pending'), (3, 'completed')], default=0),
        ),
    ]