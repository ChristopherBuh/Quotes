from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    
    return render (request, 'exam/main.html')

def register(request):
    errors = User.objects.validate_register(request.POST)
    if len(errors) ==0:
        User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], dob = request.POST['dob'])
        return redirect ('/')
    else:
        for message in errors:
            messages.error(request, message)
        return redirect ('/')

def login (request):
    errors = User.objects.validate_login(request.POST)
    if len(errors)==0:
        user = User.objects.filter(email = request.POST['email'])
        user = user[0]
        request.session['user_id'] = user.id
        return redirect ('/quotes')
    else:
        for message in errors:
             messages.error(request, message)
        return redirect ('/')

def quotes (request):
         this_user = User.objects.get(id=request.session['user_id'])
         context = {
        'user': this_user,
        'quotes':Quote.objects.exclude(favorite_quotes = this_user),
        'favorite_quotes': this_user.favorite_quotes.all()
         
    }
         return render(request, 'exam/quotes.html', context)

def createquote (request):
    errors = Quote.objects.validate_quote(request.POST)
    if len(errors)==0:
        Quote.objects.create(quoted_by = request.POST['quoted_by'], message = request.POST['message'], posted_by = User.objects.get(id=request.session['user_id']))
        return redirect ('/quotes')
    else:
        for message in errors:
            messages.error(request, message)
        return redirect ('/quotes')

def add_favquote (request, quote_id):
    this_user = User.objects.get(id=request.session['user_id'])
    fav_quote = Quote.objects.get(id = quote_id)
    this_user.favorite_quotes.add(fav_quote)
    return redirect ('/quotes')

def rem_favquote(request, quote_id):
    this_user = User.objects.get(id=request.session['user_id'])
    fav_quote = Quote.objects.get(id = quote_id)
    this_user.favorite_quotes.remove(fav_quote)
    return redirect ('/quotes')

def display_user (request, user_id):

    posts = Quote.objects.filter(posted_by = user_id)
    this_user = User.objects.get(id = user_id)
    context = {
        'user' : this_user,  
        'posts': posts
      
       
     }
    return render(request, 'exam/show_user.html', context)

def logout (request):
    request.session.clear()
    return redirect('/')






