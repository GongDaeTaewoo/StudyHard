from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from blog.forms import StudyPostForm, ReferPostForm, MemoPostForm
from blog.models import Study, Reference, Memo


def home(request):
    partial_study_post = Study.objects.all().order_by('-created_at')[0:7]
    partial_refer_post = Reference.objects.all().order_by('-created_at')[0:3]
    context = {'study_post': partial_study_post, 'refer_post': partial_refer_post}
    return render(request, 'blog/home.html', context=context)


def study_list(request):
    post_list = Study.objects.all()
    return render(request, 'blog/study_list.html', context={'post_list': post_list})


def study_detail(request, pk):
    post = get_object_or_404(Study, pk=pk)
    context = {'post': post}
    return render(request, 'blog/study_detail.html', context=context)


def study_create(request):
    if request.method == "POST":
        form = StudyPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect(post)
    else:
        form = StudyPostForm()
    return render(request, 'blog/study_create.html', {'form': form})


def study_update(request, pk):
    post = get_object_or_404(Study, pk=pk)

    if request.method == "POST":
        form = StudyPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            redirect(post)
    else:
        form = StudyPostForm(instance=post)
    return render(request, 'blog/study_update.html', {'form': form})


def study_delete(request, pk):
    post = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog:study_delete')
    else:
        return render(request, 'blog/study_delete_confirm.html')


class ReferList(ListView):
    model = Reference
    template_name = 'blog/refer_list.html'
    context_object_name = 'post_list'


refer_list = ReferList.as_view()


class ReferDetail(DetailView):
    model = Reference
    template_name = 'blog/refer_detail.html'
    context_object_name = 'refer_post'


refer_detail = ReferDetail.as_view()


class ReferCreate(CreateView):
    model = Reference
    form_class = ReferPostForm
    template_name = 'blog/refer_create.html'
    context_object_name = 'refer_form'


refer_create = ReferCreate.as_view()


class ReferDelete(DeleteView):
    model = Reference
    template_name = 'refer_delete_confirm.html'


refer_delete = ReferDelete.as_view()


class MemoList(ListView):
    model = Memo
    template_name = 'blog/memo_list.html'
    context_object_name = 'memo_list'


memo_list = MemoList.as_view()


class MemoCreate(CreateView):
    model = Memo
    form_class = MemoPostForm
    template_name = 'blog/Memo_create.html'
    context_object_name = 'Memo_form'


memo_create = MemoCreate.as_view()


class MemoDelete(DeleteView):
    model = Memo
    template_name = 'memo_delete_confirm.html'


memo_delete = MemoDelete.as_view()
