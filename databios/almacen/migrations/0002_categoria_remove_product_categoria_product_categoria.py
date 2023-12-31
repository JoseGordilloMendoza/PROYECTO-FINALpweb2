# Generated by Django 4.2.2 on 2023-08-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='categoria',
        ),
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.ManyToManyField(to='almacen.categoria'),
        ),
    ]
