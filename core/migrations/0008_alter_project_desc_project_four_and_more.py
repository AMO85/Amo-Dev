# Generated by Django 4.1 on 2023-03-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desc_project_four',
            field=models.CharField(max_length=500, null=True, verbose_name='descripcion 4'),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc_project_one',
            field=models.CharField(max_length=500, null=True, verbose_name='descripcion 1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc_project_three',
            field=models.CharField(max_length=500, null=True, verbose_name='descripcion 3'),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc_project_two',
            field=models.CharField(max_length=500, null=True, verbose_name='descripcion 2'),
        ),
    ]