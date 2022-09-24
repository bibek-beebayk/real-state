from django.contrib import admin

from apps.property.models import Property, PropertyImage, Amenity, Facility


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 0


class FacilityInline(admin.TabularInline):
    model = Facility
    extra = 0


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'price']
    list_filter = ['property_type', 'contract_type']
    search_fields = ['title', 'address', 'description']
    list_per_page = 25
    inlines = [PropertyImageInline, FacilityInline]
