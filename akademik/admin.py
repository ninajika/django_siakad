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

from .models import TahunAkademik, MataKuliah, Jadwal, KRS

@admin.register(TahunAkademik)
class TahunAkademikAdmin(ModelAdmin):
    list_display = ('tahun', 'semester')
    list_filter = [
        ("tahun", FieldTextFilter),
        ("semester", MultipleChoicesDropdownFilter),
    ]
    search_fields = ('tahun', 'semester')
    list_per_page = 20
    actions = ['convert_to_csv']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tahun_akademik.csv"'
        writer = csv.writer(response)
        writer.writerow(['Tahun', 'Semester'])
        for obj in queryset.all():
            writer.writerow([obj.tahun, obj.semester])
        return response

@admin.register(MataKuliah)
class MataKuliahAdmin(ModelAdmin):
    list_display = ('nama', 'kode', 'prodi', 'sks')
    list_filter = [
        ("nama", FieldTextFilter),
        ("kode", FieldTextFilter),
        ("prodi", MultipleChoicesDropdownFilter),
    ]
    search_fields = ('nama', 'kode', 'prodi')
    list_per_page = 20
    actions = ['convert_to_csv']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mata_kuliah.csv"'
        writer = csv.writer(response)
        writer.writerow(['Nama', 'Kode', 'Prodi', 'SKS'])
        for obj in queryset:
            writer.writerow([obj.nama, obj.kode, obj.prodi, obj.sks])
        return response

@admin.register(Jadwal)
class JadwalAdmin(ModelAdmin):
    list_display = ('nama', 'dosen', 'sks', 'jam_mulai', 'jam_selesai', 'semester')
    list_filter = [
        ("nama", FieldTextFilter),
        ("dosen", MultipleRelatedDropdownFilter),
        ("semester", MultipleChoicesDropdownFilter),
    ]
    search_fields = ('nama', 'dosen__nama')
    list_per_page = 20
    actions = ['convert_to_csv']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="jadwal.csv"'
        writer = csv.writer(response)
        writer.writerow(['Nama', 'Dosen', 'SKS', 'Jam Mulai', 'Jam Selesai', 'Semester'])
        for obj in queryset:
            writer.writerow([obj.nama, obj.dosen, obj.sks, obj.jam_mulai, obj.jam_selesai, obj.semester])
        return response

@admin.register(KRS)
class KRSAdmin(ModelAdmin):
    list_display = ('tahun_akademik', 'mahasiswa', 'jadwal')
    list_filter = [
        ("tahun_akademik", MultipleRelatedDropdownFilter),
        ("mahasiswa", MultipleRelatedDropdownFilter),
        ("jadwal", MultipleRelatedDropdownFilter),
    ]
    search_fields = ('tahun_akademik__tahun', 'mahasiswa__nama', 'jadwal__nama')
    list_per_page = 20
    actions = ['convert_to_csv']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="krs.csv"'
        writer = csv.writer(response)
        writer.writerow(['Tahun Akademik', 'Mahasiswa', 'Jadwal'])
        for obj in queryset:
            writer.writerow([obj.tahun_akademik, obj.mahasiswa, obj.jadwal])
        return response
