from django import forms

class NameForm(forms.Form):
    Phone = forms.CharField(label='Your Phone.no', max_length=100)
    Pwd = forms.CharField(label='Your Pwd', max_length=100)

class MailForm(forms.Form):
    msg=forms.CharField(label='Your Message',widget=forms.Textarea)
