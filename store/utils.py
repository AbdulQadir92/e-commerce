from .models import *


def cart_icon_total(request):
    try:
        order = Order.objects.get(user_id=request.user.id, complete=False)
        order_items = OrderItem.objects.filter(order_id=order.id)
        _cart_icon_total = 0
        for order_item in order_items:
            _cart_icon_total += order_item.quantity
        return _cart_icon_total
    except:
        return 0


def wishlist_items_total(request):
    try:
        _wishlist_items_total = WishList.objects.filter(user=request.user).count()
        return _wishlist_items_total
    except:
        return 0


def correct_price(price):
    if price == '0-50':
        price = 'Up to $50'
    elif price == '50-100':
        price = '$50 to $100'
    elif price == '100-200':
        price = '$100 to $200'
    elif price == '200-400':
        price = '$200 to $400'
    elif price == '400-600':
        price = '$400 to $600'
    elif price == '601-100000':
        price = 'Above $600'

    return price


# def all_categories():
#     categories = Categories.objects.all()
#     data = []
#     for category in categories:
#         category_dict = {
#             'id': category.id,
#             'category': category.categories,
#             'subcategories': []
#         }
#         data.append(category_dict)
#     return data


