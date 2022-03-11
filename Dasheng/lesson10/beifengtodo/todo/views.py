from django.shortcuts import render,redirect
from todo.forms import DreamForm
from todo.models import Dream

# Create your views here.

def index(request):
    dreamForm = DreamForm({'content':''})
    dreamList = Dream.objects.all()

    # return render(request,'base.html',locals())
    return render(request,'index.html',locals())

def addDream(request):
    # /d/add
    try :
        dreamForm = DreamForm(request.POST)
        if dreamForm.is_valid():
            dreamData = dreamForm.cleaned_data
            dream = Dream.objects.create(content=dreamData['content'])
            dream.save()
    except:
        print dreamFrom.errors
    return redirect(request.META['HTTP_REFERER'])

def deleteDream(request):
    # /d/d/?did=10
    dreamID = request.GET.get('did')
    try :
        dream = Dream.objects.get(pk=dreamID)
        dream.delete()
    except:
        pass

    return redirect(request.META['HTTP_REFERER'])

def updateDream(request):
    # /d/u/?did=10
    dreamID = request.GET.get('did')
    try :
        dream = Dream.objects.get(pk=dreamID)
        dream.status = True if dream.status == False else False
        dream.save()
    except:
        pass
    return redirect(request.META['HTTP_REFERER'])
