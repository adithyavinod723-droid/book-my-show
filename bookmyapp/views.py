from django.shortcuts import render
from .models import UserRegister,Movie


# Home page (MOVIES)
def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')
        print(profile_pic)

        UserRegister.objects.create(
            name=name,
            email=email,
            password=password,
            profile_pic=profile_pic
        )
        print(hrloo)
        return redirect('home')

    return render(request, 'register.html')
# # Create your views here.

from django.shortcuts import render, redirect
from .models import UserRegister

# Home Page

def home(request):
    return render(request, 'home.html')

# Register Page
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        UserRegister.objects.create(
            name=name,
            email=email,
            password=password,
            profile_pic=profile_pic
        )

        return redirect('login')

    return render(request, 'register.html')
# Login Page
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserRegister.objects.get(
                email=email,
                password=password
            )
            request.session['email'] = user.email

            return redirect('home')

        except UserRegister.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'login.html')
from django.shortcuts import render, redirect
from .models import UserRegister

def profile(request):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = UserRegister.objects.get(email=email)

    return render(request, 'profile.html', {
        'user': user
    })
def edit_profile(request):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = UserRegister.objects.get(email=email)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')

        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES.get('profile_pic')

        user.save()

        request.session['email'] = user.email

        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': user})

def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')

        Movie.objects.create(
            name=name,
            image=image
        )

        return redirect('home')

    return render(request, 'add-movie.html')
