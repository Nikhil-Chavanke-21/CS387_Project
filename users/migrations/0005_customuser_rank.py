# Generated by Django 3.0.3 on 2020-03-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200302_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rank',
            field=models.CharField(default='S', max_length=1),
        ),
    ]
