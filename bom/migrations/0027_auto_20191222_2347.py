# Generated by Django 2.2.9 on 2019-12-22 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0026_auto_20191222_2258'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='partclass',
            index_together={('organization', 'code')},
        ),
    ]
