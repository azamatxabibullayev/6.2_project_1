# Generated by Django 5.0.4 on 2024-05-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'Motobikes',
            },
        ),
    ]