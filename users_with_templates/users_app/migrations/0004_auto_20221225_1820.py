# Generated by Django 2.2.4 on 2022-12-25 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_auto_20221225_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_address',
            new_name='email',
        ),
    ]
