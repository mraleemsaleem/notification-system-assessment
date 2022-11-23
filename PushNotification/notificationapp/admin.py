from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('category_name',)
admin.site.register(Category, CategoryAdmin)

class ChannelAdmin(admin.ModelAdmin):
    model = ChannelType
    list_display = ('channel_name',)
admin.site.register(ChannelType, ChannelAdmin)

class LogHistoryAdmin(admin.ModelAdmin):
    model = LogHistory
    list_display = ('id','user','category','channell', 'message', 'send_data')

admin.site.register(LogHistory, LogHistoryAdmin)

class UserAdminDjango(admin.ModelAdmin):
    model = User
    list_display = ('username','Channel', 'category')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['email'].disabled = True

        return form

    def Channel(self, obj):
        return ", ".join([p.channel_name for p in obj.channell.all()])
admin.site.register(User, UserAdminDjango)


