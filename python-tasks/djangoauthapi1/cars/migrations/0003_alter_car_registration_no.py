# Generated by Django 3.2 on 2022-06-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='registration_no',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]