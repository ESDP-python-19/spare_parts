from django.shortcuts import render
from .forms import SearchForm
from .models.car import CarBrand
from .models.part import Part
from .models.vehicleinfo import VehicleInfo


def search_view(request):
    form = SearchForm(request.GET or None)  # здесь получаем поисковый запрос
    query = request.GET.get('query', '')  # здесь извлекаем строку запроса

    part_results = Part.objects.none()  # пустой queryset для запчастей
    vehicle_results = VehicleInfo.objects.none()  # пустой queryset для транспортных средств
    car_results = CarBrand.objects.none() # для машин

    if query:
        part_results = Part.objects.filter(name__icontains=query)  # фильтрация по названию запчасти
        vehicle_results = VehicleInfo.objects.filter(
            model__name__icontains=query # фильтрация по модели транспортного средства
        )
        car_results = CarBrand.objects.filter(name__icontains=query)


    context = {
        'form': form,
        'part_results': part_results,
        'car_brands': car_results,
        'vehicle_results': vehicle_results,
    }
    return render(request, 'search_results.html', context)
