# Generated by Django 2.0.1 on 2018-02-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PROXY_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=32)),
                ('salt', models.CharField(max_length=54)),
                ('session_token', models.CharField(max_length=54, null=True)),
            ],
        ),
    ]