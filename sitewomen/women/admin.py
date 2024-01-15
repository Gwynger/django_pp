from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category


# Определение и настройка своего фильтра
class MarriedFilter(admin.SimpleListFilter):
    title = "Women's status"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Married'),
            ('single', 'Single'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'photo', 'post_photo', 'slug', 'cat', 'husband']  # exclude - исключает поля из формы
    readonly_fields = ['post_photo']  # делает поле нередактируемым
    list_display = ('id', 'title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    ordering = ('time_create', 'title')
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Picture', ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f'<img src="{women.photo.url}", width=50>')
        return 'No photo'

    @admin.action(description='Publish selected entries')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Changed {count} entries')

    @admin.action(description='Remove selected entries')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'Changed {count} entries', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# admin.site.register(Women, WomenAdmin)
