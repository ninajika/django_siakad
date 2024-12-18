from django.db import models
from master.models import Mahasiswa

class JenisPembayaran(models.Model):
    
    class Meta:
        verbose_name = "Jenis Pembayaran"
        verbose_name_plural = "Jenis Pembayaran"
        indexes = [
            models.Index(fields=['nama_pembayaran']),
        ]
        
    nama_pembayaran = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_pembayaran

class Pembayaran(models.Model):
    class Meta:
        verbose_name = "Pembayaran"
        verbose_name_plural = "Pembayaran"
        indexes = [
            models.Index(fields=['tanggal_pembayaran']),
            models.Index(fields=['mahasiswa']),
            models.Index(fields=['jenis_pembayaran']),
        ]
        
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    jenis_pembayaran = models.ForeignKey(JenisPembayaran, on_delete=models.CASCADE)
    tanggal_pembayaran = models.DateField()
    jumlah_dibayar = models.DecimalField(max_digits=12, decimal_places=2)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.mahasiswa} - {self.jenis_pembayaran}"
