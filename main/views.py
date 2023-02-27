from django.shortcuts import render,redirect
from .models import *
from . import forms
from django.template.loader import get_template
from django.db.models import Count
from django.core import serializers
from django.http import JsonResponse
import stripe
from datetime import timedelta
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    cards = Services.objects.all()[:3]
    return render(request,'index.html',{'sliders':sliders,'cards':cards})

def package(request):
    package=Subscription.objects.annotate(total_members=Count('subscriberplan__id')).all().order_by('price')
    features=SubscriptionFeature.objects.all()

    return render(request, 'pricing.html',{'package':package,'features':features})


def contact(request):
    return render(request, 'contact.html')

def signup(request):
    msg={}
    if request.method == 'POST':
        form=forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully signed up."
    form=forms.SignUp
    return render(request, 'registration/signup.html',{'form':form,'msg':msg})

def page_detail(request,id):
    page=Page.objects.get(id=id)
    return render(request, 'page.html',{'page':page})

def faq_list(request):
    faq = FAQ.objects.all()
    return render(request, 'faq.html',{'faq':faq})

def contact(request):
    msg={}
    if request.method == 'POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid:
            form.save()
            msg='Form is submitted'
        else:
            msg='Please enter correct valid email'
            return redirect('/contact')
    form=forms.ContactForm
    return render(request,'contact.html',{'form':form,'msg':msg})


def gallery(request):
    gallery=Gallery.objects.all().order_by('-id')
    return render(request,'gallery.html',{'gallery':gallery})

def gallery_detail(request,id):
    gallery=Gallery.objects.get(id=id)
    gallery_images=GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(request, 'gallery_images.html',{'gallery_images':gallery_images,'gallery':gallery})


def checkout(request,plan_id):
    packagedetail=Subscription.objects.get(pk=plan_id)
    plandiscount=PackageDiscount.objects.all()
    return render(request, 'checkout.html',{'plan':packagedetail,'plandiscount':plandiscount})

stripe.api_key = 'sk_test_51Mdxm2SF4roCCIV4qWEkbjexqDzP1FKdBuGvv9yJiaxG7VisvTR77U015xm9srr9jBVtafqU2eEtPYIIP0eFZcLO00KuzHL4IQ'
def checkout_session(request,plan_id):
    plan=Subscription.objects.get(pk=plan_id)
    session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items= [{
      'price_data': {
        'currency': 'inr',
        'product_data': {
          'name': plan.title,
        },
        'unit_amount': plan.price*100,
      },
      'quantity': 1,
    }],
     mode='payment',
    success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
    cancel_url='http://127.0.0.1:8000/pay_cancel',
    client_reference_id=plan_id
    )
    return redirect(session.url,code=303)
from django.core.mail import EmailMessage
def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id=session.client_reference_id
    plan=Subscription.objects.get(pk=plan_id)
    user=request.user
    SubscriberPlan.objects.create(
        plan=plan,
        user=user,
        price=plan.price,
    )
    subject='Order Email'
    html_content=get_template('orderemail.html').render({'title':plan.title})
    from_email='dipensure15@gmail.com'
    msg = EmailMessage(subject,html_content,from_email,['jerry@hotmail.com'])
    msg.content_subtype="html"
    msg.send()
    return render(request,'success.html')

def pay_cancel(request):
    return render(request,'cancel.html')


def userdashboard(request):
    current_plan=SubscriberPlan.objects.get(user=request.user)
    current_trainer=AssignSubscriber.objects.get(user=request.user)
    enddate=current_plan.reg_date+timedelta(days=current_plan.plan.validity_days)
    # achieve=Achievement.objects.all()
    data=Notify.objects.all().order_by('-id')
    notifStatus=False
    jsondata=[]
    totalUnread=0
    for d in data:
        try:
            notifStatusData=NotifUserStatus.objects.get(user=request.user,notif=d)

            if notifStatusData:
                notifStatus=True
        except NotifUserStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1

    return render(request, 'user/dashboard.html',{
        'current_plan':current_plan,
        'current_trainer':current_trainer,
        'totalUnread':totalUnread,
        'enddate' : enddate,
        # 'achieve' : achieve,
    })


def update_profile(request):
    msg=None
    if request.method == 'POST':
        form=forms.ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg='Profile updated succesfully!'
    form=forms.ProfileForm(instance=request.user)
    return render(request, 'user/update-profile.html',{'form':form,'msg':msg})

def password_changed(request):
    return render(request,'registration/password_changed.html')

# Trainer Views
def trainerlogin(request):
    msg=None
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        trainer=Trainer.objects.filter(username=username,password=password).count()
        if trainer > 0:
            trainer=Trainer.objects.filter(username=username,password=password).first()
            request.session['trainerLogin']=True
            request.session['trainerid']=trainer.id
            print(trainer.id)
            return redirect('/trainer_dashboard')
        else:
            msg='Invalid'
    form=forms.TrainerLogin
    return render(request, 'trainer/trainerlogin.html',{'form':form,'msg':msg})

def trainerlogout(request):
    del request.session['trainerLogin']
    return redirect('/trainerlogin')

def trainerdashboard(request):
    return render(request,'trainer/trainer-dashboard.html')

def trainerprofile(request):
    trainer_id=request.session['trainerid']
    trainer=Trainer.objects.get(pk=trainer_id)
    form=forms.TrainerProfileForm(instance=trainer)
    
    return render(request,'trainer/trainer-profile.html',{'form':form,'trainer':trainer})

def notify(request):
    data = Notify.objects.all().order_by('-id')
    return render(request, 'notification.html',{'data':data})

# Get notification
def get_notifs(request):
    data=Notify.objects.all().order_by('-id')
    notifStatus=False
    jsondata=[]
    totalUnread=0
    for d in data:
        try:
            notifStatusData=NotifUserStatus.objects.get(user=request.user,notif=d)

            if notifStatusData:
                notifStatus=True
        except NotifUserStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1
        jsondata.append({
            'pk':d.id,
            'notifydetail':d.notifydetail,
            'notifStatus':notifStatus
        })
    # jsondata=serializers.serialize('json',data)
    return JsonResponse({'data':jsondata,'totalUnread':totalUnread})

# Mark as read by user
def mark_read_notif(request):
    notif=request.GET['notif']
    notif=Notify.objects.get(pk=notif)
    user=request.user
    NotifUserStatus.objects.create(notif=notif,user=user,status=True)
    return JsonResponse({'boolen':True})
