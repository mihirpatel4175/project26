from django.shortcuts import render

# Create your views here.
def studentHome(request):
    return render(request,"student/studentHome.html")
def studentList(request):
    studlist={
        "Name":['Mihiir','Laxmi','Ayushi','Parth'],
        "Age":[20,21,22,23],
        "Branch":["Computer Science","IT","Mechanical","Civil"]
    }
    return render(request,"student/studentList.html",{"studlist":studlist}) 