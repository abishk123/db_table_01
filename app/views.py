from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
from app.models import *


def insert_topic(request):
    tn=input('enter topicname: ')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('NEW TOPIC IS CREATED')
    else:
        return HttpResponse('ENTERED TOPIC IS ALREADY PRESENT IN DB')

def insert_topic_by_f(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        if TO[1]:
            return HttpResponse('NEW TOPIC IS CREATED')
        else:
            return HttpResponse('ENTERED TOPIC IS ALREADY PRESENT IN DB')
    else:
        return render(request,'topic.html')
    
def insert_topic_by_df(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)
            if TO[1]:
                return HttpResponse('NEW TOPIC IS CREATED')
            else:
                return HttpResponse('ENTERED TOPIC IS ALREADY PRESENT IN DB')
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'insert_topic_by_df.html',d)

def insert_topic_by_mf(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        FD=TopicModelForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('NEW TOPIC IS CREATED or ALREADY EXIST')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_topic_by_mf.html',d)




def insert_webpage(request):
    tn=input('enter topicname: ')
    name=input('enter name: ')
    url=input('enter url: ')
    email=input('enter email: ')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WTOD=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
        if WTOD[1]:
            return HttpResponse('NEW WEBPAGE OBJECT IS CREATED IN DB')
        else:
            return HttpResponse('THE DATA OF WEBPAGE OBJECT IS ALREADY EXIST IN DB')
    else:
        return HttpResponse('GIVEN TOPIC IS NOT AVAILABLE IN DB')

def insert_webpage_by_f(request):
    if request.method=='POST':
        tn=request.POST["topic_name"]
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        LTO=Topic.objects.filter(topic_name=tn)
        if LTO:
            TO=LTO[0]
            WTOD=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
            if WTOD[1]:
                return HttpResponse(f'{name} OBJECT IS CREATED IN WEBPAGE')
            else:
                return HttpResponse(f'{name} OBJECT IS ALREADY EXISTS IN WEBPAGE')
        else:
            return HttpResponse('THE ENTERED TOPIC IS NOT PRESENT IN DB')
    else:
        return render(request,'webpage.html')
    
def insert_webpage_by_df(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=tn,name=name,url=url,email=email)
            if WO[1]:
                return HttpResponse('NEW WEBPAGE OBJECT IS CREATED IN DB')
            else:
                return HttpResponse('THE DATA OF WEBPAGE OBJECT IS ALREADY EXIST IN DB')
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'insert_webpage_by_df.html',d)

def insert_webpage_by_mf(request):
    EWMFO=WebpageModelForm()
    d= {'EWMFO':EWMFO}
    if request.method=='POST':
        FD=WebpageModelForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('NEW WEBPAGE OBJECT IS CREATED IN DB')
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'insert_webpage_by_mf.html',d)




def insert_accessRecords(request):
    id=int(input('enter id of webpage'))
    date=input('enter date')
    author=input('enter author')
    LWO=Webpage.objects.filter(id=id)
    if LWO:
        ARO=AccessRecords.objects.get_or_create(name=LWO[0],date=date,author=author)
        if ARO[1]:
            return HttpResponse('ACCESS RECORD OBJECT IS INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('THE ENTERED DATA IS ALREADY PRESENT IN ACCESS RECORDS')
    else:
        return HttpResponse('THE ENTERED ID IS NOT PRESENT IN WEBPAGE IN THE DB')

# USING FORMS
def insert_accessRecords_by_f(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        date=request.POST['date']
        author=request.POST['author']
        LWO=Webpage.objects.filter(pk=id)
        print(LWO)
        if LWO:
            ARO=AccessRecords.objects.get_or_create(name=LWO[0],date=date,author=author)
            if ARO[1]:
                return HttpResponse('ACCESS RECORD OBJECT IS INSERTED SUCCESSFULLY')
            else:
                return HttpResponse('THE ENTERED DATA IS ALREADY PRESENT IN ACCESS RECORDS')
        else:
            return HttpResponse(f'THERE IS NO SUCH {id} ID IN WEBPAGE')
    else:
        return render(request,'accessrecord.html')

# USING DJANGO FORMS
def insert_accessRecords_by_df(request):
    EARO=AccessRecordsForm()
    d={'EARO':EARO}
    if request.method=='POST':
        ARDO=AccessRecordsForm(request.POST)
        if ARDO.is_valid():
            name=ARDO.cleaned_data['name']
            author=ARDO.cleaned_data['author']
            date=ARDO.cleaned_data['date']
            ARO=AccessRecords.objects.get_or_creat(name=name,author=author,date=date)
            if ARO[1]:
                return HttpResponse('ACCESS RECORD OBJECT IS INSERTED SUCCESSFULLY')
            else:
                return HttpResponse('THE ENTERED DATA IS ALREADY PRESENT IN ACCESS RECORDS')
        else:
            return HttpResponse('INVALID DATA')
    else:
        return render(request,'insert_access_by_df.html',d)

def insert_access_by_mf(request):
    EAMFO=AccessRecordsModelForm()
    d={'EAMFO':EAMFO}
    if request.method=='POST':
        FO=AccessRecordsModelForm(request.POST)
        if FO.is_valid():
            FO.save()
            return HttpResponse('ACCESS RECORD OBJECT IS INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'insert_access_by_mf.html',d)




def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LARO=AccessRecords.objects.all()
    d={'LARO':LARO}
    return render(request,'display_access.html',d)
    

