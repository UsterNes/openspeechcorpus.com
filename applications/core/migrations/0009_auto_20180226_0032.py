# Generated by Django 2.0.1 on 2018-02-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160115_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiodata',
            name='audiofile',
            field=models.FileField(upload_to='audio-data'),
        ),
    ]