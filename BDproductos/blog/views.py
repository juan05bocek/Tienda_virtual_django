from django.shortcuts import render, redirect
from blog.form import Formulariopost
from django.contrib import messages
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {'posts':posts})

def crear_post(request):
    if request.method == "POST":
        form = Formulariopost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get("titulo")
            messages.success(request, f"El post {titulo} se ha creado exitosamente")
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error.messages[msg])
    form = Formulariopost()
    return render(request, "crear_post.html", {"form": form})