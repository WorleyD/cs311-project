# Generated by Django 2.1.2 on 2018-11-20 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.IntegerField()),
                ('department', models.IntegerField()),
                ('course', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('review_amt', models.IntegerField()),
                ('review_avg', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.CharField(max_length=3)),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finder.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finder.Course')),
            ],
        ),
    ]
