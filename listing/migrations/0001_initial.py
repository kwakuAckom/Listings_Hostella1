# Generated by Django 4.1.7 on 2023-03-12 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtor', models.EmailField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('payment_method', models.CharField(choices=[('Mobile money', 'Mobile Money'), ('Bank Payment', 'Bank'), ('Credit or debit card payment', 'Debit Card'), ('Meet and pay in person', 'Personal')], max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('room_capacity', models.IntegerField()),
                ('bathroom', models.BooleanField()),
                ('kitchen', models.BooleanField()),
                ('hostel_class', models.CharField(max_length=1)),
                ('hometype', models.CharField(choices=[('Hostel', 'Hostel'), ('Homestel', 'Homestel')], max_length=10)),
                ('distance', models.CharField(choices=[('On campus', 'Campus'), ('Close to campus', 'Close'), ('Normal distance from campus', 'Normal'), ('Far from campus', 'Far')], max_length=50)),
                ('photo1', models.ImageField(upload_to='')),
                ('photo2', models.ImageField(upload_to='')),
                ('photo3', models.ImageField(upload_to='')),
                ('is_published', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
