from django.shortcuts import render

def default_view(request):
    return render(request, 'tax/default.html')

def calculate_total(request, price):
    try:
        price = float(price)
        tax_rate = 0.15  # Set the tax rate to 15% (0.15)
        total = price + (price * tax_rate)
        context = {
            'price': price,
            'tax_rate': tax_rate,
            'total': total,
        }
        return render(request, 'tax/calculate.html', context)
    except ValueError:
        return render(request, 'tax/invalid_price.html')

def tax_rate_view(request):
    tax_rate = 0.15  # Set the tax rate to 15% (0.15)
    context = {
        'tax_rate': tax_rate,
    }
    return render(request, 'tax/tax_rate.html', context)