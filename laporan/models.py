from django.db import models
from master.models import Mahasiswa
from akademik.models import MataKuliah, TahunAkademik

class Nilai(models.Model):
    
    class Meta:
        indexes = [
            models.Index(fields=['mahasiswa', 'mata_kuliah', 'tahun_akademik']),
        ]
        verbose_name = "Nilai"
        verbose_name_plural = "Nilai"
        
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE)
    nilai_akhir = models.DecimalField(max_digits=5, decimal_places=2)
    keterangan = models.CharField(max_length=50, choices=[('LULUS', 'Lulus'), ('TIDAK LULUS', 'Tidak Lulus')])

    def __str__(self):
        return f"{self.mahasiswa} - {self.nilai_akhir}"

class Kehadiran(models.Model):
    
    class Meta:
        indexes = [
            models.Index(fields=['mahasiswa', 'mata_kuliah']),
        ]
        verbose_name = "Kehadiran"
        verbose_name_plural = "Kehadiran"
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    pertemuan_ke = models.IntegerField()
    status_kehadiran = models.CharField(max_length=10, choices=[('HADIR', 'Hadir'), ('ALPHA', 'Alpha'), ('IZIN', 'Izin')])

    def __str__(self):
        return f"{self.mahasiswa} - {self.mata_kuliah} - Pertemuan {self.pertemuan_ke}"