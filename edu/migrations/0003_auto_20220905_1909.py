# Generated by Django 3.2.5 on 2022-09-05 18:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_auto_20220905_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(choices=[('mathematics', 'mathematics'), ('english', 'english'), ('physics', 'physics'), ('chemistry', 'chemistry'), ('biology', 'biology'), ('economics', 'economics'), ('accounts', 'accounts'), ('government', 'government'), ('literature', 'literature'), ('geography', 'geography'), ('futher-maths', 'futher-maths')], max_length=120, verbose_name='Select Subject')),
                ('classname', models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SSS1', 'SSS1'), ('SSS2', 'SSS2'), ('SSS3', 'SSS3')], max_length=120, verbose_name='Select Class')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.TextField(max_length=12000)),
                ('textbooks', models.TextField(max_length=12000)),
                ('syllabus_class', models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SSS1', 'SSS1'), ('SSS2', 'SSS2'), ('SSS3', 'SSS3')], default='', max_length=60)),
                ('syllabus_term', models.CharField(choices=[('1ST TERM', '1ST TERM'), ('2ND TERM', '2ND TERM'), ('3RD TERM', '3RD TERM')], default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.TextField(max_length=12000)),
                ('textbooks', models.TextField(max_length=12000)),
                ('syllabus_class', models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SSS1', 'SSS1'), ('SSS2', 'SSS2'), ('SSS3', 'SSS3')], default='', max_length=60)),
                ('syllabus_term', models.CharField(choices=[('1ST TERM', '1ST TERM'), ('2ND TERM', '2ND TERM'), ('3RD TERM', '3RD TERM')], default='', max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='teacherupload',
            name='audio',
            field=models.FileField(default='', upload_to='audio'),
        ),
        migrations.AddField(
            model_name='teacherupload',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='teacherupload',
            name='videos',
            field=models.FileField(default='', upload_to='video'),
        ),
        migrations.AlterField(
            model_name='teacherupload',
            name='slug',
            field=models.SlugField(verbose_name='Add subject abbreviation, pick three letter from topic, add class and term and  date e.g mtsalgjss11'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('commentpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='edu.teacherupload')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='edu.comment')),
            ],
        ),
        migrations.CreateModel(
            name='add_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('video', models.FileField(default='', upload_to='video')),
                ('sound', models.FileField(default='', upload_to='sound')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='edu.add_comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_comments', to='edu.teacherupload')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
