# Generated by Django 2.2 on 2020-11-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201128_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]