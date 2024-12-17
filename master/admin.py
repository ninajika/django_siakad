from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    RangeDateFilter,
    MultipleChoicesDropdownFilter,
    MultipleRelatedDropdownFilter,
)

from .models import (
    Prodi,
    Mahasiswa,
    Dosen,
    Ruang
)


@admin.register(Prodi)
class ProdiAdmin(ModelAdmin):
    list_display = ('nama', 'kode')
    list_filter = [
        ("nama", FieldTextFilter),
        ("kode", FieldTextFilter),
    ]


@admin.register(Mahasiswa)
class MahasiswaAdmin(ModelAdmin):
    list_display = ('nama', 'nim', 'prodi')
    list_filter = [
        ("nama", FieldTextFilter),
        ("nim", FieldTextFilter),
        ("prodi", MultipleRelatedDropdownFilter),
    ]


@admin.register(Dosen)
class DosenAdmin(ModelAdmin):
    list_display = ('nama', 'nid', 'tgl_lahir', 'jenis_kelamin', 'prodi')
    list_filter_submit = True
    list_filter = [
        ("nama", FieldTextFilter),
        ("tgl_lahir", RangeDateFilter),
        ("jenis_kelamin", MultipleChoicesDropdownFilter),
        ("prodi", MultipleRelatedDropdownFilter),
    ]


@admin.register(Ruang)
class RuangAdmin(ModelAdmin):
    list_display = ('nama', 'kode')
    list_filter = [
        ("nama", FieldTextFilter),
        ("kode", FieldTextFilter),
    ]
