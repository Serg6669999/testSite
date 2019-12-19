from django.shortcuts import render
from .forms import DataForm
from .forms import UserForm
import requests
import json


def start(request):
    return render(request, 'page/start.html', {})


def page(request):
    if request.method == 'POST':
        # form = DataForm(request.POST)
        response = request.POST
        dicts = response.dict()
        number_1 = dicts['number_1']
        number_2 = dicts['number_2']
        payload = {'number_1': number_1, 'number_2': number_2}

        request_response_servis = requests.post('https://microservices.pythonanywhere.com/',
                                                json=payload)
        print('request_response_servis = ', request_response_servis)
        data_dict = (request_response_servis.json())
        print('data_dict = ', data_dict)
        form = data_dict['number']
        text = 'Нажмите цифру '
        print('form = ', form)

        print('1 = ', number_1)
        print('2 = ', number_2)
        return render(request, 'page/page.html', {'data': form, 'text': text})
    else:
        form = DataForm()
        return render(request, 'page/page.html', {'form': form})


# Create your views here.


def slack(request):
    if request.method == 'POST':
        # form = DataForm(request.POST)
        response = request.POST
        dicts = response.dict()
        number_1 = dicts['number_1']
        number_2 = dicts['number_2']
        # payload = {'number_1': number_1, 'number_2': number_2}
        '''payload = {
            "token": "one-long-verification-token",
            "team_id": "T061EG9R6",
            "api_app_id": "A0PNCHHK2",
            "event": {
                "type": "message",
                "channel": "D024BE91L",
                "user": "U2147483697",
                "text": "Hello hello can you hear me?",
                "ts": "1355517523.000005",
                "event_ts": "1355517523.000005",
                "channel_type": "im"
            },
            "type": "event_callback",
            "authed_teams": ["T061EG9R6"],
            "event_id": "Ev0PV52K21",
            "event_time": 1355517523
        }'''
        payload = {"text": "Hello, World!"}
        # request_response_servis = requests.post('https://hooks.slack.com/services/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',
        #                                        json=payload)
        request_response_servis = requests.post(
            'https://hooks.slack.com/services/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',
                                               params=payload)
        print('request_response_servis = ', request_response_servis)
        data_dict = (request_response_servis.json())
        print('data_dict = ', data_dict)
        form = data_dict
        text = 'Нажмите цифру '
        print('form = ', form)

        print('1 = ', number_1)
        print('2 = ', number_2)
        return render(request, 'page/page.html', {'data': form, 'text': text})
    else:
        form = DataForm()
        return render(request, 'page/page.html', {'form': form})


def send_data_users(request):
    if request.method == 'POST':
        # form = UserForm(request.POST)
        response = request.POST
        dicts = response.dict()
        sender = dicts['sender']
        recipient = dicts['recipient']
        password = dicts['password']
        subject = dicts['subject']
        text = dicts['text']
        payload = {'sender': sender,
                   'recipient': recipient,
                   'password': password,
                   'subject': subject,
                   'text': text,
                   }
        print('payload = ', payload)
        url_request = 'https://sendemail.pythonanywhere.com'
        request_data_of_user = requests.post(url_request, json=payload)
        status_request = 'Статуст отправки сообщения'
        return render(request, 'page/email.html', {'data': request_data_of_user.json(), 'text': status_request})
    else:
        form = UserForm()
        return render(request, 'page/email.html', {'form': form})
