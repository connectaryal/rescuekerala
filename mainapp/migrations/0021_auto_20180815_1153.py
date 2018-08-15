# Generated by Django 2.1 on 2018-08-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20180815_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(choices=[('tvm', 'Thiruvananthapuram'), ('ptm', 'Pathanamthitta'), ('alp', 'Alappuzha'), ('ktm', 'Kottayam'), ('idk', 'Idukki'), ('mpm', 'Malappuram'), ('koz', 'Kozhikode'), ('wnd', 'Wayanad'), ('knr', 'Kannur'), ('ksr', 'Kasaragod'), ('pkd', 'Palakkad'), ('tcr', 'Thrissur'), ('ekm', 'Ernakulam'), ('kol', 'Kollam')], max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='is_dm',
        ),
    ]