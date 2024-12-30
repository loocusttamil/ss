from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Mock relay data (use actual hardware interface in production)
relay_status = {1: False, 2: False, 3: False, 4: False}

# View to control relay status
@csrf_exempt
def control_relay(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            relay_id = data['relay_id']
            status = data['status']

            if relay_id in relay_status:
                relay_status[relay_id] = status
                # Here, send the command to ESP32 (you could use requests to make HTTP requests to ESP32)
                # Example: requests.post('ESP32_IP_ADDRESS/relay', json={'relay_id': relay_id, 'status': status})

                return JsonResponse({'success': True, 'relay_id': relay_id, 'status': status})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid relay_id'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

# View to fetch relay statuses
def get_relay_status(request):
    return JsonResponse([
        {'relay_id': relay_id, 'status': status}
        for relay_id, status in relay_status.items()
    ], safe=False)





from django.shortcuts import render

# View to render HTML page
def relay_control_page(request):
    return render(request, 'relay_control.html')