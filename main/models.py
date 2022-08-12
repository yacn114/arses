from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#offer 
class Offer(models.Model):
    time = models.DateTimeField(_("زمان تخفیف"))
    darsad = models.IntegerField(_("درصد تخفیف"))
    def __str__(self):
        return str(self.darsad)+ "%  " + str(self.time)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'تخفیف ها '
        verbose_name_plural = 'تخفیف ها'
class Product(models.Model):
    NUMBERS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    name = models.CharField(_("اسم محصول"),max_length=255)
    price = models.IntegerField(_("قیمت به تومان"))
    picture = models.ImageField(_("عکس نمایشی"),upload_to='ProductImage/picture')
    picture2 = models.ImageField(_("عکس پیش نمایش"),upload_to='ProductImage/picture2')
    picture3 = models.ImageField(_("عکس جزيیات"),upload_to='ProductImage/picture3')
    picture4 = models.ImageField(_("عکس جزییات"),upload_to='ProductImage/picture4')
    vip = models.CharField(_("محصول ویژه"),max_length=20,default="no",choices=[("no","خیر"),("yes","بله")])
    price_offer = models.ForeignKey(Offer,on_delete = models.CASCADE,blank=True,null=True)
    category = models.ForeignKey("category",on_delete=models.CASCADE)
    star = models.IntegerField(_("امتیاز به ستاره"),choices=NUMBERS)
    caption = models.TextField(_("معرفی جزیَی"),)
    # commentID = models.ForeignKey(comment)
    detail = models.TextField(_("معرفی دقیق"),)
    buyers = models.IntegerField(_("تعداد فروش"),default=0)
    view = models.IntegerField(_("تعداد بازدید"),default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

class Userphone(models.Model):
    phone = models.CharField(max_length=11)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'شماره کاربر‍‍‍'
        verbose_name_plural = '‍شماره کاربر'
class Email(models.Model):
    Email = models.EmailField(blank=False)

# category
class category(models.Model):
    name = models.CharField(_("اسم "),max_length=255)
    image = models.ImageField(_("عکس "),upload_to="category")
    Tpost = models.IntegerField(_("تعداد پست"),default=0)
    # names = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Product",null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = ' دسته بندی ها'
        verbose_name_plural = 'دسته بندی ها'
# image trend 3
class Image_trend_2(models.Model):
    image1 = models.ImageField(_("عکس اولی"),upload_to="main/pic/1")
    image2 = models.ImageField(_("عکس دومی"),upload_to="main/pic/2")
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = ' دو عکس ترند'
        verbose_name_plural = 'دو عکس ترند'

# image_under

class image_u(models.Model):
    image = models.ImageField(_("عکس"),upload_to="main/u")
    def __str__(self):
        return "image"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'عکس پایینی'
        verbose_name_plural = 'عکس پایینی'

# Product


class interest(models.Model):
    id_pro = models.IntegerField()
    id_user = models.IntegerField()
class sabad(models.Model):
    id_pro = models.IntegerField()
    id_user = models.IntegerField()
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
@receiver(post_save,sender=Product)
def add_to_category(sender,instance,created,**kwargs):
    if created:
        b = category.objects.get(id=instance.category.id)
        b.Tpost += 1
        b.save()

@receiver(post_delete,sender=Product)
def delete_category(sender,instance,created,**kwargs):
    b = category.objects.get(id=instance.category.id)
    b.Tpost -= 1
    b.save()
class Brand(models.Model):
    name = models.CharField(_("نام"),max_length=200)
    image = models.ImageField(_("عکس برند"),upload_to="brands")
    

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")

    def __str__(self):
        return self.name
