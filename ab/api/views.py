from django.http import JsonResponse
from django.shortcuts import render
import datetime

def get_data(request):
    # Generate the message
    msg = 'Hi'
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    if hour < 12:
        msg += ', GOOD MORNING'
    else:
        msg += ', GOOD EVENING'
    s = msg
    t= datetime.datetime.now().strftime("%I:%M:%S %p")
    # JSON data to return
    data = {
        "message": "chella_kutty, Hello from SASTIKA_SRI",
        "status":s+"  -----   "+ "["+t+"]",
        "name": "laddu",
        "value": "100"
    }
    
    return JsonResponse(data)
class MockRequest:
    pass


request = MockRequest()


response = get_data(request)

dd=response.content.decode('utf-8')

print(dd)








def get_data_html(request):
    # Generate the message
    msg = 'Hi'
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    if hour < 12:
        msg += ', GOOD MORNING'
    else:
        msg += ', GOOD EVENING'
    s = msg
    t= datetime.datetime.now().strftime("%I:%M:%S %p")
    # Data to render in HTML
    context = {
        "message": "chella_kutty, Hello from SASTIKA_SRI",
        "status": s,
        "name": "laddu",
        "value": t,
        "greeting": "welcome "
    }

    return render(request, 'data_display.html', context)







