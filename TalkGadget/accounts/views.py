from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from accounts.forms import UserForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect

from . import forms
from .models import UserProfile

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

def editProfile(request):
    form_class = forms.UserProfileForm
    model = UserProfile
    second_form_class = forms.UserForm
    success_url = reverse_lazy("thanks")
    template_name = "accounts/signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class
        return context

    def form_valid(self, form):
        user_form = forms.UserForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_profile = form.save(commit=False)
            user_profile.user_id = user

            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     # If yes, then grab it from the POST form reply
            #     user_profile.profile_pic = request.FILES['profile_pic']

            user_profile.save()
        return redirect(self.success_url)
