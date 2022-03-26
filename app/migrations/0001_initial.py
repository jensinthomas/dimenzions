# Generated by Django 3.2.10 on 2022-03-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_register',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('joining_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
