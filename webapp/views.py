from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .form import loginPage


def welcome(request):
    if request.method=="GET":
        output = (request.GET.get('user'))
    
    url ="/welcome/?user={}".format(output)
    data ={
        'img3':'/static/images/pic3.jpg',
        'img2':'/static/images/pic2.jpg',
        'img':'/static/images/pic1.jpg',
        'heading':'Django',
        'title' : "Front End Django Practice",
        'h3': 'gives Detailed view for traffic and visits on the web application and bandwidth details. It also also gives Awesome UI for woking on it. Learning Django is preferred to be in one week with full devotion and practices.',
        'h1' : '''Django is a Python-based web framework that promotes rapid development and clean, reusable code. It follows the model-view-template (MVT) architectural pattern and provides numerous built-in features, such as an ORM for database interactions, URL routing, authentication, and templating. Django's emphasis on DRY and explicitness helps developers create robust web applications efficiently.''',
        'courses':['C++ Programming' , 'Python GUI' , 'Django WebApp'],
        'appli':'''Django, a popular Python web framework, offers several key features that contribute to its effectiveness and efficiency in web development: \n
    
    
These key features, among others, make Django a powerful framework for building robust, scalable, and secure web applications with ease.''',
        'h1_new':"Related Work offered",
        'my_det':[{'Name':"Muhammad Shariq Shafiq" , 'Phone':"03074322911"},
        {'Name':"Muhammad Shafiq" , 'Phone':"03074322911"},
        {'Name':"Muhammad Mujtaba" , 'Phone':"03074322911"}],
        'users':output,
        'client': url
    }
    return render(request, "welcome.html" , data)

def Home(request):
    login = loginPage()
    data={'Form':login}
    try:
        if request.method=="POST":
            uname = (request.POST.get('username'))
            password = (request.POST.get('password'))
            final = uname   
        data={
            'pass':password,
            'user':final
        }
        
        url ="/welcome/?user={}".format(final)
        
        return HttpResponseRedirect("/welcome/?user={}".format(final))

    except:
        pass
    return render(request , "index.html" , data)

def calculator(request):
    c=0
    n1 =0
    n2 =0
    try:
        if request.method=="POST":
            n1 = eval(request.POST.get('val1'))
            n2 = eval(request.POST.get('val2'))
            opr = (request.POST.get('opr'))
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
    except:
        c = 'Invalid entry or Operator ...'
    
    data = {
        'title': "Calculator in Django By M.S",
        'result':c,
        'n1':n1,
        'n2':n2
    }
    
    return render(request , "calculator.html" , data)

def marksheet(request):
    if request.method=="POST":
        sname = (request.POST.get('name'))
        faname = (request.POST.get('fname'))
        sn1 = eval(request.POST.get('val1'))
        sn2 = eval(request.POST.get('val2'))
        sn3 = eval(request.POST.get('val3'))
        sn4 = eval(request.POST.get('val4'))
        sn5 = eval(request.POST.get('val5'))
        obt = sn1 + sn2 + sn3 + sn4 + sn5
        perc = (obt / 500) * 100
        if perc >= 90:
            grade = "A+"
        elif perc >= 80 and perc <89:
            grade = "A"
        elif perc >= 70 and perc <79:
            grade = "B"
        elif perc >= 50 and perc < 69:
            grade = "C"
        else:
            grade ="Fail"
        data ={
                'title' : "Marksheet in Django",
                'Name' : sname,
                'Fname' : faname,
                'obtain' : obt,
                'total' : 500,
                'percentage' : perc,
                'Grade' : grade
        }
        print(data)
        return render(request , "marksheet.html" , data)
    return render(request , "marksheet.html" )
        
        
def contact(request): 
    data1 ={
        'img':'https://e0.pxfuel.com/wallpapers/898/129/desktop-wallpaper-cool-boy-boy-pic.jpg',
        'title' : "Contact Django Practice",
        'h1' : "Salam from Muhammad Shariq",
        'courses':['C++ Programming' , 'Python GUI' , 'Django WebApp'],
        'h1_new':"Related Work offered",
        'my_det':[{'Name':"Muhammad Shariq Shafiq" , 'Phone':"03074322911"},
        {'Name':"Muhammad Shafiq" , 'Phone':"03074322911"},
        {'Name':"Muhammad Mujtaba" , 'Phone':"03074322911"}]
        
    }
    return render(request , "contact.html" , data1)


def about(request):
    data ={
        'img':'https://e0.pxfuel.com/wallpapers/898/129/desktop-wallpaper-cool-boy-boy-pic.jpg',
        'title' : "About Django Practice",
        'h1' : "Salam from Muhammad Shariq",
        'courses':['C++ Programming' , 'Python GUI' , 'Django WebApp'],
        'h1_new':"Related Work offered",
        'my_det':[{'Name':"Muhammad Shariq Shafiq" , 'Phone':"03074322911"},
        {'Name':"Muhammad Shafiq" , 'Phone':"03074322911"},
        {'Name':"Muhammad Mujtaba" , 'Phone':"03074322911"}]
        
    }
    return render(request , "about.html" , data)
    
def courses(request):
    return HttpResponse('This is Django course')
    
def courseDetails(request , cid):
    return HttpResponse(cid)