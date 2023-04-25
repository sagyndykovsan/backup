from django.views.generic import CreateView
from .models import ContactEmail
from .forms import ContactEmailForm


# Create your views here.
class ContactView(CreateView):
    model = ContactEmail
    form_class = ContactEmailForm
    success_url = "/"

    # def post(self, request):
    #     request.POST['email']
