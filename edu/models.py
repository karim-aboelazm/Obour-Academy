from django.db import models
from random import randint
from dateutil.relativedelta import relativedelta
import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(_('full_name'),max_length=255)
    image = models.ImageField(_('image'),upload_to='student_images/')
    phone_number = models.CharField(_('phone_number'),max_length=15, blank=True, null=True)
    join_on = models.DateTimeField(_('join_on'),auto_now_add=True)
    objective = models.TextField(blank=True,null=True)
    data_of_birth = models.DateField(blank=True,null=True)
    age = models.CharField(max_length=10,blank=True,null=True)
    privacy = models.CharField(max_length=30,blank=True,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    study_at = models.CharField(max_length=50,default="Obour Institutes")
    module = models.CharField(max_length=30,blank=True,null=True)
    
    class Meta:
        verbose_name_plural = _('Student')
    def save(self, *args, **kwargs):
        self.age = str(relativedelta(datetime.date.today(),self.data_of_birth).years)
        super(Student, self).save(*args, **kwargs)
    def __str__(self):
        return self.full_name

class Offer(models.Model):
    title = models.CharField(_('title'),max_length=150)
    description = models.TextField(_('description'))
    disvalue = models.IntegerField(_('disvalue'))
    class Meta:
        verbose_name_plural = _('Offer')
    def __str__(self):
        return self.title

class WhoGetOffer(models.Model):
    full_name = models.CharField(_('full_name'),max_length=255)
    email     = models.EmailField()
    phone     = models.CharField(max_length=15)
    coupon    = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = _('WhoGetOffer')
        
    def save(self, *args, **kwargs):
        coup = "Atec_"
        for i in range(8):
            coup+=str(randint(0,i+10))
        self.coupon = coup
        super(WhoGetOffer, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.full_name} has an discount coupon : {self.coupon}"

class Course(models.Model):
    title = models.CharField(_('title'),max_length=150)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'),upload_to='course_images/')
    price = models.IntegerField(_('price'),default=0)
    discound = models.IntegerField(_('discound'),default=0)
    price_after_discount = property(lambda self: self.price - (self.price * self.discound / 100))
    instructor = models.CharField(_('instructor'),max_length=150)
    class Meta:
        verbose_name_plural = _('Course')
    def __str__(self):
        return self.title

class Galary(models.Model):
    image = models.ImageField(_('image'),upload_to='galary_images/')
    class Meta:
        verbose_name_plural = _('Galary')
    def __str__(self):
        return "Image Number : "+str(self.id)