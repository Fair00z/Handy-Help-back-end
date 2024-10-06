import calendar
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Worker_Detail,Worker_Dashboard,Worker,Client,Comment,Client_Detail,Client_Dashboard,Job_post
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.base import ContentFile

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

  if request.POST:
    edit_name = request.POST.get('name')
    edit_skill = request.POST.get('skill')
    edit_district = request.POST.get('district')
    edit_profile = request.FILES.get('profile-img')

    detail.name = edit_name
    detail.skill = edit_skill
    detail.district = edit_district
    if edit_profile:
      detail.profile_img = edit_profile
    detail.save()
    return redirect('worker-dashboard')
  context = {
    'username':user.username,
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
    if request.POST:
      work_img = request.FILES.get('work-img')
      work_name = request.POST.get('work-name')
      phone = request.POST.get('phone')
      address = request.POST.get('address')
      work_location = request.POST.get('work-location')
      description = request.POST.get('description')
      client = Client.objects.get(user=user)

      def resize_image(image_path,size=(150, 150)):
    # Open the uploaded image
        with Image.open(image_path) as img:
            # Maintain aspect ratio by using thumbnail method
            img.thumbnail(size, Image.Resampling.LANCZOS)
            
            # Create a new image with the desired size and a white background
            new_img = ImageOps.pad(img, size, method=Image.Resampling.LANCZOS, color=(255, 255, 255))
            # Save the resized image
            buffer = BytesIO()
            new_img.save(buffer, format='JPEG',quality=100) 
            image_file_name = image_path.name
            return ContentFile(buffer.getvalue(), name=image_file_name)

      img = resize_image(work_img)

      Job_post.objects.create(
        work_name = work_name,
        phone = phone,
        address = address,
        work_location = work_location,
        description =description,
        client = client,
        work_img = work_img,
        thumbnail = img
      )
      return redirect('index') 
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
  
def find_jobs(request):
  user = request.user
  if hasattr(user,'worker'):
    jobs = Job_post.objects.all()
    context = {
      'jobs':jobs
    }
    return  render(request,'find-jobs.html',context)
  else:
    return  redirect('index')
