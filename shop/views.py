from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.

def home(request):
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    
    if response.status_code == 200:
        products = response.json()
        category_product = {}
        
        for product in products:
            category = product['category']
            if category not in category_product:
                category_product[category] = product
            
        filtered_products = list(category_product.values())
        print(filtered_products)
        return render(request,'index.html',{'categories':filtered_products,'products':products})
    else:
        return HttpResponse("Error",status=response.status_code)
    
    
