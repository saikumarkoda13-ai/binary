from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm


# ================= HOME PAGE =================
def index(request):
    return render(request, 'index.html')


# ================= ADMIN LOGIN =================
def AdminLogin(request):
    return render(request, 'AdminLogin.html')


# ================= ADMIN LOGIN CHECK =================
def AdminLoginCheck(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "admin":
            request.session["admin"] = username
            messages.success(request, "Admin Login Successful")
            return redirect("AdminHome")
        else:
            messages.error(request, "Invalid Admin Login")
            return redirect("AdminLogin")

    return redirect("AdminLogin")


# ================= ADMIN HOME =================
def AdminHome(request):

    if "admin" not in request.session:
        return redirect("AdminLogin")

    return render(request, "admins/AdminHome.html")


# ================= ADMIN LOGOUT =================
def AdminLogout(request):
    request.session.flush()
    messages.success(request, "Admin Logged Out Successfully")
    return redirect("AdminLogin")


# ================= USER LOGIN =================
def UserLogin(request):
    return render(request, 'UserLogin.html')


# ================= USER REGISTER =================
def UserRegister(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful. Please Login.")
            return redirect('UserLogin')

        else:
            messages.error(request, "Registration Failed. Please check details.")

    else:
        form = UserRegistrationForm()

    return render(request, 'UserRegister.html', {'form': form})


# ================= MNIST PAGE =================
def MnistTorchQNN(request):
    return render(request, 'users/MnistTorchQNN.html')