from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    ETFO= TopicForm()
    d={'ETFO':ETFO}

    if request.method == 'POST':
        TFDO = TopicForm(request.POST) #topic form data object
        
        if TFDO.is_valid():
            tn= TFDO.cleaned_data['topic_name'] #form -- class attribute 
            print(tn)
            TO = Topic.objects.get_or_create(topic_name = tn)[0]
            TO.save()

            return HttpResponse(str(TFDO.cleaned_data))
        else:
            return HttpResponse('Invalid Data')
    return render(request, 'insert_topic.html',d)



def insert_webpage(request):
    EWFO= WebpageForm()
    d={'EWFO':EWFO}

    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        
        if WFDO.is_valid():
            tn= WFDO.cleaned_data['topic_name'] #form -- class attribute
            name = WFDO.cleaned_data['name']
            url =WFDO.cleaned_data['url']
            email = WFDO.cleaned_data['email']
            
            #WO = Webpage.objects.get_or_create(topic_name = tn,name=name,url=url,email=email)[0]
           # WO.save()

            return HttpResponse(str(WFDO.cleaned_data)) #{'topic_name': , 'name': 'NagaPrathap', 'url': None, 'email': 'prashanth@gmail.com', 'reemail': 'prashanth@gmail.com'}
        else:
            return HttpResponse('Invalid Data')
    return render(request, 'insert_webpage.html',d)



def insert_access(request):
    EAFO= AccessRecordForm()
    d={'EAFO':EAFO}

    if request.method == 'POST':
        AFDO = AccessRecordForm(request.POST) # access form data object
        
        if AFDO.is_valid():
            
            name = AFDO.cleaned_data['name']
            date =AFDO.cleaned_data['date']
            author = AFDO.cleaned_data['author']
            
            AO = AccessRecord.objects.get_or_create(name=name,date=date, author=author)[0]
            AO.save()

            return HttpResponse('Acess Record Inserted Successfully')
        else:
            return HttpResponse('Invalid Data')
    return render(request, 'insert_access.html',d)


