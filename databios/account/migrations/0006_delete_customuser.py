# Generated by Django 4.2.2 on 2023-08-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
