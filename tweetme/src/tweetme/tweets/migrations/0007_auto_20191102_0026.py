# Generated by Django 2.2.5 on 2019-11-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20191006_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp']},
        ),
    ]