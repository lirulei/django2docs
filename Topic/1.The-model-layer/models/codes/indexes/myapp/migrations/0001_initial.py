# Generated by Django 2.1 on 2018-09-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='myapp_custo_last_na_cd1c3a_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name'], name='first_name_idx'),
        ),
    ]
