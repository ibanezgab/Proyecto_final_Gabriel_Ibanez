# Generated by Django 4.1.7 on 2023-04-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('localidad', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=254)),
                ('cel', models.IntegerField()),
            ],
        ),
    ]
