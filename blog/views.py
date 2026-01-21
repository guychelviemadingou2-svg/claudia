from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .forms import ArticleForm, CommentForm, SignUpForm
from .models import Article, Comment


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['parent_comments'] = self.object.comments.filter(parent__isnull=True)
        return context


@method_decorator(login_required, name='dispatch')
class ArticleCreateView(View):
    template_name = 'blog/article_form.html'

    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form, 'title': 'Nouvel article'})

    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article publié avec succès !')
            return redirect('article_detail', pk=article.pk)
        return render(request, self.template_name, {'form': form, 'title': 'Nouvel article'})


@method_decorator(login_required, name='dispatch')
class ArticleUpdateView(UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Article mis à jour avec succès.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_staff

    def get_success_url(self):
        messages.success(self.request, 'Article supprimé avec succès.')
        return reverse('article_list')


@login_required
def toggle_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.likes.all():
        article.likes.remove(request.user)
        messages.info(request, 'Like retiré.')
    else:
        article.likes.add(request.user)
        messages.success(request, 'Vous avez aimé cet article.')
    return redirect(request.META.get('HTTP_REFERER', reverse('article_detail', kwargs={'pk': pk})))


@login_required
def add_comment(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        parent_id = request.POST.get('parent_id')
        parent_comment = Comment.objects.filter(id=parent_id, article=article).first() if parent_id else None

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.parent = parent_comment
            comment.save()
            messages.success(request, 'Commentaire publié avec succès.')
        else:
            messages.error(request, 'Erreur lors de la publication du commentaire.')
    return redirect('article_detail', pk=pk)


class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('article_list')
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('article_list')
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} ! Votre compte a été créé avec succès.')
            return redirect('article_list')
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté. À bientôt !')
    return redirect('article_list')
