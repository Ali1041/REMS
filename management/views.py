from django.shortcuts import render
from seller.models import *
from account.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import resolve
from seller.filter import *
from django.shortcuts import Http404

# Create your views here.
# def request(request):
#     search=SellerPropertyFilter()
#     return render(request,'management/new.html',{'search':search})

def PropertyHome(request):
    if not request.user.is_staff:
        raise Http404
    if request.method == 'GET':
        x = request.GET
        print(x)
        if 'search' in x:
            print('herer')
            result = SellerProperty.objects.all()
            search = SellerPropertyFilter(request.GET, queryset=result)
            result = search.qs
            return render(request, 'management/property_home.html', {'search': search, 'result': result})
        else:
            result=SellerProperty.objects.none()
            search = SellerPropertyFilter(request.GET, queryset=result)
            return render(request, 'management/property_home.html', {'search': search})

    # def get_context_data(self, *args,**kwargs):
    #     ctx=super(PropertyHome, self).get_context_data(*args,**kwargs)
    #     ctx['search']=SellerPropertyFilter()
    #     return ctx


class PropertyList(LoginRequiredMixin, generic.ListView):
    model = SellerProperty
    template_name = 'management/propertyList.html'
    context_object_name = 'list'

    def get_queryset(self):
        if not self.request.user.is_staff:
            raise Http404
        current_url = resolve(self.request.path_info).url_name
        if current_url == 'All':
            return SellerProperty.objects.all()
        else:
            return SellerProperty.objects.filter(approval_seller__request_approval__iexact=current_url)

    def get_context_data(self, *args, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        ctx = super(PropertyList, self).get_context_data(*args, **kwargs)
        ctx['dyno'] = current_url
        ctx['search'] = SellerPropertyFilter()

        return ctx


class PersonList(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'management/personlist.html'
    context_object_name = 'list'

    def get_queryset(self):
        if not self.request.user.is_staff:
            raise Http404
        current_url = resolve(self.request.path_info).url_name
        return User.object.filter(purpose__iexact=current_url)

    def get_context_data(self, *args, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        ctx = super(PersonList, self).get_context_data(*args, **kwargs)
        ctx['dynamic'] = current_url
        # ctx['search']=SellerPropertyFilter()
        return ctx


class TypeProperty(LoginRequiredMixin, generic.ListView):
    model = SellerProperty
    # template_name = 'management/type.html'
    template_name = 'management/propertyList.html'
    context_object_name = 'list'

    def get_queryset(self):
        if not self.request.user.is_staff:
            raise Http404
        current_url = resolve(self.request.path_info).url_name
        return SellerProperty.objects.filter(type__iexact=current_url)

    def get_context_data(self, *args, **kwargs):
        ctx = super(TypeProperty, self).get_context_data(*args, **kwargs)
        ctx['dyno'] = resolve(self.request.path_info).url_name
        # ctx['search']=SellerPropertyFilter()

        return ctx


class AdminApprovalProperty(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('management:All')

    def get(self, request, *args, **kwargs):
        print(self.kwargs.get('pk'))
        y = self.kwargs.get('pk')
        current_url = resolve(self.request.path_info).url_name
        x = Approve.objects.filter(approval_id=y)

        print(x[0].request_approval)
        if x:
            print(current_url)
            x[0].request_approval = current_url.capitalize()
            x[0].save()
            print(x[0].request_approval)
        else:
            Approve.objects.create(request_approval=current_url.capitalize(), approval_id=y)
        # print(x.request_approval)
        return super(AdminApprovalProperty, self).get(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin,generic.DeleteView):
    model = SellerProperty
    template_name = 'management/deleteview.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('management:All')