from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from constants import BODY_STR
from responses import *

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    From = request.values.get('From')
    incoming = request.values.get(BODY_STR, '').lower()
    print(incoming)
    response = MessagingResponse()
    message = response.message()

    responded = False
    if 'district' in incoming:
        out = listDistricts()
        message.body(out)
        responded = True

    if 'sub' in incoming:
        out = subscribe(incoming)
        print(out)
        message.body(out)
        responded = True

    if 'hospital' in incoming:
        out, out2, out3, out4, out5, out6, out7, out8 = listHospitals(incoming)
        message.body(out)
        if out2 != '':
            response.message().body(out2)
        if out3 != '':
            response.message().body(out3)
        if out4 != '':
            response.message().body(out4)
        if out5 != '':
            response.message().body(out5)
        if out6 != '':
            response.message().body(out6)
        if out7 != '':
            response.message().body(out7)
        if out8 != '':
            response.message().body(out8)
        responded = True

    if 'info' in incoming:
        print(incoming)
        out = getHospitalInfo(incoming)
        message.body(out)
        responded = True

    if not responded:
        out = listInstructions()
        message.body(out)

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)  # not ideal for production setting, change later
