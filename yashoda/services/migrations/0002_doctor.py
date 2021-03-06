# Generated by Django 2.2.3 on 2019-09-04 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=100)),
                ('doctor_pic', models.CharField(max_length=1000)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
    ]
