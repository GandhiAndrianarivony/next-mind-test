from pydantic import BaseModel


class StripePaymentSchema(BaseModel):
    email: str


class StripeCheckoutSessionSchema(BaseModel):
    session_id: str
    session_url: str
