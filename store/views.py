from django.shortcuts import render, redirect
from accounts.models import *
from .utils import *
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def home(request):
    categories_data = []
    categories = Categories.objects.all()
    for category in categories:
        subcategories = Subcategories.objects.filter(category=category)
        category_dict = {
            'category': category,
            'subcategories': subcategories
        }
        categories_data.append(category_dict)

    slider_images = SliderImages.objects.all()
    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)

    context = {
        'categories': categories_data,
        'cartIconTotal': cartIconTotal,
        'wishlistItemsTotal': wishlistItemsTotal,
        'sliderImages': slider_images,
    }

    return render(request, 'store/index.html', context)


def get_subcategories(request):
    data = json.loads(request.body)
    category_id = data['categoryId']
    subcategories = Subcategories.objects.filter(category_id=category_id)

    subcategories_data = []
    for subcategory in subcategories:
        subcategory_dict = {
            'id': subcategory.id,
            'subcategory': subcategory.subcategory
        }
        subcategories_data.append(subcategory_dict)

    return JsonResponse({'subcategories': subcategories_data, 'categoryId': category_id})


def get_more_categories(request):
    data = json.loads(request.body)
    subcategory_id = data['subcategoryId']
    more_categories = MoreCategories.objects.filter(subcategory_id=subcategory_id)

    more_categories_data = []
    for more_category in more_categories:
        more_category_dict = {
            'id': more_category.id,
            'moreCategory': more_category.more_category
        }
        more_categories_data.append(more_category_dict)

    return JsonResponse({'moreCategories': more_categories_data, 'subcategoryId': subcategory_id})


def more_category(request, more_category_id):
    moreCategory = MoreCategories.objects.get(id=int(more_category_id))
    subcategory = Subcategories.objects.get(id=moreCategory.subcategory.id)

    products = Product.objects.filter(more_category=moreCategory)
    brands = Brand.objects.filter(subcategory=moreCategory.subcategory)

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)

    context = {
        'moreCategory': moreCategory,
        'products': products,
        'brands': brands,
        'subcategory': subcategory,
        'cartIconTotal': cartIconTotal,
        'wishlistItemsTotal': wishlistItemsTotal
    }
    return render(request, 'store/moreCategory.html', context)


def more_categories(request, subcategory_id):
    more_categories = MoreCategories.objects.filter(subcategory_id=int(subcategory_id))
    subcategory = Subcategories.objects.get(id=subcategory_id)

    moreCategories = []
    brands = Brand.objects.filter(subcategory=subcategory)

    for more_category in more_categories:
        products = Product.objects.filter(more_category=more_category)

        more_category_dict = {
            'more_category': more_category.more_category,
            'products': products
        }
        moreCategories.append(more_category_dict)

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)

    context = {
        'moreCategories': moreCategories,
        'cartIconTotal': cartIconTotal,
        'wishlistItemsTotal': wishlistItemsTotal,
        'subcategory': subcategory,
        'brands': brands
    }
    return render(request, 'store/moreCategories.html', context)


def brand(request, brand_id):
    checked_brand = Brand.objects.get(id=brand_id)
    products = Product.objects.filter(brand=checked_brand)
    brands = Brand.objects.all()
    subcategory = Subcategories.objects.get(id=checked_brand.subcategory.id)

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)

    context = {
        'products': products,
        'checked_brand': checked_brand,
        'brands': brands,
        'subcategory': subcategory,
        'wishlistItemsTotal': wishlistItemsTotal,
        'cartIconTotal': cartIconTotal
    }
    return render(request, 'store/brand.html', context)


def sort_by_price(request, subcategory_id, price):
    more_categories = MoreCategories.objects.filter(subcategory_id=subcategory_id)
    subcategory = Subcategories.objects.get(id=subcategory_id)
    brands = Brand.objects.filter(subcategory_id=subcategory_id)

    split_price = price.split('-')
    min_price = int(split_price[0])
    max_price = int(split_price[1])

    products = []
    for more_category in more_categories:
        _products = Product.objects.filter(more_category=more_category).order_by('price')
        for product in _products:
            product_price = int(product.price)
            if product_price <= max_price and product_price >= min_price:
                products.append(product)

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)
    price = correct_price(price)

    context = {
        'products': products,
        'brands': brands,
        'subcategory': subcategory,
        'price': price,
        'wishlistItemsTotal': wishlistItemsTotal,
        'cartIconTotal': cartIconTotal
    }
    return render(request, 'store/sortByPrice.html', context)


