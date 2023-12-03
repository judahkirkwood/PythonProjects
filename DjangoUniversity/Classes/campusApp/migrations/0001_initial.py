# Generated by Django 4.2.7 on 2023-12-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campus_id', models.IntegerField(blank=True, default='')),
            ],
        ),
    ]
