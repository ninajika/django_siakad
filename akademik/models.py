from django.db import models

from master.models import Dosen, Mahasiswa, Prodi

class TahunAkademik(models.Model):
    tahun = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return self.tahun + ' ' + self.semester

    class Meta:
        verbose_name = 'Tahun Akademik'
        verbose_name_plural = 'Tahun Akademik'
        indexes = [
            models.Index(fields=['tahun']),
        ]


class MataKuliah(models.Model):
    nama = models.CharField(max_length=255)
    kode = models.CharField(max_length=10)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, blank=True, null=True)    
    sks = models.IntegerField()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'Mata Kuliah'
        verbose_name_plural = 'Mata Kuliah'
        indexes = [
            models.Index(fields=['nama']),
            models.Index(fields=['kode']),
        ]

class Jadwal(models.Model):
    nama = models.CharField(max_length=255)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    sks = models.IntegerField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    semester = models.CharField(max_length=10)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'Jadwal'
        verbose_name_plural = 'Jadwal'
        indexes = [
            models.Index(fields=['nama']),
        ]

class KRS(models.Model):
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tahun_akademik) + ' ' + str(self.mahasiswa) + ' ' + str(self.jadwal)

    class Meta:
        verbose_name = 'KRS'
        verbose_name_plural = 'KRS'
