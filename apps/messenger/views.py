from django.http import HttpRequest, HttpResponse
from django.views import View
from django.conf import settings

from apps.common import response
from apps.messenger.forms import MessageForm

import telebot

bot = telebot.TeleBot(token=settings.TELEGRAM_BOT_TOKEN)


class MessageView(View):
    template_name = 'messenger.html'
    form_class = MessageForm

    recipient = settings.TELEGRAM_USER_ID

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        ''' This method returns form in html webpage. '''
        return response.TemplateFormResponse(request, self.template_name, self.form_class())

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.POST.get('name') or not request.POST.get('message'):
            return HttpResponse('You have to fill all inputs.')

        bot.send_message(self.recipient, '\n'.join([
            f'Message from {request.POST.get('name')}',
            'Body:',
            str(request.POST.get('message'))
        ]))

        return HttpResponse(content='Sent!')
