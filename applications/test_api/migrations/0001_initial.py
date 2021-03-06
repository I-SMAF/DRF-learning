# Generated by Django 4.0.6 on 2022-07-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='сюда имя писать надо, максимум 64 символа', max_length=64, verbose_name='имя')),
                ('last_name', models.CharField(help_text='сюда фамилию писать надо, максимум 64 символа', max_length=64, verbose_name='фамилия')),
            ],
            options={
                'verbose_name': 'человек',
                'verbose_name_plural': 'люди',
                'ordering': ['id'],
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
