from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from service.models import Service
from contactdata.models import ContactEnquiry


def homepage(request):
    serviceData = Service.objects.all()
    if request.method=='GET':
        st = request.GET.get('newsname')
        if st != None:
            serviceData = Service.objects.filter(post_title__icontains=st)


    data = {
        'serviceData' : serviceData


    }


    return render(request,"index.html",data)




def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"services.html")
def submitform(request):
    try:
        if request.method=="POST":
            n1 = int(request.POST.get('name'))
            n2 = int(request.POST.get('email'))
            n3 = int(request.POST.get('message'))
            finalscore = n1+n2+n3
             
            return HttpResponse(finalscore)
            
    except:
        pass
    

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en = ContactEnquiry(name=name,email=email,message=message)
        en.save()
    return render(request,"contact.html")

def marksheet(request):
    
    if request.method=="POST":
        sub1=int(request.POST.get('Shubject 1'))
        sub2=int(request.POST.get('Shubject 2'))
        sub3=int(request.POST.get('Shubject 3'))
        total = sub1+sub2+sub3
        p = total*100/500
        deta={
            'total' : total,
            'p' : p,

            }
            
        return render(request,"marksheet.html",deta)
    return render(request,"marksheet.html")  

def detailview(request,slug):
    serviceData = Service.objects.get(news_slug=slug)

    data = {
        'serviceData' : serviceData


    }
    return render(request,"newsdetail.html",data)
   
    

    
