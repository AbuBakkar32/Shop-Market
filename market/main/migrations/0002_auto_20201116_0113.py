# Generated by Django 3.1.2 on 2020-11-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
