# Generated by Django 3.0 on 2023-06-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable('Profile', 'profiles_NewProfile'),
            ],
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ]
        )
    ]
