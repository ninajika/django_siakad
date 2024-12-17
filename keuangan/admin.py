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
import csv

from .models import JenisPembayaran, Pembayaran

@admin.register(JenisPembayaran)
class JenisPembayaranAdmin(ModelAdmin):
    list_display = ('nama_pembayaran', 'jumlah', 'keterangan')
    list_filter = [
        ("nama_pembayaran", FieldTextFilter),
        ("jumlah", FieldTextFilter),
    ]
    search_fields = ('nama_pembayaran', 'jumlah')
    list_per_page = 20
    actions = ['convert_to_csv']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="jenis_pembayaran.csv"'

        writer = csv.writer(response)
        writer.writerow(['nama_pembayaran', 'jumlah', 'keterangan'])

        for obj in queryset:
            writer.writerow([obj.nama_pembayaran, obj.jumlah, obj.keterangan])

        return response

@admin.register(Pembayaran)
class PembayaranAdmin(ModelAdmin):
    list_display = ('mahasiswa', 'jenis_pembayaran', 'tanggal_pembayaran', 'jumlah_dibayar')
    list_filter = [
        ("mahasiswa", MultipleRelatedDropdownFilter),
        ("jenis_pembayaran", MultipleRelatedDropdownFilter),
        ("tanggal_pembayaran", RangeDateFilter),
    ]
    search_fields = ('mahasiswa__nama', 'jenis_pembayaran__nama_pembayaran', 'tanggal_pembayaran')
    list_per_page = 20
    actions = ['convert_to_csv']

    @admin.action(description='Convert to CSV')
    def convert_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pembayaran.csv"'

        writer = csv.writer(response)
        writer.writerow(['mahasiswa', 'jenis_pembayaran', 'tanggal_pembayaran', 'jumlah_dibayar'])

        for obj in queryset:
            writer.writerow([obj.mahasiswa, obj.jenis_pembayaran, obj.tanggal_pembayaran, obj.jumlah_dibayar])

        return response
