# Generated by Django 2.1.3 on 2019-03-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]