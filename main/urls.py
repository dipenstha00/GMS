from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('package/',views.package,name='package'),
    path('contact/',views.contact,name='contact'),
    path('page/<int:id>',views.page_detail,name='page'),
    path('faq/',views.faq_list,name='faq'),
    # Gallery
    path('gallery/',views.gallery,name='gallery'),
    path('gallerydetail/<int:id>',views.gallery_detail,name='gallerydetail'),
    path('accounts/signup/',views.signup, name='signup'),
    path('checkout/<int:plan_id>',views.checkout,name='checkout'),
    path('checkout_session/<int:plan_id>',views.checkout_session,name='checkout_session'),
    # Payment
    path('pay_success',views.pay_success,name='pay_success'),
    path('pay_cancel',views.pay_cancel,name='pay_cancel'),
    # User
    path('dashboard/',views.userdashboard,name='dashboard'),
    path('updateprofile/',views.update_profile,name='udpateprofile'),
    path('success',views.password_changed,name='success'),
    # Trainer
    path('trainerlogin/',views.trainerlogin,name='trainerlogin'),
    path('trainerlogout/',views.trainerlogout,name='trainerlogout'),
    path('trainerdashboard/',views.trainerdashboard,name='trainerdashboard'),
    path('trainerprofile/',views.trainerprofile,name='trainerprofile'),
    # Notification
    path('notify/',views.notify,name='notify'),
    path('get_notifs',views.get_notifs,name='get_notifs'),
    path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)