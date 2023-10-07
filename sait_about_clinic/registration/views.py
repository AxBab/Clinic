from django.shortcuts import render
from .models import Registers
from django.http import HttpResponseRedirect, HttpResponse

def registration(request):
    return render(request, 'registration/registration.html')

def user_authentication(request):
    return render(request, 'registration/user_authentication.html')


def user_profile(request):
    # Вход в аккаунт при помощи куки
    if request.COOKIES.get('user_id') and (request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/?' or 
                                           request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000'):
        user = Registers.objects.get(pk = request.COOKIES.get('user_id'))
        return render(request, 'registration/user_profile.html', {"user": user})


    # Регистрация
    elif request.method == 'POST' and request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/registration/?':
        try:
            if request.POST['pol_boy']:
                print(request.POST['pol_boy'])
                pol = 'Мужчина'
        except:
            try:
                if request.POST['pol_girl']:
                    pol = 'Женщина'
            except:
                pol = "Нет данных"
        
        if int(request.POST['age']) >= 11 and int(request.POST['age']) <= 19:
            age = request.POST['age'] + ' лет'
        elif int(request.POST['age'][-1]) > 4 or int(request.POST['age'][-1]) == 0:
            age = request.POST['age'] + ' лет'
        elif int(request.POST['age'][-1]) == 1:
            age = request.POST['age'] + ' год'
        elif int(request.POST['age'][-1]) <= 4:
            age = request.POST['age'] + ' года'

        Registers.objects.create(name = request.POST['name'], surname = request.POST['surname'], pol = pol,
                                 age = age, phone = request.POST['phone'],
                                 email = request.POST['email'], password = request.POST['password'])
        
        return HttpResponseRedirect('/')


    # Вход в аккаунт и создание куки
    elif request.method == 'POST' and request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/registration/user_authentication?':
        if not request.COOKIES.get('user_id'):
            try:
                user = Registers.objects.get(name = request.POST['FIO'].split()[1], surname = request.POST['FIO'].split()[0],
                                         password = request.POST['password'])
            except:
                user = Registers.objects.get(name = request.POST['FIO'].split()[0], surname = request.POST['FIO'].split()[1],
                                         password = request.POST['password'])
            
            content = render(request, 'registration/user_profile.html', {"user": user})
            content.set_cookie('user_id', user.pk, 31_536_000)
            return content
            
        else:
            return HttpResponseRedirect('/')
    

    # Выход из аккаунта и удаление куки
    elif request.method == 'POST' and (request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/registration/user_profile?' or
                                       'http://127.0.0.1:8000/registration/user_profile'):
        sait = HttpResponseRedirect("/")
        sait.delete_cookie('user_id')
        return sait
    

    else:
        return HttpResponseRedirect("/registration/user_authentication?")
    
    






