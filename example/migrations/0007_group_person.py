# Generated by Django 3.1.5 on 2021-01-29 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_delete_geeksmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.person')),
            ],
        ),
    ]
