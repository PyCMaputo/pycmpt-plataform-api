from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from .forms import RegisterForm, UserAdminCreationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer


def account(request):
    pass


def create_account(request):
    data = dict()
    if request.method == "POST":
        form = UserAdminCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("url_home")

    data['form'] = UserAdminCreationForm()
    return render(request, 'accounts/singup.html', data)


def login_view(request):
    proximo = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if request.POST['url_next'] != 'None':
                caminho = request.POST['url_next']
                return redirect(caminho)
            return redirect('url_home')
        else:
            # Return an 'invalid login' error message.
            return redirect('url_login')
    else:
        proximo['prox'] = request.GET.get('next')
        return render(request, 'accounts/login.html', proximo)


def logout_view(request):
    logout(request)
    return redirect('url_login')


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
'''

'''
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
'''