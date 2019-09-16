from django.contrib import admin
from reservations.models import Reservation, Appartment, AppartmentImage
from django.utils.html import format_html


class AppartmentImageInline(admin.TabularInline):
    model = AppartmentImage


@admin.register(Appartment)
class AppartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_appartment_url','is_bookable','price')
    inlines = [AppartmentImageInline]

    def show_appartment_url(self, obj):
        if not obj.is_visible:
            return "This apartment is only visible in admin"
        return format_html('<a href="/{url}">{url}</a>', url=obj.slug)

    show_appartment_url.short_description = "Link to appartment page"


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name','appartment', 'start_date', 'end_date','status','created_date')
    list_filter = ('appartment',)
    search_fields = ('name',)
