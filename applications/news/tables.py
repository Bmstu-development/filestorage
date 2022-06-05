import django_tables2

from . import models


class TableStyleMeta:
    attrs = {
        "class": "table table-bordered",
    }
    template_name = "django_tables2/bootstrap4.html"


class PublicationTable(django_tables2.Table):
    actions = django_tables2.TemplateColumn(verbose_name='', template_name='news/cell_action.html')
    title = django_tables2.Column(verbose_name='Заголовок', orderable=False)
    created = django_tables2.DateTimeColumn(verbose_name='Дата публикации')

    class Meta(TableStyleMeta):
        model = models.Publication
        fields = 'title', 'created'
