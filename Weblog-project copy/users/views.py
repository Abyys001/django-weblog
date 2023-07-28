from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from rest_framework import mixins

# importing models
from .models import User, Profile
from .forms import UpdateProfileForm, UpdateUserForm

# Create your views here.

def page(request):
    return render(request, './index.html') 


class MyProfile(LoginRequiredMixin, View):
    
    def get(self, request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'users/profile.html', context)

    def post(self, request):
        user_form = UpdateUserForm(
            request.POST,
            instance=request.user
        )
        profile_form = UpdateProfileForm(
            request.POST,
            request.FILE,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Your profile has been updated successfully")

            return redirect('profile')
    
        else: 
            messages.error(request, "Error Updateing Your profile")

            context = {
                'user_form': user_form,
                'profile_form': profile_form,   
            }

            return render(request, 'users/profile.html', context=context)

            