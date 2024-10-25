from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User

# Create your views here.
def login(request):
    return render(request,'login.html')

def Login(request):
    validation_error = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.filter(email=email).first()

            if user:
                if user.password == password:
                    # Store the user's ID in the session
                    request.session['user_id'] = user.id
                    request.session['user_type'] = 'Admin' if user.isAdmin else 'Adopter'

                    # Redirect to appropriate page after successful login
                    return redirect('adopter_pet_list')
                else:
                    validation_error = 'Invalid password'
            else:
                validation_error = 'Email does not exist'
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'validation': validation_error,
        'title_text': 'Login',
        'submit_text': 'Log in',
        'redirect_message': "Don't have an account?",
        'redirect_title': 'Sign up',
        'redirect_link': 'adopter_register'
    })

def Register(request): 
    validation_error = None

    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            contact_no = form.cleaned_data['contact_no']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            user = User.objects.filter(email = email)

            if(not user.exists()):
                if(password == confirm_password):
                    userType = 'Adopter'

                    
                    regUser = User.objects.create(
                        first_name = first_name,
                        last_name = last_name,
                        age = age,
                        contact_no = contact_no,
                        address = address,
                        email = email,
                        password = password,)
                    
                    return redirect(login)
                else:
                    validation_error = 'Password and Confirm Password are not the same'
            else:
                validation_error = 'Email already exists'

    else:
        form = RegisterForm()

    return render(request, 'login.html', {'form': form, 'validation': validation_error, 'title_text': 'Register', 'submit_text': "Sign up", 'redirect_message': 'Already have an account?', 'redirect_title': 'Log in', 'redirect_link': 'login'})