# Generated by Django 3.2.9 on 2022-01-21 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.TextField(choices=[('BENZYNA', 'Benzyna'), ('LPG', 'LPG'), ('DIESEL', 'Diesel'), ('ELEKTRYCZNY', 'Elektryczny'), ('HYBRYDA', 'Hybryda')], default='BENZYNA', max_length=25)),
                ('power', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('transmission', models.TextField(choices=[('MANUALNA', 'Manualna'), ('AUTOMATYCZNA', 'Automatyczna')], default='MANUALNA', max_length=25)),
                ('mark', models.TextField(default='', max_length=25)),
                ('model', models.TextField(default='', max_length=25)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['mark'],
            },
        ),
    ]