from django.shortcuts import render
from django.shortcuts import redirect

from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list/')

    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})