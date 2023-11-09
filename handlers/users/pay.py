from aiogram import Router, types
from loader import bot
from aiogram.filters import Command

from data.config import token

router = Router()

keyboards = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Pay",
                pay=True
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Link",
                url="https://nztcoder.com"
            )
        ]
    ]
)

RU_SHIPPING = types.ShippingOption(
    id='ru',
    title="Shipping to Russia",
    prices=[
        types.LabeledPrice(
            label="Shipping to Russia",
            amount=500
        )
    ]
)

UZ_SHIPPING = types.ShippingOption(
    id='uz',
    title="Shipping to Uzbekistan",
    prices=[
        types.LabeledPrice(
            label="Shipping to Uzbekistan",
            amount=250
        )
    ]
)

USA_SHIPPING = types.ShippingOption(
    id='usa',
    title="Shipping to USA",
    prices=[
        types.LabeledPrice(
            label="Shipping to USA",
            amount=1000
        )
    ]
)


async def shipping_check(shipping_query: types.ShippingQuery):
    shipping_options = []
    countries = ['RU', 'UZ', 'USA']
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id, ok=False,
                                               error_message="We can't delivery to your country")

    if shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(RU_SHIPPING)

    if shipping_query.shipping_address.country_code == 'UZ':
        shipping_options.append(UZ_SHIPPING)

    if shipping_query.shipping_address.country_code == 'USA':
        shipping_options.append(USA_SHIPPING)

    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options)


@router.message(Command(commands='pay'))
async def order(message: types.Message):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="With telegram bot",
        description="Payment with telegram bot",
        payload="Payment through a bot",
        provider_token=token,
        currency='rub',
        prices=[
            types.LabeledPrice(
                label="Way to secret data",
                amount=30000
            ),
            types.LabeledPrice(
                label="NDS",
                amount=20000
            ),
            types.LabeledPrice(
                label="Discount",
                amount=20000
            ),
            types.LabeledPrice(
                label="Bonus",
                amount=-40000
            ),
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='uzbsobirov',
        provider_data=None,
        photo_url="https://t.me/blogca/323",
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successfull_payment(message: types.Message):
    msg = f"Thanks for payment {message.successful_payment.total_amount // 100} {message.successful_payment.currency}"
    await message.answer(msg)
