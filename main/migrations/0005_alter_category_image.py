# Generated by Django 4.2.4 on 2023-08-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_productattributes_productattribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(max_length=300, upload_to='cat_imgs/'),
        ),
    ]
