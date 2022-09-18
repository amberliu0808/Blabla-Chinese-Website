from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from website.models import Blog, Category, Tag
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.mail import send_mail


# Create your views here.
def home(request):
    blog_posts = Blog.objects.order_by('-created_time')[:3]
    blog_post1 = blog_posts[0]
    blog_post2 = blog_posts[1]
    blog_post3 = blog_posts[2]

    context = {'blog_post1': blog_post1, 'blog_post2': blog_post2, 'blog_post3': blog_post3}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            ['amberliu0808@foxmail.com', 'amber08gf@gmail.com'],
            fail_silently=False,
        )

        context = {'name': name, 'blog_post1': blog_post1, 'blog_post2': blog_post2, 'blog_post3': blog_post3}
        return render(request, 'index.html', context)
    else:
        return render(request, "index.html", context)


# def blog(request):
# blogs = Blog.objects.all()
# context = {'blogs': blogs}
# return render(request, 'blog.html', context)
# ordering = ['-created_time']
# Codemy用ListView可以用，不用View怎么实现?


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    ordering = ['-created_time']

    def get_context_data(self, *args, **kwargs):
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['cats_list'] = category_list
        context['tag_list'] = tag_list
        return context

    paginate_by = 5


# def blogpost(request, slug):
# blog = Blog.objects.filter(slug=slug).first()
# context = {'blog': blog}
# return render(request, 'blog-details.html', context)
# return HttpResponse(f'you are viewing {slug}')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-details.html'

    def get_context_data(self, *args, **kwargs):
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context['cats_list'] = category_list
        context['tag_list'] = tag_list
        return context


def Categories(request, cats):
    categories_posts = Blog.objects.filter(category=cats.title().replace('-', ' ')).order_by('-created_time')
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    # test = ['1', '2', '3', '4', '5', '6', '7', '8']
    # paginator = Paginator(test, 2)
    paginator = Paginator(categories_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'categories_posts': categories_posts, 'cats': cats.title().replace('-', ' '), 'cats_list': category_list,
               'tag_list': tag_list, 'page_obj': page_obj}
    return render(request, 'categories.html', context)
    # return HttpResponse(f'You are viewing {cats}')


def Tags(request, tag):
    tags_posts = Blog.objects.filter(tag=tag.title().replace('-', ' ')).order_by('-created_time')
    tag_list = Tag.objects.all()
    category_list = Category.objects.all()

    paginator = Paginator(tags_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'tags_posts': tags_posts, 'cats': tag.title().replace('-', ' '), 'tag_list': tag_list,
               'cats_list': category_list, 'page_obj': page_obj}
    return render(request, 'tags.html', context)
    # return HttpResponse(f'You are viewing {cats}')


class AddPostView(CreateView):
    model = Blog
    form_class = PostForm
    template_name = 'add-post.html'

    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Blog
    form_class = UpdatePostForm
    template_name = 'update-post.html'
    # fields = ['title', 'content', 'shortcut', 'slug']


class DeletePostView(DeleteView):
    model = Blog
    template_name = 'delete-post.html'
    success_url = reverse_lazy('blog')
