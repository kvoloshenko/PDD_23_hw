from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogapp.models import Hh_Response, Hh_Request
from blogapp.forms import Hh_Search_Form
from django.urls import reverse, reverse_lazy
from django.views.generic.base import ContextMixin
import hhru.all_data as ad
import pprint


# Create your views here.
def main_view(request):
    requests = Hh_Request.objects.all()
    return render(request, 'blogapp/index.html', context={'requests': requests})

def history(request):
    # обратная сортировка
    requests = Hh_Request.objects.order_by('id').reverse()
    responses = Hh_Response.objects.all()
    return render(request, 'blogapp/history.html', context={'requests': requests, 'responses': responses})


def create_result(request, id):
    # hh_request = Hh_Request.objects.last()
    hh_request = get_object_or_404(Hh_Request, id=id)
    responses = Hh_Response.objects.filter(request = hh_request)
    return render(request, 'blogapp/result.html', context={'hh_request': hh_request, 'responses': responses})

def create_form(request):
    form = Hh_Search_Form(request.POST)
    if form.is_valid():
        # Получить данные из фомры
        hh_query = form.cleaned_data['hh_query']
        hh_option = form.cleaned_data['hh_option']
        # print(type(hh_option), f' hh_option = {hh_option}')
        # обработка полученных данных
        # print(type(hh_query),f' hh_query = {hh_query}')

        if hh_option == 'all':
            keywords_s = f'{hh_query}'
        elif hh_option == 'company':
            keywords_s = f'COMPANY_NAME:({hh_query})'
        elif hh_option == 'name':
            keywords_s = f'NAME:({hh_query})'

        ad.set_keywords(keywords_s)
        result = ad.get_data(keywords_s)
        # print(type(result))
        # print(type(result[0]['requirements']))
        # pprint.pprint(result)
        keywords = result[0]['keywords']
        # print(f'keywords={keywords}')
        Hh_Request.objects.create(keywords = keywords)
        last_request = Hh_Request.objects.last()
        # print(f'last_request.id = {last_request.id}')

        requirements_l = result[0]['requirements']
        # print(type(requirements_l), f'requirements_l={requirements_l}')
        for item in requirements_l:
            # print(f'item={item}')
            # print(f'{item["name"]} {item["count"]} {round(int(item["persent"]))}')
            Hh_Response.objects.create(request=last_request,
                                       skill_name=item["name"],
                                       skill_count=item["count"],
                                       skill_persent=round(int(item["persent"])))
        #  подготовка для отображения на странице result.html
        hh_request = get_object_or_404(Hh_Request, id=last_request.id)
        responses = Hh_Response.objects.filter(request=hh_request)
        return render(request, 'blogapp/result.html', context={'hh_request': hh_request, 'responses': responses})
    else:
        return render(request, 'blogapp/form.html', context={'form': form})

    return render(request, 'blogapp/form.html', context={'form':form})


def create_contacts(request):
    dev_name = 'Konstantin Voloshenko'
    creation_date = 'Июнь 2022'
    return render(request, 'blogapp/contacts.html', context={'dev_name': dev_name, 'creation_date': creation_date})

# CRUD CREATE, READ (LIST, DETAIL), UPDATE, DELETE
# Read List: Список запросов
class Hh_RequestListView(ListView):
    model = Hh_Request
    template_name = 'blogapp/req_list.html'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        # return Hh_Request.objects.all()
        return Hh_Request.objects.order_by('id').reverse()

class ResponsesContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        hh_request = kwargs['object']
        responses = Hh_Response.objects.filter(request=hh_request)
        context = super().get_context_data(*args, **kwargs)
        context['responses'] = responses
        return context

# Read Detail
class Hh_RequestDetailView(DetailView, ResponsesContextMixin):
    model = Hh_Request
    template_name = 'blogapp/req_detail.html'
# Create
class  Hh_RequestCreateView(CreateView):
    fields = '__all__'
    model = Hh_Request
    success_url = reverse_lazy('blog:req_list')
    template_name = 'blogapp/req_create.html'

# Update
class Hh_RequestUpdateView(UpdateView, ResponsesContextMixin):
    fields = '__all__'
    model = Hh_Request
    success_url = reverse_lazy('blog:req_list')
    template_name = 'blogapp/req_update.html'
# Delete
class Hh_RequestDeleteView(DeleteView):
    fields = '__all__'
    model = Hh_Request
    success_url = reverse_lazy('blog:req_list')
    template_name = 'blogapp/req_delete.html'

