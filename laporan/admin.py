from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    RangeDateFilter,
    MultipleChoicesDropdownFilter,
    MultipleRelatedDropdownFilter,
)
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.html import format_html
from django.contrib.admin.actions import delete_selected

from .models import Nilai, Kehadiran

@admin.register(Nilai)
class NilaiAdmin(ModelAdmin):
    list_display = ('mahasiswa', 'mata_kuliah', 'tahun_akademik', 'nilai_akhir', 'keterangan')
    list_filter = [
        ("mahasiswa", MultipleRelatedDropdownFilter),
        ("mata_kuliah", FieldTextFilter),
        ("tahun_akademik", MultipleRelatedDropdownFilter),
        ("keterangan", MultipleChoicesDropdownFilter),
    ]
    search_fields = ['mahasiswa__nama', 'mata_kuliah__nama']
    list_per_page = 20
    actions = ['convert_to_csv', 'mark_as_lulus', 'mark_as_tidak_lulus']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="nilai.csv"'
        writer = csv.writer(response)
        writer.writerow(['Mahasiswa', 'Mata Kuliah', 'Tahun Akademik', 'Nilai Akhir', 'Keterangan'])
        for obj in queryset:
            writer.writerow([obj.mahasiswa, obj.mata_kuliah, obj.tahun_akademik, obj.nilai_akhir, obj.keterangan])
        return response

    @admin.action(description='Mark as LULUS')
    def mark_as_lulus(self, request, queryset):
        queryset.update(keterangan='LULUS')
        self.message_user(request, "Selected nilai marked as LULUS")
        return reverse_lazy('admin:laporan_nilai_changelist')

    @admin.action(description='Mark as TIDAK LULUS')
    def mark_as_tidak_lulus(self, request, queryset):
        queryset.update(keterangan='TIDAK LULUS')
        self.message_user(request, "Selected nilai marked as TIDAK LULUS")
        return reverse_lazy('admin:laporan_nilai_changelist')

@admin.register(Kehadiran)
class KehadiranAdmin(ModelAdmin):
    list_display = ('mahasiswa', 'mata_kuliah', 'pertemuan_ke', 'status_kehadiran')
    list_filter = [
        ("mahasiswa", MultipleRelatedDropdownFilter),
        ("mata_kuliah", FieldTextFilter),
        ("status_kehadiran", MultipleChoicesDropdownFilter),
    ]
    search_fields = ['mahasiswa__nama', 'mata_kuliah__nama']
    list_per_page = 20
    actions = ['mark_as_hadir', 'mark_as_izin', 'mark_as_alpha', 'convert_to_csv']

    @admin.action(description='Mark as HADIR')
    def mark_as_hadir(self, request, queryset):
        queryset.update(status_kehadiran='HADIR')
        self.message_user(request, "Selected kehadiran marked as HADIR")
        return reverse_lazy('admin:laporan_kehadiran_changelist')

    @admin.action(description='Mark as IZIN')
    def mark_as_izin(self, request, queryset):
        queryset.update(status_kehadiran='IZIN')
        self.message_user(request, "Selected kehadiran marked as IZIN")
        return reverse_lazy('admin:laporan_kehadiran_changelist')

    @admin.action(description='Mark as ALPHA')
    def mark_as_alpha(self, request, queryset):
        queryset.update(status_kehadiran='ALPHA')
        self.message_user(request, "Selected kehadiran marked as ALPHA")
        return reverse_lazy('admin:laporan_kehadiran_changelist')

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="kehadiran.csv"'
        writer = csv.writer(response)
        writer.writerow(['Mahasiswa', 'Mata Kuliah', 'Pertemuan Ke', 'Status Kehadiran'])
        for obj in queryset:
            writer.writerow([obj.mahasiswa, obj.mata_kuliah, obj.pertemuan_ke, obj.status_kehadiran])
        return response
