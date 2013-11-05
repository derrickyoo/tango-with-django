from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Query the database for a list of ALL categories stored.
    # Order the categories by number of lokes in descending order.
    # Retrive the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary whihc will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {
        'boldmessage': 'Welcome to the Rango Homepage', 
        'categories': category_list
    }

    # Return a rendered response to send the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': 'Welcome to the Rango About Page'}
    return render_to_response('rango/about.html', context_dict, context)