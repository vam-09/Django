from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
arr = ["python","PHP","c","c++","Javascript","Django"]

count = dict()
print(count)
a = dict(sorted(count.items(),key = lambda x:x[1],reverse=True))
print(a)


def index(request):
    return render(request,"index.html")

def getquery(request):
    q = request.GET["languages"]
    
    if q not in count:
        count[q] = 1
    else:
        count[q] += 1
    
    mydict = {
        "arr" : arr,
        "count" :count,
    }
    # print(mydict["count"])
    return render(request,"index.html",context=mydict)
    
def sortedpoll(request):
    global count
    count = dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
    mydict = {
        "arr" :arr,
        "count" : count,
    }
    return render(request,"index.html",context=mydict)


'''
arr = [1,2,3,4,6,2,4,5]
mydict = dict()
for i in arr:
    if i in mydict:
        pass
    else:
        count = arr.count[i]
        mydict[i] = count

'''
