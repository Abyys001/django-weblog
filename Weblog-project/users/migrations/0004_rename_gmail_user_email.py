# Generated by Django 4.2.3 on 2023-07-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gmail',
            new_name='email',
        ),
    ]
