from django.http import HttpResponse
from django.shortcuts import render



def welcome(request):
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
        {'Name':"Muhammad Mujtaba" , 'Phone':"03074322911"}]
        
    }
    return render(request, "welcome.html" , data)


def Home(request):
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
        {'Name':"Muhammad Mujtaba" , 'Phone':"03074322911"}]
        
    }
    return render(request, "index.html" , data)


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