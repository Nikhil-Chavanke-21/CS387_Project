# Generated by Django 3.0.3 on 2020-03-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rank',
            field=models.CharField(default='Silver', max_length=10),
        ),
    ]
