from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy
from django.urls import resolve
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.conf import settings
from django.core.exceptions import ValidationError


# Create your views here.

# password changing view
class PasswordsChange(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'seller/password.html'
    success_url = reverse_lazy('seller:seller_home')


# this is for the contact form
def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        send_mail('Contact form',
                  message,
                  email,
                  [settings.EMAIL_HOST_USER],
                  fail_silently=False
                  )
        return HttpResponseRedirect(reverse_lazy('seller:index'))
    ctx = Contactform()
    return render(request, 'seller/contactform.html', {'form': ctx})


# seller property creation view
class SellerCreate(LoginRequiredMixin, generic.CreateView):
    form_class = SellerForm
    template_name = 'seller/sellercreate.html'
    success_url = reverse_lazy('seller:redirect')
    login_url = 'account:login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.by = self.request.user
        self.object.save()
        return super(SellerCreate, self).form_valid(form)


# redirecting user to this view after creation of property to set the approval instance of the particular property to pending
class ApprovalView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('seller:seller_home')

    def get(self, request, *args, **kwargs):
        x = SellerProperty.objects.count()
        p = SellerProperty.objects.all()
        Approve.objects.create(request_approval='pending', approval_id=p[0].id)
        return super().get(request, *args, **kwargs)


# seller list of property
class SellerListSold(generic.ListView, LoginRequiredMixin):
    model = Approve
    template_name = 'seller/list_sold_property.html'
    context_object_name = 'sold_list'

    def get_queryset(self):
        print(SellerProperty.objects)
        current_url = resolve(self.request.path_info).url_name
        return Approve.objects.filter(request_approval=current_url, approval__by=self.request.user).order_by(
            '-approval__timestamp')

    def get_context_data(self, *args, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        ctx = super(SellerListSold, self).get_context_data(*args, **kwargs)
        ctx['dynamic'] = current_url
        return ctx


# seller property home
class SellerHome(generic.TemplateView, LoginRequiredMixin):
    template_name = 'seller/seller_extension.html'


# buyers home page
class BuyerHome(generic.TemplateView, LoginRequiredMixin):
    template_name = 'seller/buyer_home.html'


# buyer list of property
class BuyerListPropertiesHouese(LoginRequiredMixin, generic.ListView):
    model = Approve
    template_name = 'seller/list_buyer_property.html'
    context_object_name = 'buyer_list'

    def get_queryset(self):
        current_url = resolve(self.request.path_info).url_name
        if current_url == 'rent':
            return Approve.objects.filter(request_approval='Approve', approval__purpose__iexact=current_url).order_by(
                '-approval__timestamp')
        else:
            return Approve.objects.filter(request_approval='Approve', approval__type__iexact=current_url).order_by(
                '-approval__timestamp')


# details of property in seller interface
class DetailProperty(LoginRequiredMixin, generic.DetailView):
    model = SellerProperty
    template_name = 'seller/detail_property.html'
    context_object_name = 'detail'


# details of property in buyers interface
class DetailProperty1(LoginRequiredMixin, generic.DetailView):
    model = SellerProperty
    template_name = 'seller/detail_property_buyer.html'
    context_object_name = 'detail'
