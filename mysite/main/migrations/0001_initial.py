# Generated by Django 3.1.3 on 2020-11-30 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maneger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mail_adress', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Id', models.URLField(primary_key=True, serialize=False)),
                ('age', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('volunteer_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Elderly',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.person')),
                ('phone_number', models.UUIDField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            bases=('main.person',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.person')),
                ('phone_number', models.UUIDField()),
            ],
            bases=('main.person',),
        ),
    ]
