from django.shortcuts import render, redirect
from blog.form import Formulariopost
from django.contrib import messages
from blog.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts/acceder/')
# Create your views here.
def index(request):
    listado__posts = Post.objects.all()
    paginator = Paginator(listado__posts,3)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, posts.paginator.num_pages +1) 
    return render(request, "blog.html", {'posts':posts, "paginas": paginas, "pagina_actual": pagina_actual})

@login_required(login_url='accounts/acceder/')
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

@login_required(login_url='accounts/acceder/')
def eliminar_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request, "El post que buscas no existe")
        return redirect('blog')

    if post.autor  != request.user:
        request.error(request, "No eres el autor de este post")
        return redirect('blog')

    post.delete()
    messages.success(request, f"El post {post.titulo} ha sido eliminado!")
    return redirect("blog")

