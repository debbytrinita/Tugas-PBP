from django.shortcuts import render
from mywatchlist.models import MovieWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    return render(request, "mywatchlist.html",context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = MovieWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MovieWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

data = MovieWatchList.objects.all()
my_watch_list = MovieWatchList.objects.all()
context = {
    'list_film': my_watch_list,
    
}
