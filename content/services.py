import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_product(name):
    product = stripe.Product.create(
        name=name
    )
    return product["id"]


def create_stripe_price(product_id, amount):
    price = stripe.Price.create(
        unit_amount=amount * 100,
        currency="usd",
        product=product_id,
    )
    return price["id"]


def create_stripe_session(price_id):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )

    return session["url"]