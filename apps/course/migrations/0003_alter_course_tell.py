# Generated by Django 4.2.7 on 2024-12-25 05:50

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tell',
            field=mdeditor.fields.MDTextField(default='#### 课程须知\n如果有问题及时反馈  \n#### 你能学到什么\n电力行业的相关知识\n', verbose_name='需要告知的内容'),
        ),
    ]