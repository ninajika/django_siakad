# Generated by Django 5.1.2 on 2024-12-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0001_initial'),
        ('laporan', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kehadiran',
            options={'verbose_name': 'Kehadiran', 'verbose_name_plural': 'Kehadiran'},
        ),
        migrations.AlterModelOptions(
            name='nilai',
            options={'verbose_name': 'Nilai', 'verbose_name_plural': 'Nilai'},
        ),
        migrations.AlterField(
            model_name='kehadiran',
            name='pertemuan_ke',
            field=models.IntegerField(),
        ),
        migrations.AddIndex(
            model_name='kehadiran',
            index=models.Index(fields=['mahasiswa', 'mata_kuliah'], name='laporan_keh_mahasis_3a30c3_idx'),
        ),
        migrations.AddIndex(
            model_name='nilai',
            index=models.Index(fields=['mahasiswa', 'mata_kuliah', 'tahun_akademik'], name='laporan_nil_mahasis_b8566e_idx'),
        ),
    ]
