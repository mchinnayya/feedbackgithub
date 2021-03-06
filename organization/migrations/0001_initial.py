# Generated by Django 2.2.8 on 2020-07-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=191)),
                ('created_by', models.CharField(max_length=191)),
                ('city', models.CharField(max_length=191)),
                ('state', models.CharField(max_length=191)),
                ('country', models.CharField(max_length=191)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
