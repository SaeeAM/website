from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Service, Dataform, joinus, track


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class ServiceListView(ListView):
    model = Service
    template_name = 'blog/service.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'allservice'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_message = "Project Create successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(SuccessMessageMixin,LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/project'
    success_message = "Project Delete successfully"
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def search(request):
    que= request.GET.get('search')
    context = Service.objects.all().filter(content__icontains=que)
    params = {'service':context, 'msg':""}
    if len(context) ==0 or len(que) ==0:
        params = {'msg':"Please make sure to enter relevent search"}
    return render(request, 'blog/search.html', params)

def home(request):
    name = request.GET.get('name')
    tray = track.objects.filter(bookid=name)
    params = {'tracks': tray, 'msg': ""}
    print(params)
    if len(tray) == 0 or len(name) <0:
        params = {'msg': "make sure not enter text only number"}
    return render(request, 'blog/index.html', params)


class serviceDetailView(DetailView):
    model = Service


class JoinusCreateView(SuccessMessageMixin, CreateView):
    model = joinus
    fields = ['name','email', 'mobile', 'message','resume']
    success_url = '/project'
    success_message = "Message Send was successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DataformCreateView(SuccessMessageMixin,CreateView):
    model = Dataform
    fields = ['name','phone', 'sender', 'message','servic', 'upload']
    success_url = '/service'
    success_message = "Service Booked successfully Booking Id Send You"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


