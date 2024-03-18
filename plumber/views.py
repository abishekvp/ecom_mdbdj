from django.shortcuts import render, redirect
from user_admin.models import AdminProduct as Product
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'plumber/index.html')

def products(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        for i in range(len(products)):
            features = products[i].pro_features
            features = features.split('\n')
            products[i].pro_price_per_user=products[i].pro_price_plumber
            products[i].pro_price_prime=products[i].pro_price_plumber
            products[i].pro_price=products[i].pro_price_plumber
            for j in range(len(features)):
                features[j] = features[j].strip()
            products[i].pro_features = features
        return render(request, 'plumber/products.html', {'products': products})
    else:return redirect('signin')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'plumber/profile.html', {'user': request.user})
    else:
        return redirect('signin')
    
def edit_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=request.user.email)
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('plumber-profile')
    return render(request, 'plumber/editprofile.html', {'user': request.user})