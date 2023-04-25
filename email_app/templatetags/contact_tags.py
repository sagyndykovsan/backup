from django import template
from email_app.forms import ContactEmailForm

register = template.Library()


@register.inclusion_tag("form.html")
def contact_form():
    return {"contact_form": ContactEmailForm()}
