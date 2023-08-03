# Generated by Django 4.1 on 2023-08-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.CharField(default='作业指导', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='request',
            name='field',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='request',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='requestfollows',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
