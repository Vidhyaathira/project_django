# Generated by Django 5.1.2 on 2025-02-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courses_name', models.TextField()),
                ('parent_id', models.IntegerField()),
                ('details_name', models.TextField(null=True)),
                ('duration', models.TextField(default='4 months course + 3 months on the Job Training', null=True)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
