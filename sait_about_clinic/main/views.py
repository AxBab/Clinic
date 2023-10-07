from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def doctors(request):
    return render(request, 'main/doctors.html')
    
def list_services(request):
    return render(request, 'main/list_services.html')