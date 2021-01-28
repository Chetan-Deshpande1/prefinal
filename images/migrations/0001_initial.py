# Generated by Django 3.1.2 on 2020-11-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='images')),
                ('uploded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
    ]
