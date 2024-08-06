from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.template.response import TemplateResponse
from .models import Categories, System, Buttons, Messages, Lists, ListTitles, FlowerType, BouquetType, FlowerSubtype, FlowerColor


class CustomAdminSite(admin.AdminSite):
    site_header = 'Административная панель'

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        return TemplateResponse(request, 'admin/index.html', self.each_context(request))


admin_site = CustomAdminSite()


class ContentAdmin(admin.AdminSite):
    site_header = 'Содержимое бота'


content_admin_site = ContentAdmin(name='content')


class NomenclatureAdmin(admin.AdminSite):
    site_header = 'Номенклатура цветов'


nomenclature_admin_site = NomenclatureAdmin(name='nomenclature')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']


class SystemAdmin(admin.ModelAdmin):
    list_display = ['variable', 'text', 'category', 'screen']
    list_filter = ['category']
    search_fields = ['variable', 'text']
    readonly_fields = ['variable']


class ButtonsAdmin(admin.ModelAdmin):
    list_display = ['variable', 'text', 'category', 'screen']
    list_filter = ['category']
    search_fields = ['variable', 'text']
    readonly_fields = ['variable']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['variable', 'text', 'category', 'screen']
    list_filter = ['category']
    search_fields = ['variable', 'text']
    readonly_fields = ['variable']


class ListsAdmin(admin.ModelAdmin):
    list_display = ['variable', 'text', 'category', 'screen']
    list_filter = ['category']
    search_fields = ['variable', 'text']
    readonly_fields = ['variable']


class ListTitlesAdmin(admin.ModelAdmin):
    list_display = ['variable', 'text', 'category', 'screen']
    list_filter = ['category']
    search_fields = ['variable', 'text']
    readonly_fields = ['variable']


class BouquetTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'view_flower_types_link']

    def view_flower_types_link(self, obj):
        count = obj.flower_types.count()
        url = reverse("nomenclature:AdminPanel_flowertype_changelist") + "?bouquet_type__id__exact=" + str(obj.id)
        return format_html('<a href="{}">Типы цветков ({})</a>', url, count)

    view_flower_types_link.short_description = "Типы цветков"

    search_fields = ['name']


class FlowerTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'bouquet_type_link', 'view_subtypes_link']

    def bouquet_type_link(self, obj):
        url = reverse("nomenclature:AdminPanel_bouquettype_changelist") + f"?id__exact={obj.bouquet_type.id}"
        return format_html('<a href="{}">{}</a>', url, obj.bouquet_type.name)

    bouquet_type_link.short_description = "Тип букета"

    def view_subtypes_link(self, obj):
        count = obj.sub_types.count()
        url = reverse("nomenclature:AdminPanel_flowersubtype_changelist") + "?flower_type__id__exact=" + str(obj.id)
        return format_html('<a href="{}">Подвиды ({})</a>', url, count)

    view_subtypes_link.short_description = "Подвиды цветков"

    list_filter = ['bouquet_type']
    search_fields = ['name']


class FlowerSubtypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'flower_type_link', 'view_colors_link']

    def flower_type_link(self, obj):
        url = reverse("nomenclature:AdminPanel_flowertype_changelist") + f"?id__exact={obj.flower_type.id}"
        return format_html('<a href="{}">{}</a>', url, obj.flower_type.name)

    flower_type_link.short_description = "Тип цветка"

    def view_colors_link(self, obj):
        count = obj.colors.count()
        url = reverse("nomenclature:AdminPanel_flowercolor_changelist") + "?flower_subtype__id__exact=" + str(obj.id)
        return format_html('<a href="{}">Цвета ({})</a>', url, count)

    view_colors_link.short_description = "Цвета цветков"

    list_filter = ['flower_type']
    search_fields = ['name']


class FlowerColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'flower_subtype_link']

    def flower_subtype_link(self, obj):
        url = reverse("nomenclature:AdminPanel_flowersubtype_changelist") + f"?id__exact={obj.flower_subtype.id}"
        return format_html('<a href="{}">{}</a>', url, obj.flower_subtype.name)

    flower_subtype_link.short_description = "Подвид цветка"

    list_filter = ['flower_subtype']
    search_fields = ['name']


content_admin_site.register(Categories, CategoriesAdmin)
content_admin_site.register(System, SystemAdmin)
content_admin_site.register(Buttons, ButtonsAdmin)
content_admin_site.register(Messages, MessagesAdmin)
content_admin_site.register(Lists, ListsAdmin)
content_admin_site.register(ListTitles, ListTitlesAdmin)

nomenclature_admin_site.register(FlowerType, FlowerTypeAdmin)
nomenclature_admin_site.register(BouquetType, BouquetTypeAdmin)
nomenclature_admin_site.register(FlowerSubtype, FlowerSubtypeAdmin)
nomenclature_admin_site.register(FlowerColor, FlowerColorAdmin)


admin_site.register(Categories, CategoriesAdmin)
admin_site.register(System, SystemAdmin)
admin_site.register(Buttons, ButtonsAdmin)
admin_site.register(Messages, MessagesAdmin)
admin_site.register(Lists, ListsAdmin)
admin_site.register(ListTitles, ListTitlesAdmin)
admin_site.register(FlowerType, FlowerTypeAdmin)
admin_site.register(BouquetType, BouquetTypeAdmin)
admin_site.register(FlowerSubtype, FlowerSubtypeAdmin)
admin_site.register(FlowerColor, FlowerColorAdmin)