# Generated by Django 4.0 on 2023-02-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LetsQuiz_Api', '0010_joinquiz_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizequiz',
            name='quiz_id',
            field=models.IntegerField(unique=True),
        ),
    ]
