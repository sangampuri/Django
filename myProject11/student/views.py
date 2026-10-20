from django.shortcuts import redirect, render
from .forms import StudentForm
# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})
