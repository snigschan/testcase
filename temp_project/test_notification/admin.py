from django.contrib import admin
from .models import  NotificationPreference  # import all models together



#from django.contrib import admin
from .models import NotificationPreference

@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ('mobile_number',)  # Make sure this is a tuple
    search_fields = ('mobile_number',)
    # ❌ REMOVE any list_filter or list_display entries that include 'is_active'


from .models import CardDetail

@admin.register(CardDetail)
class CardDetailAdmin(admin.ModelAdmin):
    list_display = ( 'card_type', 'last4', 'expiry_month', 'expiry_year')
    search_fields = ('last4',)
