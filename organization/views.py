from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView
from organization.models import Organization
from organization.forms import OrganizationForm
from django.urls import reverse_lazy

# Create your views here.

class OrganizationList(TemplateView):
    model = Organization
    context_object_name = 'organization:organization_list'
    template_name = 'organization/organization_list.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        paginator = Paginator(queryset, 10)  # Show 10 contacts per page
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return contacts

    def get_context_data(self, **kwargs):
        context = super(OrganizationList, self).get_context_data(**kwargs)
        context['organizations'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class OrganizationDetails(DetailView):
    model = Organization
    template_name = 'organization/organization_details.html'


class OrganizationCreate(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/organization_create.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        organization = Organization()
        organization.organization_name = self.request.POST.get('organization_name')
        organization.created_by = 1    # logged user
        organization.city = self.request.POST.get('city')
        organization.state = self.request.POST.get('state')
        organization.country = self.request.POST.get('country')
        organization.save()
        return redirect('organization:organization_list')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super(OrganizationCreate, self).get_context_data(**kwargs)
        context["form"] = self.form_class
        return context


def OrganizationUpdate(request, pk):
    organization = Organization.objects.get(pk=pk)

    form = OrganizationForm(request.POST or None, instance=organization)
    if request.method == 'POST':

        if form.is_valid():
            organization.organization_name = request.POST.get('organization_name')
            organization.created_by = request.POST.get('created_by')
            organization.city = request.POST.get('city')
            organization.state = request.POST.get('state')
            organization.country = request.POST.get('country')
            organization.save()
            return redirect('organization:organization_list')


    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'organization/organization_update.html', {'form': form, 'pk': pk})


def OrganizationDelete(request):
    organization = Organization.objects.get(id=request.POST.get('organizationid'))
    organization.delete()
    return HttpResponse(True)

def organization_search(request):
    if request.method == 'GET':
        queryset = Organization.objects.all().order_by('-id')
        query = request.GET.get("q")
        if query:
                queryset = queryset.filter(Q(organization_name__icontains=query) |
                                          Q(city__icontains=query)).distinct()
        paginator = Paginator(queryset, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        organization = paginator.get_page(page)

    return render(request,"organization/organization_search.html",{"name":organization})