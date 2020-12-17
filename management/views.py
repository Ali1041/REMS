from django.shortcuts import render
from seller.models import *
from account.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import resolve
from seller.filter import *
from django.shortcuts import Http404

# Create your views here.

# filtering functional view for the admin page
def PropertyHome(request):
    if not request.user.is_staff:
        raise Http404
    if request.method == 'GET':
        x = request.GET
        if 'search' in x:
            result = SellerProperty.objects.all()
            search = SellerPropertyFilter(request.GET, queryset=result)
            result = search.qs
            return render(request, 'management/property_home.html', {'search': search, 'result': result})
        else:
            result=SellerProperty.objects.none()
            search = SellerPropertyFilter(request.GET, queryset=result)
            return render(request, 'management/property_home.html', {'search': search})

# property list for admin page
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

# list of users present i.e buyers and sellers list
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
        return ctx

# list of property based on its type
class TypeProperty(LoginRequiredMixin, generic.ListView):
    model = SellerProperty
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

        return ctx

# detail page for approval of property
class AdminApprovalProperty(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('management:All')

    def get(self, request, *args, **kwargs):
        print(self)
        y = self.kwargs.get('pk')
        current_url = resolve(self.request.path_info).url_name
        x = Approve.objects.filter(approval_id=y)

        if x:
            x[0].request_approval = current_url.capitalize()
            x[0].save()
        else:
            Approve.objects.create(request_approval=current_url.capitalize(), approval_id=y)
        return super(AdminApprovalProperty, self).get(request, *args, **kwargs)


# deleting the property from the admin panel
class DeleteView(LoginRequiredMixin,generic.DeleteView):
    model = SellerProperty
    template_name = 'management/deleteview.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('management:All')