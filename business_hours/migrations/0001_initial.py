# Generated by Django 5.1.2 on 2024-10-29 14:21

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessHours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weekday', models.IntegerField(choices=[(1, '星期一'), (2, '星期二'), (3, '星期三'), (4, '星期四'), (5, '星期五'), (6, '星期六'), (7, '星期日')], unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)], verbose_name='星期')),
                ('start_time', models.TimeField(verbose_name='开始时间')),
                ('end_time', models.TimeField(verbose_name='结束时间')),
                ('is_open', models.BooleanField(default=True, verbose_name='是否营业')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '营业时间',
                'verbose_name_plural': '营业时间',
                'ordering': ['weekday'],
            },
        ),
    ]