from django.contrib import admin

# Register your models here.

from .models import SearchWord, Recommendation

class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 5

class SearchWordAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['search_word_text']}),
            ('Date Information', {'fields': ['search_date'],
                                  'classes': ['collapse']}),
            ]
    inlines = [RecommendationInline]
    list_display = ('search_word_text', 'search_date')
    list_filter = ['search_date']
    search_fields = ['search_word_text']

admin.site.register(SearchWord, SearchWordAdmin)
