# Generated by Django 5.1.2 on 2025-02-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='details_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='duration',
            field=models.TextField(blank=True, default='4 months course + 3 months on the Job Training', null=True),
        ),
    ]
