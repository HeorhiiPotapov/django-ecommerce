# Generated by Django 3.0.6 on 2020-06-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200526_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('White', 'Белый'), ('Black', 'Черный'), ('Blue', 'Синий'), ('Green', 'Зеленый'), ('Red', 'Красный'), ('Yellow', 'Желтый'), ('Orange', 'Оранжевый'), ('Violet', 'Фиолетовый'), ('Brown', 'Коричневый'), ('Grey', 'Серый')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sex_type',
            field=models.CharField(choices=[('Male', 'Мужской'), ('Female', 'Женский')], max_length=10),
        ),
    ]