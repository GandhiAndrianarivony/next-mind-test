import os
from fastapi import Depends, APIRouter, Request

import stripe

from onyx.auth.users import current_user
from onyx.db.models import User
from onyx.server.stripe.schema import StripeCheckoutSessionSchema


stripe_payment_router = APIRouter(
    tags=["Stripe-Payment"],
    prefix="/stripe",
)


@stripe_payment_router.post("/create-checkout-session")
def create_checkout_session(
    request: Request,
    user: User | None = Depends(current_user),
) -> StripeCheckoutSessionSchema:
    stripe_api_key = os.environ.get("STRIPE_SECRET_KEY")
    stripe.api_key = stripe_api_key

    # TODO: Get product from database
    product = {"price": 2000, "name": "Test Product", "product_id": 1}

    YOUR_DOMAIN = "http://127.0.0.1:3000"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": product["price"],
                    "product_data": {
                        "name": product["name"],
                    },
                },
                "quantity": 1,
            },
        ],
        metadata={"product_id": product["product_id"]},
        mode="payment",
        success_url=YOUR_DOMAIN + "/chat",
        cancel_url=YOUR_DOMAIN + "/",
    )
    return StripeCheckoutSessionSchema(session_id=checkout_session.id, session_url=checkout_session.url)
