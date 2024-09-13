from django.shortcuts import get_object_or_404
from django.utils.http import urlencode

from django.db.models import Q
from django.views.generic import ListView, DetailView

from webapp.forms import SearchForm
from webapp.models import Part, Country

class BasePartView(ListView):
    model = Part
    paginate_by = 12
    ordering = ['-price']

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(price__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        context["countries"] = Country.objects.all()
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context

class PartsListView(BasePartView):
    context_object_name = 'parts'
    template_name = 'part/index.html'

class PartsByCountryView(BasePartView):
    context_object_name = 'parts_by_country'
    template_name = 'part/parts_by_country.html'

    def get_queryset(self):
        country = get_object_or_404(Country, pk=self.kwargs['pk'])
        return Part.objects.filter(vehicle_info__countries=country).order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = get_object_or_404(Country, pk=self.kwargs['pk'])
        return context

class PartsDetailView(DetailView):
    model = Part
    context_object_name = 'part'
    template_name = 'part/parts_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        part_category = self.object.category
        related_parts = Part.objects.filter(category=part_category).exclude(pk=self.object.pk)[:5]  # Получаем похожие запчасти по категории
        context['related_parts'] = related_parts
        context['category'] = part_category

        return context







