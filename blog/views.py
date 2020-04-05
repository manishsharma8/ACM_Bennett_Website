from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import ContactForm, PostForm
from .models import Post
from django.forms import forms
from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# For Mail
from django.core.mail import send_mail
from acm_website.settings import EMAIL_HOST_USER


# Create your views here.

def HomePage(request):
    form = ContactForm(request.POST or None)
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    # postform = PostForm(request.POST, request.FILES)

    if form.is_valid():
        subject = str(form['subject'].value())
        message = str(form['text'].value())
        recepient = str(form['email'].value())
        send_mail(subject, 
            message, recepient, [EMAIL_HOST_USER], fail_silently = False)
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'index.html', context)


class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(generic.CreateView, mixins.LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm

class PostUpdateView(generic.UpdateView, mixins.LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('index')

class PostDraftView(generic.ListView):
    template_name = 'post_draft_list.html'
    model = Post
    login_url = '/login/'
    redirect_field_name = "post_draft_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)