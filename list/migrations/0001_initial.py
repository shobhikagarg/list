# Generated by Django 3.1.2 on 2020-10-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('Designation', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=10)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]