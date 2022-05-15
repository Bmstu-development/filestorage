from django_tables2 import SingleTableView
from django.views.generic import DetailView

from . import models, tables


class NewsListView(SingleTableView):
    template_name = 'news/list.html'
    model = models.Publication
    table_class = tables.PublicationTable


class NewsDetailView(DetailView):
    pass
