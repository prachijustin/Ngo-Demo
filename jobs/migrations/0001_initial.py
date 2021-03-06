# Generated by Django 2.1.1 on 2019-12-08 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('minAge', models.PositiveIntegerField()),
                ('maxAge', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=1000)),
                ('vacancy', models.PositiveIntegerField()),
                ('generalFee', models.PositiveIntegerField()),
                ('obcFee', models.PositiveIntegerField()),
                ('scstFee', models.PositiveIntegerField()),
                ('payment', models.CharField(default=1, max_length=100)),
                ('addedDate', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-addedDate'],
            },
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.CharField(max_length=100)),
                ('jobID', models.PositiveIntegerField()),
                ('candidateFirstName', models.CharField(max_length=50)),
                ('candidateMiddleName', models.CharField(blank=True, max_length=50)),
                ('candidateLastName', models.CharField(max_length=50)),
                ('relativeType', models.CharField(default='Father', max_length=10)),
                ('fatherFirstName', models.CharField(max_length=50)),
                ('fatherMiddleName', models.CharField(blank=True, max_length=50)),
                ('fatherLastName', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('aadhaar', models.CharField(max_length=12)),
                ('caste', models.CharField(max_length=20)),
                ('addr1', models.CharField(max_length=100)),
                ('village1', models.CharField(max_length=100)),
                ('post1', models.CharField(max_length=100)),
                ('panchayat1', models.CharField(max_length=100)),
                ('ward1', models.CharField(max_length=100)),
                ('block1', models.CharField(max_length=100)),
                ('district1', models.CharField(max_length=100)),
                ('city1', models.CharField(max_length=100)),
                ('pin1', models.PositiveIntegerField()),
                ('addr2', models.CharField(max_length=100)),
                ('village2', models.CharField(max_length=100)),
                ('post2', models.CharField(max_length=100)),
                ('panchayat2', models.CharField(max_length=100)),
                ('ward2', models.CharField(max_length=100)),
                ('block2', models.CharField(max_length=100)),
                ('district2', models.CharField(max_length=100)),
                ('city2', models.CharField(max_length=100)),
                ('pin2', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=50)),
                ('board1', models.CharField(blank=True, default=None, max_length=200)),
                ('percentage1', models.CharField(blank=True, default=1, max_length=10)),
                ('board2', models.CharField(blank=True, default=None, max_length=200)),
                ('percentage2', models.CharField(blank=True, default=1, max_length=10)),
                ('board3', models.CharField(blank=True, default=None, max_length=200)),
                ('percentage3', models.CharField(blank=True, default=1, max_length=10)),
                ('pic', models.ImageField(upload_to='candidates/pics/')),
                ('signhin', models.ImageField(upload_to='candidates/signhin/')),
                ('signeng', models.ImageField(upload_to='candidates/signeng/')),
                ('status', models.CharField(default='APPL', max_length=5)),
                ('appliedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('payStatus', models.CharField(default='PEND', max_length=4)),
                ('transactionID', models.CharField(default=0, max_length=200)),
            ],
            options={
                'ordering': ['-appliedDate'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('jobid', models.CharField(max_length=10000)),
                ('orderDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-orderDate'],
            },
        ),
    ]
