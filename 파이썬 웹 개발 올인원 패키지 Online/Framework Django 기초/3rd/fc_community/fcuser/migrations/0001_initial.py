# Generated by Django 2.1.7 on 2022-12-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fcuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_dttm', models.DateTimeField(auto_created=True, verbose_name='등록시간')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
            ],
            options={
                'db_table': 'fastcampus_fcuser',
            },
        ),
    ]
