# Generated by Django 4.2.4 on 2023-08-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_testresult_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
