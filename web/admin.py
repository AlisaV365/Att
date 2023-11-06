from django.contrib import admin

from web.models import Suppliers, Product


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city',)
    list_filter = ('city',)
    actions = ["admin_action"]

    """Функция очищающая задолженность перед поставщиком у выбранных объектов"""
    def admin_action(self, request, queryset):
        for obj in queryset:
            obj.products.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'model', 'release_date', 'supplier', 'get_supplier_link',)
    list_filter = ('supplier',)

    """Ссылка на «Поставщика»"""
    def get_supplier_link(self, obj):
        if obj.supplier:
            return "{}".format(obj.supplier.id, obj.supplier.name)
        return "-"

    get_supplier_link.allow_tags = True
    get_supplier_link.short_description = "Поставщик"
    list_display = ('name_product', 'model', 'release_date', 'get_supplier_link',)
