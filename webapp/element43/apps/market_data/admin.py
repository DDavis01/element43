from django.contrib import admin

from apps.market_data.models import UUDIFMessage, OrderMessage

class UUDIFMessageAdmin(admin.ModelAdmin):
    """
    Admin site definition for the UUDIFMessage model.
    """

    list_display = ('key', 'received_dtime', 'is_order')
    list_filter = ('is_order', 'received_dtime')
    search_fields = ('key',)
    date_hierarchy = 'received_dtime'

admin.site.register(UUDIFMessage, UUDIFMessageAdmin)


class OrderMessageAdmin(admin.ModelAdmin):
    """
    Admin site definition for the OrderMessage model.
    """

    list_display = ('generated_at', 'is_bid', 'type_id', 'region_id')
    list_filter = ('is_bid', 'generated_at')
    search_fields = ('message_key', 'uploader_ip_hash')
    date_hierarchy = 'generated_at'

admin.site.register(OrderMessage, OrderMessageAdmin)