from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
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
      return redirect('index')  # Redirect to a homepage or dashboard
    else:
      # Add error if authentication fails
      return redirect('user-choice')
  return render(request,'login-page.html')
def user_choice(request):
  return render(request,'user-choice.html')
def worker_signup(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    conformpassword = request.POST.get('conformpassword')

    user = User.objects.create(
        username=email,
        email=email,
        password=password
    )
    if user is not None:
      login(request, user)
      return redirect('index')
    else:
      return redirect('worker-home.html')
    
  return render(request,'worker-signup.html')
def logout_view(request):
  logout(request)
  return redirect('login-page')
