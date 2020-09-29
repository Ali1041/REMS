from django.shortcuts import render
from .forms import *
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home.html', {'buyer': 'buyer', 'seller': 'seller'})


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        x = self.kwargs.get('slug')
        if x == 'seller':
            self.object.purpose = x
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('account:login'))
        elif x == 'buyer':
            self.object.purpose = x
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('account:login'))

        return super(SignUpView, self).form_valid(form)
