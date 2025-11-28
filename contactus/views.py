from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactUsForm



# ==================== CONTACT US VIEW ====================
class ContactUsView(FormView):
    template_name = "contactus/contact.html"
    form_class = ContactUsForm
    success_url = reverse_lazy('contact:contact') 

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
