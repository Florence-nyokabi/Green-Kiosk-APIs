from django.shortcuts import render
from .forms import ProductUploadForm

# Create your views here.
def product_upload_view(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form":form})
