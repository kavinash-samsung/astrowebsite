# Generated by Django 3.2.5 on 2021-08-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20210826_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='vastu',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterModelOptions(
            name='vedicastrology',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='service',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='vastu',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='vedicastrology',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
