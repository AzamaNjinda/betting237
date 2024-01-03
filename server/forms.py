from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

PAYMENT_CHOICES = [
    ('MTN', 'Mobile Money (MTN)'),
    ('OM', 'Orange Money (OM)'),
]
User = get_user_model()


class UserLoginForm(forms.Form):
    phoneNumber = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'placeholder':'Ex: +1 000 00 0000'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Your password here'}))
    

    def clean(self, *args, **kwargs):
        phoneNumber = self.cleaned_data.get('phoneNumber')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(phoneNumber=phoneNumber, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    phoneNumber = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'placeholder':'Ex: +671 234 567'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Your password here'}))
    cpassword = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Re-enter your same password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'phoneNumber',
            'password',
            'cpassword'
        ]

    def clean(self, *args, **kwargs):
        phoneNumber = self.cleaned_data.get('phoneNumber')
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password != cpassword:
            raise forms.ValidationError("Password must match")
        phoneNumber_qs = User.objects.filter(phone_number=phoneNumber)
        if phoneNumber_qs.exists():
            raise forms.ValidationError(
                "This Phone Number  has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

class PaymentForm(forms.Form):
    phoneNumber = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'placeholder':'Ex: 671 234 567'}))
    amount = forms.IntegerField(required=True,widget=forms.TextInput(attrs={ 'placeholder':'Ex: 5000'}))
    payment_method = forms.ChoiceField(label='Select your Payment Method', choices=PAYMENT_CHOICES, widget=forms.Select(attrs={'class': 'dropdown-toggle', 'id': 'wallet-select', 'data-bs-toggle': 'dropdown', "aria-expanded":"false"}))

    def clean(self, *args, **kwargs):
        phoneNumber = self.cleaned_data.get('phoneNumber')
        amount = self.cleaned_data.get('amount')
        payment_method = self.cleaned_data.get('payment_method')

        return super(PaymentForm, self).clean(*args, **kwargs)
