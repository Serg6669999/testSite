from django.shortcuts import render
from .forms import DataForm
import requests
import json


def page(request):
    if request.method == 'POST':
        # form = DataForm(request.POST)
        response = request.POST
        dicts = response.dict()
        number_1 = dicts['number_1']
        number_2 = dicts['number_2']
        payload = {'number_1': number_1, 'number_2': number_2}
        request_response_servis = requests.post('http://127.0.0.1:8000/',
                                          json=payload)
        print('request_response_servis = ', request_response_servis)
        data_dict = json.loads(request_response_servis.content)
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
