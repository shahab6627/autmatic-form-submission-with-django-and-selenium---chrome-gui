# Generated by Django 4.2.4 on 2023-08-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
