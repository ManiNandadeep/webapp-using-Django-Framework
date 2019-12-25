from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm


def register(request):
	if request.method=='POST':
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! You are now able to Log in') 
			return redirect('login')
	else:
		form=UserRegistrationForm()
	return render(request,'users/register.html',{'form':form})


#login_required decorator checks whether the user is logged in or not to access the profile 
@login_required
def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST, instance=request.user) #u_form is the instance of UserUpdateFrom() method and instance=request.user helps us to view the user details before modifications
		p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #p_form is the instance of UserProfileForm() method instance=request.user.profile helps us to view the profile of the user before modifications
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your profile has been updated!')	
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)	
	context={
		'u_form':u_form,
		'p_form':p_form
	}

	return render(request,'users/profile.html',context)