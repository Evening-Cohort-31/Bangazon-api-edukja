from django.contrib import admin
from bangazonapi.models import Customer, Favorite, Order, OrderProduct, Payment, Product, ProductCategory, ProductRating, Rating, Recommendation

# Register your models here.
admin.site.register(Customer)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductRating)
admin.site.register(Rating)
admin.site.register(Recommendation)