from django.shortcuts import render
from .forms import *
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.core.validators import validate_email, ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


# Create your views here.
# home page to select if user wants to sign up as seller or buyer
def home(request):
    return render(request, 'home.html', {'buyer': 'buyer', 'seller': 'seller'})

# actual view for the sign up
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        x = self.kwargs.get('slug')
        # checking the url to know if user has selected the seller page or buyer page
        if x == 'seller':
            self.object.purpose = x
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('account:login'))
        elif x == 'buyer':
            self.object.purpose = x
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('account:login'))

        return super(SignUpView, self).form_valid(form)

# login view
class LoginHelpView(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