def sort_by_price_more_category(request, more_category_id, price):
    _products = Product.objects.filter(more_category_id=more_category_id)
    more_category = MoreCategories.objects.get(id=more_category_id)
    brands = Brand.objects.filter(subcategory_id=more_category.subcategory.id)

    split_price = price.split('-')
    min_price = int(split_price[0])
    max_price = int(split_price[1])

    products = []
    for product in _products:
        product_price = int(product.price)
        if product_price <= max_price and product_price >= min_price:
            products.append(product)

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)
    price = correct_price(price)

    context = {
        'products': products,
        'moreCategory': more_category,
        'brands': brands,
        'price': price,
        'wishlistItemsTotal': wishlistItemsTotal,
        'cartIconTotal': cartIconTotal
    }
    return render(request, 'store/sortByPriceMoreCategory.html', context)


def sort_by_price_brand(request, brand_id, price):
    checked_brand = Brand.objects.get(id=brand_id)
    _products = Product.objects.filter(brand_id=brand_id)
    brands = Brand.objects.filter(subcategory_id=checked_brand.subcategory.id)

    split_price = price.split('-')
    min_price = int(split_price[0])
    max_price = int(split_price[1])

    products = []
    for product in _products:
        product_price = int(product.price)
        if product_price <= max_price and product_price >= min_price:
            products.append(product)

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)
    price = correct_price(price)

    context = {
        'products': products,
        'price': price,
        'checked_brand': checked_brand,
        'brands': brands,
        'wishlistItemsTotal': wishlistItemsTotal,
        'cartIconTotal': cartIconTotal
    }
    return render(request, 'store/sortByPriceBrand.html', context)


def product_details(request, product_id):
    product = Product.objects.get(pk=int(product_id))

    more_category = product.more_category
    subcategory = more_category.subcategory

    wishlistItemsTotal = wishlist_items_total(request)
    cartIconTotal = cart_icon_total(request)

    context = {
        'product': product,
        'cartIconTotal': cartIconTotal,
        'wishlistItemsTotal': wishlistItemsTotal,
        'subcategory': subcategory,
        'moreCategory': more_category,
    }
    return render(request, 'store/productDetails.html', context)


