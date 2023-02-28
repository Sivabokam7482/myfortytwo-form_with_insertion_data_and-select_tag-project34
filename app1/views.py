from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic data is Inserted')
    return render(request,'insert_topic.html')




def insert_webpage(request):
    QST=Topic.objects.all()
    d={'topic':QST}
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        name=request.POST['name']
        url=request.POST['url']
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('Webpage data is Inserted.')
    return render(request,'insert_webpage.html',d)




    
def insert_accessrecord(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST": 
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()

        name=request.POST['name']
        url=request.POST['url']
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()

        date=request.POST['date']
        A=AccessRecord.objects.get_or_create(name=W,date=date)[0]
        A.save()
        return HttpResponse('Access data is Inserted.')
    return render(request,'insert_access.html',d)


