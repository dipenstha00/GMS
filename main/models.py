from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Slider/banner
class Slider(models.Model):
    img=models.ImageField(upload_to="sliders/")
    alt_text = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural='Slider'
    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80px">'  % (self.img.url))

class Services(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to="services/")
    
    class Meta:
        verbose_name_plural='Services'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80px">'  % (self.img.url))


class Page(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    subject=models.TextField()
    message=models.TextField()
    send_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to="gallery/")

    class Meta:
        verbose_name_plural='Gallery'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80px">'  % (self.img.url))

class GalleryImage(models.Model):
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE,null=True)
    alt_text=models.CharField(max_length=150)
    img=models.ImageField(upload_to="gallery_imgs/")

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80px">'  % (self.img.url))


class Subscription(models.Model):
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    max_member=models.IntegerField(null=True)
    validity_days=models.IntegerField(null=True)
    def __str__(self):
        return self.title

class SubscriptionFeature(models.Model):
    # subs=models.ForeignKey(Subscription,on_delete=models.CASCADE)
    subs = models.ManyToManyField(Subscription)
    title=models.CharField(max_length=150)

    def __str__(self):
        return self.title

class PackageDiscount(models.Model):
    subs=models.ForeignKey(Subscription,on_delete=models.CASCADE,null=True)
    total_months=models.IntegerField()
    total_discount=models.IntegerField()

    def __str__(self):
        return str(self.total_months)

class Subscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    img=models.ImageField(upload_to="subs/")

    def __str__(self):
        return str(self.user)

    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % (self.img.url))
        else:
            return 'no-image'
@receiver(post_save, sender=User)
def create_subscriber(sender,instance,created, **kwargs):
    if created:
        Subscriber.objects.create(user=instance)


class SubscriberPlan(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    plan=models.ForeignKey(Subscription,on_delete=models.CASCADE)
    price=models.CharField(max_length=50)
    reg_date=models.DateField(auto_now_add=True,null=True)

class Trainer(models.Model):
    full_name = models.CharField(max_length=150)
    username=models.CharField(max_length=150,null=True)
    password=models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=50)
    address = models.TextField()
    is_active=models.BooleanField(default=False)
    detail = models.TextField()
    image = models.ImageField(upload_to='trainers/')
    instagram=models.CharField(max_length=300,null=True)
    twitter=models.CharField(max_length=300,null=True)
    youtube=models.CharField(max_length=300,null=True)
    salary=models.IntegerField(null=True)

    def __str__(self):
        return self.full_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="80">' % self.image.url)

class Notify(models.Model):
    notifydetail = models.TextField()
    read_by_user=models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    read_by_trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE, null=True,blank=True)
    
    class Meta:
        verbose_name_plural='Notification'

    def __str__(self):
        return str(self.notifydetail)
# Mark as read notification for user
class NotifUserStatus(models.Model):
    notif=models.ForeignKey(Notify, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

#Assigning Subscriber to trainer
class AssignSubscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    

class Achievement(models.Model):
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    detail=models.TextField()
    img=models.ImageField(upload_to='achievements/')

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80>' % self.img.url)
        else:
            return 'no-image'
    
    class Meta:
        verbose_name_plural="Trainer's Achievements"


class TrainerSalary(models.Model):
    trainer= models.ForeignKey(Trainer, on_delete=models.CASCADE)
    amount=models.IntegerField()
    date_given=models.DateField()
    remarks=models.TextField(null=True)

    def __str__(self):
        return self.trainer.full_name
    
    class Meta:
        verbose_name_plural="Trainer's Salary"

