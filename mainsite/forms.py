from django import forms
from mainsite.models import Customer
#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label = '用户名 :',max_length = 50)
    password = forms.CharField(label = '密码 :',widget = forms.PasswordInput())

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','address','website','is_trade','taxcode','taxaddress','taxtele','taxbank','taxbankcode']
