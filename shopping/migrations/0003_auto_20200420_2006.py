# Generated by Django 2.0.6 on 2020-04-20 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20200420_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='产品列表',
            old_name='购买地址',
            new_name='购买网址',
        ),
    ]