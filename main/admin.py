from django.contrib import admin
from . import models
# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(models.Slider, SliderAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Services, ServiceAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display=('title',)
admin.site.register(models.Page, PageAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display=('question',)
admin.site.register(models.FAQ, FAQAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','subject','send_time')
admin.site.register(models.Contact, ContactAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Gallery, GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(models.GalleryImage, GalleryImageAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_editable=('max_member',)
    list_display=('title','price','max_member','validity_days')
admin.site.register(models.Subscription, SubscriptionAdmin)

class SubscriptionFeatureAdmin(admin.ModelAdmin):
    list_display=('title','subplan')
    def subplan(self,obj):
        return "|".join([sub.title for sub in obj.subs.all()])
admin.site.register(models.SubscriptionFeature, SubscriptionFeatureAdmin)


class PackageDiscountAdmin(admin.ModelAdmin):
    list_display=('subs','total_months','total_discount')
admin.site.register(models.PackageDiscount, PackageDiscountAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display=('user','image_tag','mobile')
admin.site.register(models.Subscriber, SubscriberAdmin)

class SubscriberPlanAdmin(admin.ModelAdmin):
    list_display=('user','plan','price','reg_date')
admin.site.register(models.SubscriberPlan, SubscriberPlanAdmin)

class TrainerAdmin(admin.ModelAdmin):
    list_editable=('is_active',)
    list_display=('full_name','mobile','image_tag','is_active')
admin.site.register(models.Trainer, TrainerAdmin)

class NotifyAdmin(admin.ModelAdmin):
    list_display=('notifydetail','read_by_user','read_by_trainer',)
admin.site.register(models.Notify,NotifyAdmin)

class NotifUserStatusAdmin(admin.ModelAdmin):
    list_display=('notif','user','status',)
admin.site.register(models.NotifUserStatus, NotifUserStatusAdmin)

class AssignSubscriberAdmin(admin.ModelAdmin):
    list_display=('trainer','user')
admin.site.register(models.AssignSubscriber, AssignSubscriberAdmin)
 
class AchievementAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Achievement, AchievementAdmin)