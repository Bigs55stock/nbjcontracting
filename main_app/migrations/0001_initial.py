# Generated by Django 4.1.7 on 2023-03-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('Inquiries', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
