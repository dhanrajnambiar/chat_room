from django.shortcuts import render

import requests, json

from .forms import postForm
from riot_chat.wsgi import acc_token
# Create your views here.

def post(request):
    #requests.packages.urllib3.disable_warnings() to disable warnings about ssl certificate
    def post_message(msg,r_id_1,r_id_2):
        acc = acc_token # acc_token is imported from wsgi file which get's exec only during startup of server
        d = {"msgtype":"m.text","body":msg}
        url = "https://matrix.org:8448/_matrix/client/r0/rooms/%21{0}/send/m.room.message?access_token={1}".format(r_id_1, acc)
        r = requests.post(url, data = json.dumps(d))
        url = "https://matrix.org:8448/_matrix/client/r0/rooms/%21{0}/send/m.room.message?access_token={1}".format(r_id_2, acc)
        q = requests.post(url, data = json.dumps(d))

    room_id_1 = "whKbuarNiMcNeMMlVg:matrix.org"
    room_id_2 = "iCoOVDrUqeATFFdwyZ:matrix.org"

    form_var = postForm(request.POST or None)

    if request.method == "POST":
        if form_var.is_valid():
            heading = "Done"
            message_to_post = form_var.cleaned_data.get('message')

            post_message(message_to_post,room_id_1,room_id_2)

    if request.method == "GET":
        heading = "Enter Your Message"

    context = {
        'title':heading,
        'form':form_var,
    }

    return render(request, 'chat_client/home.html',context)
