from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from tf_idf.forms import FilesForm
from tf_idf.utils import compute_tf_idf, trunc_str


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'tf_idf/index.html', {'form': FilesForm()})


class TfIdfListView(ListView):
    paginate_by = 20
    queryset = None
    file_names = None
    template_name = 'tf_idf/table.html'
    allow_empty = True

    def post(self, request):
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data['files']
            corpus = [f.file for f in cd]
            words, tf_idf_array = compute_tf_idf(corpus)

            queryset = [[word] + row for word, row in zip(words, tf_idf_array)]
            self.update_queryset(queryset)

            file_names = [trunc_str(f.name) for f in cd]
            self.update_file_names(file_names)
            return redirect('tf_idf:process_form')
        return HttpResponseRedirect('tf_idf:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_names'] = self.file_names

        page = context.get('page_obj')
        rows_counter_start = 0
        if page is not None:
            rows_counter_start = (page.number - 1) * self.paginate_by
        context['rows_counter_start'] = rows_counter_start
        return context

    @classmethod
    def update_queryset(cls, queryset):
        cls.queryset = queryset

    @classmethod
    def update_file_names(cls, file_names):
        cls.file_names = file_names
