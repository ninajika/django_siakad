# Generated by Django 5.1.2 on 2024-12-17 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('sks', models.IntegerField()),
                ('jam_mulai', models.TimeField()),
                ('jam_selesai', models.TimeField()),
                ('semester', models.CharField(max_length=10)),
                ('dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.dosen')),
            ],
            options={
                'verbose_name': 'Jadwal',
                'verbose_name_plural': 'Jadwal',
            },
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('kode', models.CharField(max_length=10)),
                ('sks', models.IntegerField()),
                ('prodi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.prodi')),
            ],
            options={
                'verbose_name': 'Mata Kuliah',
                'verbose_name_plural': 'Mata Kuliah',
            },
        ),
        migrations.CreateModel(
            name='TahunAkademik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Tahun Akademik',
                'verbose_name_plural': 'Tahun Akademik',
                'indexes': [models.Index(fields=['tahun'], name='akademik_ta_tahun_190715_idx')],
            },
        ),
        migrations.CreateModel(
            name='KRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jadwal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.jadwal')),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.mahasiswa')),
                ('tahun_akademik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik')),
            ],
            options={
                'verbose_name': 'KRS',
                'verbose_name_plural': 'KRS',
            },
        ),
        migrations.AddIndex(
            model_name='jadwal',
            index=models.Index(fields=['nama'], name='akademik_ja_nama_ccbb3c_idx'),
        ),
        migrations.AddIndex(
            model_name='matakuliah',
            index=models.Index(fields=['nama'], name='akademik_ma_nama_f160c9_idx'),
        ),
        migrations.AddIndex(
            model_name='matakuliah',
            index=models.Index(fields=['kode'], name='akademik_ma_kode_40953b_idx'),
        ),
    ]
