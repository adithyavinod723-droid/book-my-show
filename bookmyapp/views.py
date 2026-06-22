from django.shortcuts import render,redirect
from .models import UserRegister,Movie


# Home page (MOVIES)
def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, 'index.html', {'movies': movies})



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
    movies = Movie.objects.all()
    return render(request, 'home.html', {
        'movies': movies
    })

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
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = UserRegister.objects.get(email=email)

    if request.method == "POST":
        Movie.objects.create(
            user=user,
            name=request.POST.get('name'),
            genre=request.POST.get('genre'),
            duration=request.POST.get('duration'),
            image=request.FILES.get('image'),
            video=request.FILES.get('video')
        )

        return redirect('home')

    return render(request, 'add-movie.html')

def edit_movie(request, id):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = UserRegister.objects.get(email=email)

    movie = Movie.objects.get(id=id, user=user)
    movie.genre = request.POST.get('genre')
    movie.duration = request.POST.get('duration')

    if request.FILES.get('video'):
        movie.video = request.FILES.get('video')

    if request.method == "POST":
        movie.name = request.POST.get('name')

        if request.FILES.get('image'):
            movie.image = request.FILES.get('image')
        if request.FILES.get('video'):
            movie.video = request.FILES.get('video')


        movie.save()

        return redirect('home')

    return render(request, 'edit_movie.html', {
        'movie': movie
    })
def my_movies(request):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = UserRegister.objects.get(email=email)

    movies = Movie.objects.filter(user=user)

    return render(request, 'my-movies.html', {
        'movies': movies
    })
def delete_movie(request, id):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = UserRegister.objects.get(email=email)

    movie = Movie.objects.get(id=id, user=user)

    movie.delete()

    return redirect('my_movies')
def logout(request):
    request.session.flush()
    return redirect('login')