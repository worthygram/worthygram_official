# Generated by Django 4.1.5 on 2023-02-16 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0002_alter_contact_id_alter_facts_id_alter_quote_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Facts',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
