# Generated by Django 4.0.3 on 2022-03-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_irisdata_delete_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irisdata',
            name='petal_length',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='irisdata',
            name='petal_width',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='irisdata',
            name='result',
            field=models.CharField(max_length=121),
        ),
        migrations.AlterField(
            model_name='irisdata',
            name='sepal_length',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='irisdata',
            name='sepal_width',
            field=models.CharField(max_length=10),
        ),
    ]