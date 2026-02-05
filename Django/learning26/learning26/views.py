from django.http import HttpResponse
from django.shortcuts import render

# specific urls 
def test(request):
    return HttpResponse("Hello")
def AboutUs(request):
    return render(request,"about.html")
def ContactUs(request):
    return render(request,"contactus.html")
def home(request):
    return render(request,"home.html")
def movies(request):
    return render(request,"movies.html")
def shows(request):
    return render(request,"shows.html")
def news(request):
    return render(request,"news.html")
def recipe(request):
    ingredients=["Noodles","Masala","Vagitable","Water"]
    data={
        "name":"Maggie",
        "time":5,
        "ingredients": ingredients
    }
    return render(request,"recipe.html",data)
def team(request):
    players1=["Dhoni", "Ruturaj", "Sanju", "Jadeja", "Rishabh"]
    players2=["Bumrah", "Virat", "Shami", "Rohit" , "Hardik", "Kuldip"]
    data={"team1name": "Chennai Super Kings",
         "team2name": "Royal Challengers Bangalore",
         "captain1": "Dhoni",
         "captain2": "Virat",
         "players1": players1,
         "players2": players2,
         "rcbtrophy" : 2,
         "csktrophy" : 5
    }
    return render(request,"team.html",data)