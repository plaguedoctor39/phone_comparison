# Generated by Django 2.2.10 on 2020-08-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.TextField()),
                ('price', models.IntegerField()),
                ('op_sys', models.TextField()),
                ('ram', models.IntegerField()),
                ('pixels_per_inch', models.IntegerField()),
                ('double_cam', models.BooleanField(blank=True)),
                ('processor', models.TextField()),
                ('resolution', models.TextField()),
                ('fm_radio', models.BooleanField(blank=True)),
            ],
            options={
                'db_table': 'phones',
            },
        ),
        migrations.CreateModel(
            name='SamsungPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]