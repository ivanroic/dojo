from django.shortcuts import render
from time import gmtime, strftime, timezone
    
def index(request):
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request,'index.html', context)

