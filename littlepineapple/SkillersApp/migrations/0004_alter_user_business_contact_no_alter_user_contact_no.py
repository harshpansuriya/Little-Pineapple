# Generated by Django 4.1.5 on 2023-01-17 13:43

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillersApp', '0003_alter_user_business_contact_no_alter_user_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='business_contact_no',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]