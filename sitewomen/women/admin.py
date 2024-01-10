from django.contrib import admin, messages
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
    fields = ['title', 'content', 'slug', 'cat', 'husband']  # exclude - исключает поля из формы
    readonly_fields = ['slug']  # делает поле нередактируемым
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('id', 'title')
    ordering = ('time_create', 'title')
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    def brief_info(self, women: Women):
        return f'Description {len(women.content)} symbols.'

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
