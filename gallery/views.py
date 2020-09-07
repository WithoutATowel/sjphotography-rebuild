from django.shortcuts import render
from .models import Collection, Photo

# Create your views here.
def index(request):
    return render(request, 'index.html')

def collections(request):
    collections = Collection.objects.all()
    return render(request, 'collections.html', {'collections': collections})

def show_collection(request, collection_id):
    photos = Photo.objects.filter(collection_id=collection_id)
    collection = Collection.objects.get(id=collection_id)
    return render(request, 'show_collection.html', {'collection': collection, 'photos': photos})

def contact(request):
    return render(request, 'contact.html')
