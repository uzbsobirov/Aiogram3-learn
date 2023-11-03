from aiogram import Router, types
from loader import bot
from aiogram.filters import Command

from data.config import token

router = Router()


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
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successfull_payment(message: types.Message):
    msg = f"Thanks for payment {message.successful_payment.total_amount // 100} {message.successful_payment.currency}"
    await message.answer(msg)
