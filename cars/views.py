from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.context_processors import csrf
from .models import Info
from .forms import InfoForm
from django import forms
from django.contrib import messages
import pandas as pd
import json


def demo(request):
    return render(request, 'cars/help.html')


def index(request):
    return render(request, 'cars/index.html')


def sign_in(request):
    return render(request, 'cars/sign_in.html')


def register(request):
    return render(request, 'cars/register.html')


def forget(request):
    return render(request, 'cars/forget.html')


def signing_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    # print(i.first_name, i.last_name, i.email, i.password)
    data = Info.objects.all()
    for i in data:
        if (email == i.email and password == i.password):
            return render(request, 'cars/index.html')
    else:
        return render(request, 'cars/register.html')


def forget_in(request):
    import smtplib as sm
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    # fetching receiver ID and name
    email = request.POST.get('email')
    # print(i.first_name, i.last_name, i.email, i.password)
    data = Info.objects.all()
    for i in data:
        print(i.email)
        if(email == i.email):
            rID = email
            uName = i.first_name
            password = i.password
    sID = "deltashadow16@gmail.com"
    msg = MIMEMultipart()

    message = "Hi "+uName+"\nWe get a request to remind you the password of your C@RS for this mail id\nSo here is your password - " + password

    # setup the parameters of the message
    msg['From'] = sID
    msg['To'] = rID
    msg['Subject'] = "Password reset"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    server = sm.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login("deltashadow16@gmail.com", "12345!@#$%")

    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    return render(request, 'cars/sign_in.html')


def register_in(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    Inf = Info.objects.all()
    z = 0
    for i in Inf:
        print(i.email)
        if i.email == email:
            z += 1
            print("email already exist")
            messages.error(request, "form is not valid")
            break
    if z>0:
        return render(request, 'cars/register.html')

    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            info = Info(first_name=first_name, last_name=last_name, email=email, password=password)
            info.save()
        else:
            print("    ")
    return render(request, 'cars/sign_in.html')



def search(request):
    return render(request, 'cars/search.html')



def search_in(request):

    df_u = pd.read_csv(r'C:/Users/sanas/Desktop/Untitled Folder/New folder/finalcar.csv')

    output = []

    fuel = request.POST.getlist('fuel')  # fuel_type
    bdy = request.POST.getlist('body')  # body_type
    tra = request.POST.getlist('trans')  # type
    brnd = request.POST.getlist('brand')  # make
    try:
        minr = int(request.POST.get('from'))
    except Exception as e:
        print(e)  # handle your errors
        minr = int('1')  # The Default value when erros comes

    try:
        maxr = int(request.POST.get('to'))
    except Exception as e:
        print(e)  # handle your errors
        maxr = 10000000000

    if fuel == []:
        fuel = ['petrol', 'diesel', 'cng']

    if bdy == []:
        bdy = ['hatchback', 'mpv', 'crossover', 'sedan', 'suv', 'muv']

    if tra == []:
        tra = ['manual', 'automatic', 'amt', 'dct', 'cvt']

    if brnd == []:
        brnd = ['datsun', 'ford', 'honda', 'hyundai', 'isuzu', 'jeep', 'kia','mahindra', 'maruti suzuki', 'maruti suzuki r', 'mg', 'nissan','renault', 'skoda', 'tata', 'toyota', 'volkswagen']


    df = df_u[df_u['make'].isin(brnd) & df_u['fuel_type'].isin(fuel) & df_u['type'].isin(tra) & df_u['body_type'].isin(bdy)]
    df2 = df.loc[df_u['price'] > minr]
    df3 = df2.loc[df_u['price'] < maxr]

    # a = df3.groupby(['Link', 'image_link'])['image_link'].unique()
    a = df3.groupby(['Link', 'image_link', 'make', 'model', 'fuel_type', 'type', 'body_type', 'price', 'Variant'])['image_link'].unique()
    b = pd.DataFrame(a)
    b = b.drop('image_link', axis=1)
    b = b.sort_values(by='price', ascending=True)

    json_records = b.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'cars/result.html', context)

def help(request):
    return render(request, 'cars/help.html')

def feedback(request):
    return render(request, 'cars/feedback.html')

def contact_us(request):
    return render(request, 'cars/contact_us.html')

def hatchback(request):
    return render(request, 'cars/hatchback.html')

def sedan(request):
    return render(request, 'cars/sedan.html')

def mpv(request):
    return render(request, 'cars/mpv.html')

def muv(request):
    return render(request, 'cars/muv.html')

def suv(request):
    return render(request, 'cars/suv.html')

def crossover(request):
    return render(request, 'cars/crossover.html')

def amt(request):
    return render(request, 'cars/amt.html')

def cvt(request):
    return render(request, 'cars/cvt.html')

def auto(request):
    return render(request, 'cars/auto.html')