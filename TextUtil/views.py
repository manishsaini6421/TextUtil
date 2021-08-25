from django.http import HttpResponse, request
from django.shortcuts import render
 
def index(request):    
    return render(request ,'index.html')

def textanalyzer(request):
    text=request.POST.get("text","default")
    punc="""~!@#$%^&*()_-";:'?{}[]\.<>,/?"""

    removepunc=request.POST.get("removepunc","off")
    extraspaceremove=request.POST.get("extraspaceremove","off")
    newlineremove=request.POST.get("newlineremove","off")
    cherectorcount=request.POST.get("cherectorcount","off")
    CAPITALIZE_TEXT=request.POST.get("CAPITALIZE_TEXT","off")
    
    
    if removepunc =='on':
        analyzed=''
        
        for i in text:
            if i not in punc:
                analyzed+=i
        param={"analyzed_text":analyzed,"purpose":"Removed punctation"}  
        text=analyzed      
       
    if(extraspaceremove=="on"):
        analyzed=''
        for i,j in enumerate(text):
            if not (text[i]==" " and text[i+1]==" "):
                analyzed+=j
        param={"analyzed_text":analyzed,"purpose":"Removed Extra space"}
        text=analyzed 
        
    if(newlineremove=="on"):
        analyzed=''
        for i in text:
            if i !="\n" and i!="\r":
                analyzed+=i 
            
        param={"analyzed_text":analyzed,"purpose":"Removed NewLine charector"}
        text=analyzed 
                   
    if(CAPITALIZE_TEXT=="on"):
        analyzed=''
        for i in text:
            analyzed+=i.upper()
        param={"analyzed_text":analyzed,"purpose":"Capatilazed text"} 
         
    if (removepunc !='on' and CAPITALIZE_TEXT!="on" and newlineremove!="on" and extraspaceremove!="on") :
        analyzed=text
        param={"analyzed_text":analyzed,"purpose":"No action selected"} 

    return  render(request,"analyze.html",param)        
      
        
    
    

     