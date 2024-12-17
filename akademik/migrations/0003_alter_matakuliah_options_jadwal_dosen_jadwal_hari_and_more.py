# Generated by Django 5.1.2 on 2024-12-04 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0002_alter_matakuliah_options_matakuliah_kode_and_more'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matakuliah',
            options={},
        ),
        migrations.AddField(
            model_name='jadwal',
            name='dosen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.dosen'),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='hari',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='jam_mulai',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='jam_selesai',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='kuota_peserta',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='mata_kuliah',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.matakuliah'),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='ruang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.ruang'),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='semester',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='tahun_akademik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik'),
        ),
        migrations.AddField(
            model_name='krs',
            name='jadwal',
            field=models.ManyToManyField(to='akademik.jadwal'),
        ),
        migrations.AddField(
            model_name='krs',
            name='mahasiswa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.mahasiswa'),
        ),
        migrations.AddField(
            model_name='krs',
            name='tahun_akademik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik'),
        ),
        migrations.AddField(
            model_name='tahunakademik',
            name='semester',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tahunakademik',
            name='tahun',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='KHS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('mahasiswa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.mahasiswa')),
                ('mata_kuliah', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.matakuliah')),
                ('tahun_akademik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik')),
            ],
        ),
        migrations.CreateModel(
            name='SPP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_biaya', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('mahasiswa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.mahasiswa')),
                ('tahun_akademik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik')),
            ],
        ),
    ]