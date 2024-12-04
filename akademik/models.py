from django.db import models

from master.models import Dosen, Mahasiswa, Ruang


class TahunAkademik(models.Model):
    # class Meta:
    #     verbose_name = 'tahun akademik'
    #     verbose_name_plural = 'tahun akademik'
        
    tahun = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)

class MataKuliah(models.Model):
    # class Meta:
    #     verbose_name = 'mata kuliah'
    #     verbose_name_plural = 'mata kuliah'
        
    nama = models.CharField(max_length=50, null=True)
    kode = models.CharField(max_length=10, null=True)
    sks = models.IntegerField(null=True)

class Jadwal(models.Model):
    # class Meta:
    #     verbose_name = 'jadwal'
    #     verbose_name_plural = 'jadwal'
        
    dosen = models.ForeignKey(Dosen, null=True, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, null=True, on_delete=models.CASCADE)
    hari = models.CharField(max_length=20, null=True)
    jam_mulai = models.TimeField(null=True)
    jam_selesai = models.TimeField(null=True)
    semester = models.IntegerField(null=True)
    ruang = models.ForeignKey(Ruang, null=True, on_delete=models.CASCADE)
    kuota_peserta = models.IntegerField(null=True)
    tahun_akademik = models.ForeignKey(TahunAkademik, null=True, on_delete=models.CASCADE)

class KRS(models.Model):
    # class Meta:
    #     verbose_name = 'krs'
    #     verbose_name_plural = 'krs'
        
    tahun_akademik = models.ForeignKey(TahunAkademik, null=True, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, null=True, on_delete=models.CASCADE)
    jadwal = models.ManyToManyField(Jadwal)

class KHS(models.Model):
    # class Meta:
    #     verbose_name = 'khs'
    #     verbose_name_plural = 'khs'
        
    tahun_akademik = models.ForeignKey(TahunAkademik, null=True, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, null=True, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, null=True, on_delete=models.CASCADE)
    nilai = models.DecimalField(max_digits=4, decimal_places=2, null=True)

class SPP(models.Model):
    # class Meta:
    #     verbose_name = 'spp'
    #     verbose_name_plural = 'spp'
        
    tahun_akademik = models.ForeignKey(TahunAkademik, null=True, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, null=True, on_delete=models.CASCADE)
    total_biaya = models.DecimalField(max_digits=12, decimal_places=2, null=True)

