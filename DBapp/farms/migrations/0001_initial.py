# Generated by Django 3.0.6 on 2020-06-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_code', models.CharField(max_length=64)),
                ('division_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=64)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farms', to='farms.Division')),
            ],
        ),
    ]
