# Generated by Django 3.2 on 2021-05-19 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210505_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=140),
        ),
    ]
