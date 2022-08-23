from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from common.models import Offer, Cooperation
from . import static_text
from tgbot.models import User
from .keyboards import make_keyboard_for_offer_option_uz, make_keyboard_for_offer_option_ru

OFFER, OFFER_RECEIVE = range(3, 5)


def offer_handler(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    text = static_text.give_offer_uz
    keyboard = make_keyboard_for_offer_option_uz()
    if u.lang == "ru":
        text = static_text.give_offer_ru
        keyboard = make_keyboard_for_offer_option_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return OFFER


def offer_receiver(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    offer = update.message.text
    offer_obj = Offer.objects.create(text=offer, user=u)
    text = static_text.offer_received_uz
    keyboard = make_keyboard_for_offer_option_uz()
    if u.lang == "ru":
        text = static_text.give_offer_ru
        keyboard = make_keyboard_for_offer_option_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    # context.bot.send_message(chat_id='-1001799210747', from_chat_id=update.message.chat_id,
    #                                 text="Taklif")
    a = context.bot.forward_message(chat_id='-1001799210747', from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
    offer_obj.group_msg_id = a.message_id
    update.message.reply_text("Taklifingiz uchun id: {}".format(a.message_id))
    offer_obj.save()
    return OFFER_RECEIVE


def offer_and_cooperation_answer_handler(update: Update, context: CallbackContext):
    if update.message.reply_to_message and update.message.reply_to_message.chat.type == 'supergroup':

        try:
            object = Offer.objects.get(group_msg_id=update.message.reply_to_message.message_id)
            text = f"Siz yuborgan {object.group_msg_id} - sonli taklifingiz uchun javob:\n\n'{update.message.text}'"

        except:
            object = Cooperation.objects.get(group_msg_id=update.message.reply_to_message.message_id)
            text = f"Siz yuborgan {object.group_msg_id} - sonli xamkorlik xatingiz uchun javob:\n\n'{update.message.text}'"

        context.bot.send_message(chat_id=object.user.user_id, text=text)
        object.is_active = False
        object.save()

