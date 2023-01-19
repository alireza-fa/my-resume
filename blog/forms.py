from django import forms

from blog.models import NewsletterSubscribe


class NewsletterSubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscribe
        fields = ('email',)

        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": 'آدرس ایمیل خود را وارد کنید ...'})
        }
