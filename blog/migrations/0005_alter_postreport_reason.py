# Generated by Django 4.1.5 on 2023-02-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_certify_author_alter_certify_certify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreport',
            name='reason',
            field=models.CharField(choices=[('SPAM', 'SPAM'), ('INAPPROPRIATE', 'INAPPROPRIATE'), ('NEGATIVE', 'NEGATIVE'), ('ABUSIVE', 'ABUSIVE')], max_length=150),
        ),
    ]