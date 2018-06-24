from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.username
    def __unicode__(self):
        return self.username
    class Meta:
        verbose_name='User'
        verbose_name_plural='User'

class Customer(models.Model):
    name=models.CharField(max_length=50,unique=True,verbose_name='名称')
    address=models.CharField(max_length=100,verbose_name='通讯地址')
    website=models.URLField(null=True,blank=True,verbose_name='公司网站')
    is_trade=models.BooleanField(default=False,verbose_name='交易客户')
    taxcode=models.CharField(max_length=100,null=True,blank=True,verbose_name='税号')
    taxaddress=models.CharField(max_length=100,null=True,blank=True,verbose_name='单位地址')
    taxtele=models.CharField(max_length=50,null=True,blank=True,verbose_name='电话号码')
    taxbank=models.CharField(max_length=100,null=True,blank=True,verbose_name='开户行')
    taxbankcode=models.CharField(max_length=100,null=True,blank=True,verbose_name='银行账号')

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='客户'
        verbose_name_plural='客户'
