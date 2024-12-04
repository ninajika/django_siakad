from django.contrib import admin
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    SliderNumericFilter,
    RangeNumericFilter,
    RangeDateTimeFilter,
    RangeNumericListFilter,
)
from django.contrib.admin import SimpleListFilter

from akademik.models import TahunAkademik, MataKuliah, Jadwal, KRS, KHS, SPP

class TahunSliderFilter(SliderNumericFilter):
    parameter_name = "tahun"
    title = "tahun"
    
@admin.register(TahunAkademik)
class TahunAkademikAdmin(ModelAdmin):
    list_display = ["tahun", "semester"]
    list_filter_submit = True
    list_filter = [
        ("tahun", SliderNumericFilter),
        ("semester", FieldTextFilter),
    ]
    ordering = ["tahun", "semester"]
    search_fields = ["tahun", "semester"]
    actions = ["set_semester_genap", "set_semester_ganjil"]
    def set_semester_genap(self, request, queryset):
        queryset.update(semester=1)
    set_semester_genap.short_description = "Set to Semester Genap"
    def set_semester_ganjil(self, request, queryset):
        queryset.update(semester=2)
    set_semester_ganjil.short_description = "Set to Semester Ganjil"

class SKSSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 8

@admin.register(MataKuliah)
class MataKuliahAdmin(ModelAdmin):
    list_display = ["nama", "kode", "sks"]
    list_filter_submit = True
    list_filter = [
        ("nama", FieldTextFilter),
        ("kode", FieldTextFilter),
        ("sks", SKSSliderNumericFilter),
    ]
    ordering = ["nama"]
    search_fields = ["nama", "kode", "sks"]

class TimeFilter(SimpleListFilter):
    title = _('Waktu')
    parameter_name = 'time'

    def lookups(self, request, model_admin):
        return [
            ('pagi', _('Pagi (06:00-11:00)')),
            ('siang', _('Siang (11:00-15:00)')),
            ('sore', _('Sore (15:00-18:00)')),
            ('malam', _('Malam (18:00-22:00)')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'pagi':
            return queryset.filter(jam_mulai__hour__gte=6, jam_mulai__hour__lt=11)
        if self.value() == 'siang':
            return queryset.filter(jam_mulai__hour__gte=11, jam_mulai__hour__lt=15)
        if self.value() == 'sore':
            return queryset.filter(jam_mulai__hour__gte=15, jam_mulai__hour__lt=18)
        if self.value() == 'malam':
            return queryset.filter(jam_mulai__hour__gte=18, jam_mulai__hour__lt=22)
        return queryset

@admin.register(Jadwal)
class JadwalAdmin(ModelAdmin):
    list_display = ["dosen", "mata_kuliah", "hari", "jam_mulai", "jam_selesai", "semester", "ruang", "tahun_akademik"]
    list_filter_submit = True
    list_filter = [
        ("dosen", FieldTextFilter),
        ("mata_kuliah", FieldTextFilter),
        ("hari", FieldTextFilter),
        TimeFilter,
        ("semester", FieldTextFilter),
        ("ruang", FieldTextFilter),
        ("tahun_akademik", FieldTextFilter),
    ]
    ordering = ["dosen", "mata_kuliah", "hari", "jam_mulai"]
    search_fields = ["dosen", "mata_kuliah", "hari", "jam_mulai", "jam_selesai", "semester", "ruang", "tahun_akademik"]

@admin.register(KRS)
class KRSAdmin(ModelAdmin):
    list_display = ["tahun_akademik", "mahasiswa"]
    list_filter_submit = True
    list_filter = [
        ("tahun_akademik", FieldTextFilter),
        ("mahasiswa", FieldTextFilter),
    ]
    ordering = ["tahun_akademik", "mahasiswa"]
    search_fields = ["tahun_akademik", "mahasiswa"]

class NilaiSliderFilter(SliderNumericFilter):
    parameter_name = "nilai"
    title = "nilai"
    MAX_DECIMALS = 2
    STEP = 0.1
    
@admin.register(KHS)
class KHSAdmin(ModelAdmin):
    list_display = ["tahun_akademik", "mahasiswa", "mata_kuliah", "nilai"]
    list_filter_submit = True
    list_filter = [
        ("tahun_akademik", FieldTextFilter),
        ("mahasiswa", FieldTextFilter),
        ("mata_kuliah", FieldTextFilter),
        ("nilai", NilaiSliderFilter),
    ]
    ordering = ["tahun_akademik", "mahasiswa", "mata_kuliah"]
    search_fields = ["tahun_akademik", "mahasiswa", "mata_kuliah", "nilai"]

@admin.register(SPP)
class SPPAdmin(ModelAdmin):
    list_display = ["tahun_akademik", "mahasiswa", "total_biaya"]
    list_filter_submit = True
    list_filter = [
        ("tahun_akademik", FieldTextFilter),
        ("mahasiswa", FieldTextFilter),
        ("total_biaya", RangeNumericFilter),
    ]
    ordering = ["tahun_akademik", "mahasiswa"]
    search_fields = ["tahun_akademik", "mahasiswa", "total_biaya"]
