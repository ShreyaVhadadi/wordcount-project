from django.http import HttpResponse
from django.shortcuts import render
import operator
# We actually passing an http request
# We cannot just give back a string we need to give back an http response
def homepage(request):
     return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    dictionary={}
    for word in wordlist:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word]=1
    sortedword=sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltxt':fulltext,'count':len(wordlist),'sortedword':sortedword})

def about(request):
    return render(request,'about.html')