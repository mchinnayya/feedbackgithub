from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, DeleteView
from role.models import Role, UserRole
from organization.models import Organization
from branch.models import Branch
from account.models import Account
from role.forms import RoleForm


# Create your views here.

class RoleList(TemplateView):
    model = Role
    context_object_name = 'role_list'
    template_name = 'role/role_list.html'

    # paginate_by = 10

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(role_name__contains=query)
            ).distinct()
        paginator = Paginator(queryset, 4)  # Show 25 contacts per page

        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)

        return contacts

    def get_context_data(self, **kwargs):
        context = super(RoleList, self).get_context_data(**kwargs)
        context['roles'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class RoleDetails(DetailView):
    model = Role
    template_name = 'role/role_details.html'


class RoleCreate(CreateView):
    model = Role
    fields = '__all__'
    form_class = RoleForm
    template_name = 'role/role_create.html'

    def get(self, request):
        form = RoleForm()

        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    def post(self, request):
        role = Role()
        role.organization = Organization.objects.get(id=1)
        role.branch = Branch.objects.get(id=1)
        role.role_name = self.request.POST.get('role_name')
        role.role_description = self.request.POST.get('role_description')
        role.save()
        return redirect('role:role_list')


def role_update(request, pk):
    role = Role.objects.get(pk=pk)
    form = RoleForm(request.POST or None, instance=role)
    if request.method == 'POST':
        if form.is_valid():
            role.role_name = request.POST.get('role_name')
            role.role_description = request.POST.get('role_description')
            role.save()
            return redirect('role:role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'role/role_update.html', {'form': form, 'pk': pk})


def role_delete(request):
    role = Role.objects.get(id=request.POST.get('roleid'))
    role.delete()
    return HttpResponse(True)
