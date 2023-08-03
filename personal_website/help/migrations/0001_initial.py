# Generated by Django 4.1 on 2023-08-01 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0022_user_field_user_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=2000)),
                ('field', models.CharField(choices=[(0, '自动化/控制工程'), (1, '计算机'), (2, '机械'), (3, '土木'), (4, '电气'), (5, '生物'), (6, '环境'), (7, '化学'), (8, '材料')], max_length=20)),
                ('hits', models.IntegerField(default=0)),
                ('state', models.IntegerField(choices=[(0, '正在竞标'), (1, '已结束')])),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.user')),
            ],
        ),
        migrations.CreateModel(
            name='RequestFollows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_price', models.IntegerField()),
                ('state', models.IntegerField(choices=[(0, '未中标'), (1, '已中标')])),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help.request')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.user')),
            ],
        ),
    ]
