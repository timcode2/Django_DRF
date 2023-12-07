
import stripe
from config import settings


def get_stripe_link(payment) -> str:
    """Функция для получения ссылки на платеж"""

    stripe.api_key = settings.STRIPE_SECRET_KEY  # авторизация на сервере

    # если у платежа есть курс, получаем курс. Иначе получаем урок.
    if payment.course:
        purchase = payment.course  # получаем курс
    else:
        purchase = payment.lesson  # получаем урок

    product = stripe.Product.create(name=purchase.name, description=purchase.description)  # создаем продукт

    # Создаем цену для продукта (stripe считает что цена в копейках или центах.
    # Умножаем на 100 чтобы получить доллары или рубли)
    price = stripe.Price.create(unit_amount_decimal=purchase.price * 100,
                                currency=purchase.currency,
                                product=product.get("id"))

    # Создаем ссылку на платеж
    payment_link = stripe.PaymentLink.create(line_items=[{"price": price.get("id"), "quantity": 1}])

    return payment_link.get("url")