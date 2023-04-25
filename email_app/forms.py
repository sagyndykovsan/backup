from django import forms
from .models import ContactEmail


class ContactEmailForm(forms.ModelForm):
    """Формs Подписки на email """

    class Meta:
        model = ContactEmail
        fields = ("email",)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control bg-light border-light w-100 py-3 ps-4 pe-5",
                                             "placeholder": "Ваш email"})
        }

        labels = {
            'email': ''
        }
