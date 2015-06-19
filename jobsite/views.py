
from django.template import RequestContext
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import render
from jobsite.forms import UserDataForm,JobDataForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from jobsite.models import Jobs,Apply



from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import hashlib, datetime, random
from django.utils import timezone
from forms import SignupForm
from models import User

def signin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('signin.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/not_active/')
    return HttpResponseRedirect('/invalid/')

def not_active(request):
    return render_to_response('not_active.html')

def dashboard(request):
    user = request.user
    args = {'user': user}
    return render_to_response('dashboard.html',args)

def invalid(request):
    return render_to_response('invalid.html')

def signout(request):
    auth.logout(request)
    return render_to_response('signout.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            role=form.cleaned_data['role'],
            password=form.cleaned_data['password'],
            )
            return HttpResponseRedirect('/registered/')
    else:
        form= SignupForm()
    return render(request,'signup.html',{'form':form},context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('registered.html')


def home(request,job_id):
 if request.user:
  job=Jobs.objects.get(id=job_id)
  
  if request.method == "POST":
    form = UserDataForm(request.POST)
    if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
        form.save(commit=False)
     
            
           
    return redirect('/home')
  else:
      form = UserDataForm()




  return render_to_response("job.html",{'job':job,'form' :form}, context_instance=RequestContext(request))



def post_job(request):
 

  if request.method == "POST" :
   if request.user.role=='1':
    form = JobDataForm(request.POST)
    if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
        form.save()
      
      
            
           
    return redirect('/home')
  else:
      form = JobDataForm()




  return render_to_response("job_post.html",{'form' :form}, context_instance=RequestContext(request))

def jobs(request):
  job=Jobs.objects.all()
  return render_to_response("home.html",{'job_detail':job})

def employer(request):
 if request.user.role=='1':  
  appliers=Apply.objects.all()
 return render_to_response("apply.html",{"apply":appliers})

def search_titles(request):
    if request.POST:
        search_text = request.POST['search_text']
    else:
        search_text = ''
    articles = Jobs.objects.filter(title__contains=search_text)
    return render(request, 'ajax_search.html', {'articles': articles})