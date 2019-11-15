from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','city','guide')
    list_display_links=('id','city')
    list_filter=('guide',)
    search_fields=('city','description','state','country')
    list_per_page=25

admin.site.register(Listing,ListingAdmin)
