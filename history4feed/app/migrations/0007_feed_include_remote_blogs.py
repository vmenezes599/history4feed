# Generated by Django 5.0.6 on 2024-07-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_fulltextjob_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='include_remote_blogs',
            field=models.BooleanField(default=False),
        ),
    ]
