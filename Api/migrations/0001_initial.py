# Generated by Django 5.0.4 on 2024-04-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('department', models.CharField(max_length=90)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
