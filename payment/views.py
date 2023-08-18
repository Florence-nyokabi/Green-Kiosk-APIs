from django.shortcuts import render, redirect
from product_cart.models import ProductCart
from .models import Payment
from .forms import PaymentForm
from datetime import datetime

# Create your views here.
def make_payment(request):
    product_cart = ProductCart.objects.all()

    # total_price = sum(item.total_price() for item in product_cart)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_details = form.cleaned_data  # Use cleaned_data instead of changed_data

            payment = Payment.objects.create(
                payment_method=payment_details['payment_method'],
                # amount=total_price,
                currency=payment_details['currency'],
                date_of_payment=datetime.now(),
                status='Pending'
            )

            product_cart.delete()
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'payment/make_payment.html', {'form': form})