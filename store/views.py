import django
from django.contrib.auth.models import User
from store.models import Address, Cart, Category, Order, Product,BlogPost
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistrationForm, AddressForm
from django.contrib import messages
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for Class Based Views
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


from .models import BlogPost  # Import BlogPost model

def about(request):
    return render(request, 'store/about.html')
def blog_post_detail(request, id):
    post = BlogPost.objects.get(id=id)  # Use BlogPost, not Post
    return render(request, 'store/post_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phonenumber']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email (example using Django's send_mail function)
            send_mail(
                f"Message from {name} ({subject})",
                f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}",
                email,
                [settings.CONTACT_EMAIL],  # Replace with your contact email
            )

            # Show a success message
            messages.success(request, "Your message has been sent successfully!")
            return render(request, 'store/contact.html', {'form': form})

        else:
            messages.error(request, "There was an error with your form. Please check the details and try again.")

    else:
        form = ContactForm()

    return render(request, 'store/contact.html', {'form': form})

# Create your views here.

def home(request):
    categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'store/index.html', context)


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.exclude(id=product.id).filter(is_active=True, category=product.category)
    context = {
        'product': product,
        'related_products': related_products,

    }
    return render(request, 'store/detail.html', context)


def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'store/categories.html', {'categories':categories})


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(is_active=True, category=category)
    categories = Category.objects.filter(is_active=True)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/category_products.html', context)


# Authentication Starts Here

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, "Congratulations! Registration Successful! Please log in.")
            return redirect('store:login')  # Redirect to the login page
        return render(request, 'account/register.html', {'form': form})  # Re-render registration page if form is invalid

        






@method_decorator([never_cache, csrf_exempt], name='dispatch')
class LogoutView(BaseLogoutView):
    def get(self, request, *args, **kwargs):
        # Call the parent `post` method to reuse the logout logic
        return self.post(request, *args, **kwargs)

@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {'addresses':addresses, 'orders':orders})


@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'account/add_address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            user=request.user
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            reg = Address(user=user, locality=locality, city=city, state=state)
            reg.save()
            messages.success(request, "New Address Added Successfully.")
        return redirect('store:profile')


@login_required
def remove_address(request, id):
    a = get_object_or_404(Address, user=request.user, id=id)
    a.delete()
    messages.success(request, "Address removed.")
    return redirect('store:profile')

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(Cart, product=product_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user, product=product).save()
    
    return redirect('store:cart')


@login_required
def cart(request):
    user = request.user
    cart_products = Cart.objects.filter(user=user)

    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

    # Customer Addresses
    addresses = Address.objects.filter(user=user)

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
        'addresses': addresses,
    }
    return render(request, 'store/cart.html', context)


@login_required
def remove_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
        messages.success(request, "Product removed from Cart.")
    return redirect('store:cart')


@login_required
def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('store:cart')


@login_required
def minus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        # Remove the Product if the quantity is already 1
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('store:cart')


@login_required
def checkout(request):
    user = request.user
    address_id = request.GET.get('address')

    # Check if address_id exists and is valid
    if not address_id:
        messages.error(request, "No address selected. Please select a shipping address.")
        return redirect('store:profile')  # Redirect to profile or address selection page

    try:
        # Ensure that the address belongs to the current user
        address = Address.objects.get(id=address_id, user=user)
    except Address.DoesNotExist:
        messages.error(request, "Invalid address selected. Please select a valid address.")
        return redirect('store:profile')  # Redirect to profile or address selection page

    # Get all the products of the User in Cart
    cart = Cart.objects.filter(user=user)
    if not cart.exists():
        messages.error(request, "Your cart is empty. Please add items to the cart.")
        return redirect('store:shop')  # Redirect to the shop or cart page

    # Proceed to save the order and clear the cart
    for c in cart:
        # Saving all the products from Cart to Order
        Order(user=user, address=address, product=c.product, quantity=c.quantity).save()
        # Deleting from Cart
        c.delete()

    messages.success(request, "Your order has been placed successfully!")
    return redirect('store:orders')

@login_required
def orders(request):
    all_orders = Order.objects.filter(user=request.user).order_by('-ordered_date')
    return render(request, 'store/orders.html', {'orders': all_orders})





def shop(request):
    return render(request, 'store/shop.html')

from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'store/blog_list.html', {'posts': posts})


def test(request):
    return render(request, 'store/test.html')
