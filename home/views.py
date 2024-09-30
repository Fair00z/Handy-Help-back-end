import calendar
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Worker_Detail,Worker_Dashboard,Worker,Client,Comment,Client_Detail,Client_Dashboard
# Create your views here.

def index(request):
  if request.user.is_authenticated:
    user = request.user
    if hasattr(user, 'worker'):
      return redirect('worker-home')
    else:
      return redirect('client-home')
  else:
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
  current_year = datetime.datetime.now().year
  years = list(range(current_year, current_year - 50, -1))
  months = [(i, calendar.month_name[i]) for i in range(1, 13)]
  date = list(range(31,0,-1))
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    conformpassword = request.POST.get('conformpassword')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    year = request.POST.get('year')
    month = request.POST.get('month')
    day = request.POST.get('date')
    dob = f'{day}/{month}/{year}'
    skill = request.POST.get('skill')
    experience = request.POST.get('experience')
    district = request.POST.get('district')
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
          Worker_Detail.objects.create(
            name = name,
            phone = phone,
            dob = dob,
            skill = skill,
            gender = gender,
            experience = experience,
            district =  district,
            user = request.user
          )
          Worker_Dashboard.objects.create(
            user=user,
            title = name,
          )
          Worker.objects.create(
            user = user
          )
          return redirect('worker-home')
        else:
          return redirect('worker-signup')
      else:
        return render(request,'worker-signup.html',{'pass_error': 'Password did not match'})
  return render(request,'worker-signup.html',{'years': years,'months': months,'dates': date})
def logout_view(request):
  logout(request)
  return redirect('login-page')

@login_required(login_url='/login/')
def worker_home(request):
  user = request.user
  if hasattr(user,'worker'):
    detail = Worker_Detail.objects.get(user=user)
    context = {
      'user_details':detail,
    }
    return render(request,'worker-home.html',context)
  else:
    return redirect('client-home')

@login_required(login_url='/login/')
def client_home(request):
  user = request.user
  if hasattr(user,'client'):
    detail = Client_Detail.objects.get(user=user)
    context = {
      'user_details':detail,
    }
    return render(request,'client-home.html',context)
  else:
    return redirect('worker-home')

def worker_dashboard(request):
  user = request.user
  dashboard, created = Worker_Dashboard.objects.get_or_create(user=user)
  detail = Worker_Detail.objects.get(user=user)
  worker = Worker.objects.get(user=user)
  comments = Comment.objects.filter(worker=worker)
  context = {
    'username':dashboard.title,
    'user_details':detail,
    'comments':comments,
  }
  return render(request,'worker-dashboard.html',context)

def client_dashboard(request):
  user = request.user
  dashboard, created = Client_Dashboard.objects.get_or_create(user=user)
  detail = Client_Detail.objects.get(user=user)
  client = Client.objects.get(user=user)
  comments = Comment.objects.filter(client=client)
  context = {
    'username':dashboard.title,
    'user_details':detail,
    'comments':comments,
  }
  return render(request,'client-dashboard.html',context)

def client_signup(request):
  current_year = datetime.datetime.now().year
  years = list(range(current_year, current_year - 50, -1))
  months = [(i, calendar.month_name[i]) for i in range(1, 13)]
  date = list(range(31,0,-1))
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    conformpassword = request.POST.get('conformpassword')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    year = request.POST.get('year')
    month = request.POST.get('month')
    day = request.POST.get('date')
    dob = f'{day}/{month}/{year}'
    district = request.POST.get('district')

    if User.objects.filter(username=email).exists():
            return render(request, 'client-signup.html', {'error': 'Email already exists'})
    else:
      if password == conformpassword:
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        if user is not None:
          login(request, user)
          Client_Detail.objects.create(
            name = name,
            phone = phone,
            dob = dob,
            gender = gender,
            district =  district,
            user = request.user
          )
          Client_Dashboard.objects.create(
            user=user,
            title = name,
          )
          Client.objects.create(
            user = user
          )
          return redirect('client-home')
        else:
          return redirect('client-signup')
      else:
        return render(request,'client-signup.html',{'pass_error': 'Password did not match'})

  return render(request,'client-signup.html',{'years': years,'months': months,'dates': date})

def job_posting(request):
  user = request.user
  if hasattr(user,'client'):
    return render(request,'job-posting.html')
  else:
    return redirect('index')

def list_workers(request):
  user = request.user
  if hasattr(user,'client'):
    workers = Worker.objects.all()
    context = {
      'workers':workers,
    }
    return  render(request,'workers.html',context)
  else:
    return redirect('index')
