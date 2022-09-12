from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    return render(request, "katalog.html",context)

data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Debby Trinita'
}

