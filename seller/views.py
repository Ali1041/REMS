from django.shortcuts import render
from .forms import *
from .models import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import resolve
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordChangeView,PasswordChangeForm

from django.conf import settings
# Create your views here.


class PasswordsChange(LoginRequiredMixin,PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'seller/password.html'
    success_url = reverse_lazy('seller:seller_home')

def index(request):
    if request.method=='POST':
        print('here')
        message=request.POST['message']
        email=request.POST['email']
        print(email)
        send_mail('Contact form',
                  message,
                  email,
                  [settings.EMAIL_HOST_USER],
                  fail_silently=False
        )
        return HttpResponseRedirect(reverse_lazy('seller:index'))
    ctx=Contactform()
    return render(request,'seller/contactform.html',{'form':ctx})

class SellerCreate(generic.CreateView, LoginRequiredMixin):
    form_class = SellerForm
    template_name = 'seller/sellercreate.html'
    success_url = reverse_lazy('seller:redirect')

    # def post(self, request, *args, **kwargs):
    #     self.object=self.request.POST
    #     print(Approve.objects.all())
    #     print(Approve.objects.count())
    #     print(Approve.objects.filter(approval_id=2))
    #     x=SellerProperty.objects.get(title__iexact=self.object['title'],address__iexact=self.object['address'])
    #     print(x)
        # Approve.objects.create()


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.by = self.request.user
        self.object.save()
        # print('here')
        # x=SellerProperty.objects.get(title__iexact=self.object['title'],address__iexact=self.object['address'])
        # print(x)
        return super(SellerCreate, self).form_valid(form)

class ApprovalView(generic.RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('seller:seller_home')

    def get(self, request, *args, **kwargs):
        x = SellerProperty.objects.count()
        # print(SellerProperty.objects.all())
        p=SellerProperty.objects.all()
        # print(p[x-1].id,p[x-1])
        # print(x)
        # y=x-1
        # print(y)
        print(Approve.objects.create(request_approval='pending', approval_id=p[x-1].id))
        Approve.objects.create(request_approval='pending', approval_id=p[x-1].id)
        return super().get(request,*args,**kwargs)
#
# class SellerList(generic.ListView, LoginRequiredMixin):
#     model = Approve
#     template_name = 'seller/detail_property_buyer.html'
#     context_object_name = 'approve_list'
#
#     def get_queryset(self):
#         x = Approve.objects.filter(approval__by=self.request.user)
#         for i in range(len(x)):
#             if x[i].request_approval == 'Approve':
#                 return Approve.objects.filter(request_approval=x[i].request_approval)
#
#
# class SellerListReject(generic.ListView, LoginRequiredMixin):
#     model = Approve
#     template_name = 'seller/password.html'
#     context_object_name = 'reject_list'
#
#     def get_queryset(self):
#         x = Approve.objects.filter(approval__by=self.request.user)
#         for i in range(len(x)):
#             print(x[i])
#             if x[i].request_approval == 'Reject':
#                 return Approve.objects.filter(request_approval=x[i].request_approval)


class SellerListSold(generic.ListView, LoginRequiredMixin):
    model = Approve
    template_name = 'seller/list_sold_property.html'
    context_object_name = 'sold_list'

    def get_queryset(self):
        current_url=resolve(self.request.path_info).url_name
        return Approve.objects.filter(request_approval=current_url,approval__by=self.request.user)

    def get_context_data(self, *args ,**kwargs):
        current_url=resolve(self.request.path_info).url_name
        ctx=super(SellerListSold, self).get_context_data(*args,**kwargs)
        ctx['dynamic']=current_url
        return ctx


class SellerHome(generic.TemplateView, LoginRequiredMixin):
    template_name = 'seller/seller_extension.html'


class BuyerHome(generic.TemplateView, LoginRequiredMixin):
    template_name = 'seller/buyer_home.html'


class BuyerListPropertiesHouese(LoginRequiredMixin, generic.ListView):
    model = Approve
    template_name = 'seller/list_buyer_property.html'
    context_object_name = 'buyer_list'

    def get_queryset(self):
        current_url = resolve(self.request.path_info).url_name
        if current_url=='rent':
            return Approve.objects.filter(request_approval='Approve', approval__purpose__iexact=current_url)
        else:
            return Approve.objects.filter(request_approval='Approve', approval__type__iexact=current_url)

class DetailProperty(LoginRequiredMixin,generic.DetailView):
    model = SellerProperty
    template_name = 'seller/detail_property.html'
    context_object_name = 'detail'

class DetailProperty1(LoginRequiredMixin,generic.DetailView):
    model = SellerProperty
    template_name = 'seller/detail_property_buyer.html'
    context_object_name = 'detail'
