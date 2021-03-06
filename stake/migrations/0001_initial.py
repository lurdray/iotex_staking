# Generated by Django 3.1.7 on 2022-01-24 16:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('payment_confirmation_status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appuser')),
            ],
        ),
    ]
