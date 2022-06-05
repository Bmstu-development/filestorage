from django_tables2 import SingleTableView
from django.views.generic import DetailView

from . import models, tables


class NewsListView(SingleTableView):
    template_name = 'news/list.html'
    model = models.Publication
    table_class = tables.PublicationTable

    def get_queryset(self):
        fields = [
            'title',
            'created'
        ]
        return super().get_queryset().only(*fields)


class NewsDetailView(DetailView):
    template_name = 'news/detail.html'
    model = models.Publication
