# Generated by Django 3.0 on 2023-06-18 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_delete_profile'),
    ]

    state_operations = [
        migrations.RemoveField(
            model_name='letting',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable('Address', 'lettings_Address'),
                migrations.AlterModelTable('Letting', 'lettings_Letting'),
            ],
            state_operations=state_operations
        )
    ]
