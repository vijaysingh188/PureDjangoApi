# Generated by Django 2.1.5 on 2020-03-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=264)),
                ('esal', models.FloatField()),
                ('eadd', models.CharField(max_length=264)),
            ],
        ),
    ]