def order_item(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        product_id = data['productId']
        Product.objects.get(pk=product_id)

        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        order_item, created = OrderItem.objects.get_or_create(
            product_id=product_id,
            order=order
        )
        order_item.quantity += 1
        order_item.save()

        cartIconTotal = cart_icon_total(request)

        return JsonResponse({'msg': 'Order item created', 'cartIconTotal': cartIconTotal})
    else:
        return HttpResponse('Login or Register to add items to cart')


def cart(request):
    if request.user.is_authenticated:
        data = []
        try:
            order = Order.objects.get(user_id=request.user.id)
            order_items = OrderItem.objects.filter(order_id=order.id)

            for order_item in order_items:
                product = Product.objects.get(pk=order_item.product_id)
                order_item_dict = {
                    'id': order_item.id,
                    'primary_image': product.primary_image,
                    'item': product.description,
                    'price': product.price,
                    'shipping': product.shipping,
                    'quantity': order_item.quantity,
                    'total': product.price * order_item.quantity,
                    'product_id': order_item.product_id
                }
                data.append(order_item_dict)
        except:
            pass

        wishlistItemsTotal = wishlist_items_total(request)
        cartIconTotal = cart_icon_total(request)

        context = {
            'order_items': data,
            'cartIconTotal': cartIconTotal,
            'wishlistItemsTotal': wishlistItemsTotal,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('login')

def delete_cart_item(request):
    data = json.loads(request.body)
    cart_item_id = data['id']
    order = Order.objects.get(user=request.user, complete=False)
    order_item = OrderItem.objects.get(order=order, id=cart_item_id)
    order_item.delete()

    cartIconTotal = cart_icon_total(request)

    return JsonResponse({'msg': 'Cart item deleted', 'cartIconTotal': cartIconTotal})


def increment_quantity(request):
    data = json.loads(request.body)
    order_item_id = data['id']
    order_item = OrderItem.objects.get(pk=order_item_id)
    order_item.quantity += 1
    order_item.save()

    cartIconTotal = cart_icon_total(request)

    return JsonResponse({'msg': 'Order item incremented', 'cartIconTotal': cartIconTotal})


def decrement_quantity(request):
    data = json.loads(request.body)
    order_item_id = data['id']
    order_item = OrderItem.objects.get(pk=order_item_id)
    order_item.quantity -= 1
    order_item.save()

    cartIconTotal = cart_icon_total(request)

    return JsonResponse({'msg': 'Order item decremented', 'cartIconTotal': cartIconTotal})


def wishlist(request):
    if request.user.is_authenticated:
        wish_list_items = []
        try:
            data = WishList.objects.filter(user=request.user)
            for wishlist_item in data:
                product = Product.objects.get(id=wishlist_item.product_id)
                wish_list_item = {
                    'primary_image': product.primary_image,
                    'item': product.description,
                    'rating': product.rating,
                    'price': product.price,
                    'shipping': product.shipping,
                    'product_id': wishlist_item.product_id
                }
                wish_list_items.append(wish_list_item)
        except:
            print('Error occurred')

        wishlistItemsTotal = wishlist_items_total(request)
        cartIconTotal = cart_icon_total(request)

        context = {
            'wish_list_items': wish_list_items,
            'cartIconTotal': cartIconTotal,
            'wishlistItemsTotal': wishlistItemsTotal,
        }
        return render(request, 'store/wishlist.html', context)
    else:
        return redirect('login')


def wishlist_item(request):
    try:
        data = json.loads(request.body)
        product_id = data['productId']
        wishlist_item, created = WishList.objects.get_or_create(
            product_id=product_id,
            user=request.user
        )
        wishlist_item.save()

        wishlistItemsTotal = wishlist_items_total(request)
        cartIconTotal = cart_icon_total(request)

        return JsonResponse({
            'msg': 'Wish list item created',
            'cartIconTotal': cartIconTotal,
            'wishlistItemsTotal': wishlistItemsTotal
        })
    except:
        return HttpResponse('Login or Register to add items to wish list')


def delete_wishlist_item(request):
    data = json.loads(request.body)
    wishlist_item_id = data['productId']
    wishlist_item = WishList.objects.get(user=request.user, product_id=wishlist_item_id)
    wishlist_item.delete()

    wishlistItemsTotal = wishlist_items_total(request)

    return JsonResponse({'msg': 'Wish list item deleted', 'wishlistItemsTotal': wishlistItemsTotal})


def checkout(request):
    if request.user.is_authenticated:
        data = []
        total = 0
        shipping = 0
        grand_total = 0
        shipping_information = []
        try:
            order = Order.objects.get(user_id=request.user.id)
            order_items = OrderItem.objects.filter(order_id=order.id)
            for order_item in order_items:
                product = Product.objects.get(pk=order_item.product_id)
                order_item_dict = {
                    'id': order_item.id,
                    'primary_image': product.primary_image,
                    'item': product.description,
                    'price': product.price,
                    'shipping': product.shipping,

                    'quantity': order_item.quantity,
                    'total': product.price * order_item.quantity
                }
                data.append(order_item_dict)
                total += order_item_dict['total']
                shipping += order_item_dict['shipping']
                grand_total = total + shipping

            shipping_information = ShippingInformation.objects.get(customer=request.user.customer)
        except:
            pass

        wishlistItemsTotal = wishlist_items_total(request)
        cartIconTotal = cart_icon_total(request)

        context = {
            'order_items': data,
            'cartIconTotal': cartIconTotal,
            'wishlistItemsTotal': wishlistItemsTotal,
            'shipping': shipping,
            'total': total,
            'grandTotal': grand_total,
            'shippingInformation': shipping_information,
        }
        return render(request, 'store/checkout.html', context)
    else:
        return redirect('login')
