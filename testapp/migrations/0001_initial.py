# Generated by Django 3.2.8 on 2021-10-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option_a', models.CharField(max_length=100)),
                ('option_b', models.CharField(max_length=100)),
                ('option_c', models.CharField(max_length=100)),
                ('option_d', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]