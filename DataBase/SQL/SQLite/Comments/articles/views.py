from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ArticleForm, CommentForm
from .models import Article, Comment


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 특정 게시글에 작성된 모든 댓글 조회 (역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def comments_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글인지 알려면 게시글 먼저 조회
    article = Article.objects.get(pk=article_pk)
    # comment 모델을 활용한 댓글
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 외래키 데이터를 넣으려면 댓글 인스턴스가 필요한데
        # 댓글 인스턴스는 save() 호출이 완료 되어야 반환됨
        # commit 키워드를 False로 바꾸면
        # 댓글 인스턴스는 생성하지만, DB에 저장 요청은 보내지 않고 대기
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form
    }
    return render(request, 'articles/deatil.html', context)


def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글이 삭제되는 것인지 조회
    comment = Comment.objects.get(pk=comment_pk)
    # [보조적인 방법] comment 인스턴스에서 article pk 가져오기
    # article_pk = comment.article.pk
    # 댓글 삭제
    comment.delete()
    return redirect('articles:detail', article_pk)