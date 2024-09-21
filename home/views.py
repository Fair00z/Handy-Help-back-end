from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  return render(request,'index.html')
def how_it_works(request):
  return render(request,'how-it-works.html')

def about_us(request):
  return render(request,'About-us.html')
def login_page(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=email, password=password)

    if user is not None:
      # Log the user in
      login(request, user)
      return redirect('worker-home')  # Redirect to a homepage or dashboard
    else:
      # Add error if authentication fails
      return redirect('login-page')
  return render(request,'login-page.html')
def user_choice(request):
  return render(request,'user-choice.html')
def worker_signup(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    conformpassword = request.POST.get('conformpassword')

    if User.objects.filter(username=email).exists():
            return render(request, 'worker-signup.html', {'error': 'Email already exists'})
    else:
      if password == conformpassword:
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        if user is not None:
          login(request, user)
          return redirect('worker-home')
        else:
          return redirect('worker-home.html')
      else:
        return render(request,'worker-signup.html',{'pass_error': 'Password did not match'})
  return render(request,'worker-signup.html')
def logout_view(request):
  logout(request)
  return redirect('login-page')

@login_required(login_url='/login/')
def worker_home(request):
  return render(request,'worker-home.html')
