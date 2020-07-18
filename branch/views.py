from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView
from branch.models import Branch
from organization.models import Organization
from .forms import BranchForm
from django.urls import reverse_lazy

# Create your views here.


class BranchList(TemplateView):
    model = Branch
    context_object_name = 'branch_list'
    template_name = 'branch/branch_list.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        paginator = Paginator(queryset, 10)  # Show 10 contacts per page
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return contacts

    def get_context_data(self, **kwargs):
        context = super(BranchList, self).get_context_data(**kwargs)
        context['branches'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class BranchDetails(DetailView):
    model = Branch
    template_name = 'branch/branch_details.html'


# class BranchCreate(CreateView):
#     model = Branch
#     form_class = BranchForm
#     template_name = 'branch/branch_create.html'

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#
#         return self.form_invalid(form)
#
#     def form_valid(self, form):
#         branch = Branch()
#         branch.organization = Organization.objects.get(id=self.request.POST.get('organization'))
#         branch.created_by = 1    # logged user
#         branch.branch_name = self.request.POST.get('branch_name')
#         branch.parent_id = self.request.POST.get('parent_id') if self.request.POST.get('parent_id') != "" else 0
#         branch.type = self.request.POST.get('type')
#         branch.city = self.request.POST.get('city')
#         branch.state = self.request.POST.get('state')
#         branch.country = self.request.POST.get('country')
#         branch.branch_code = self.request.POST.get('branch_code')
#         branch.branch_code = self.request.POST.get('branch_code')
#         branch.save()
#         return redirect('branch:branch_list')
#
#     def form_invalid(self, form):
#         return render(self.request, self.template_name, {'form': form})
#
#     def get_context_data(self, **kwargs):
#         context = super(BranchCreate, self).get_context_data(**kwargs)
#         context["form"] = self.form_class
#         return context
class BranchCreate(CreateView):
    model = Branch
    form_class = BranchForm
    template_name = 'branch/branch_create.html'


    def get(self, request):
        form = BranchForm()

        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    def post(self, request):
        branch = Branch()
        branch.organization = Organization.objects.get(id=self.request.POST.get('organization'))
        branch.created_by = 1    # logged user
        branch.branch_name = self.request.POST.get('branch_name')
        branch.parent_id = self.request.POST.get('parent_id') if self.request.POST.get('parent_id') != "" else 0
        branch.type = self.request.POST.get('type')
        branch.city = self.request.POST.get('city')
        branch.state = self.request.POST.get('state')
        branch.country = self.request.POST.get('country')
        branch.branch_code = self.request.POST.get('branch_code')
        branch.branch_code = self.request.POST.get('branch_code')
        branch.save()
        return redirect('branch:branch_list')


def BranchUpdate(request, pk):
    branch = Branch.objects.get(pk=pk)

    form = BranchForm(request.POST or None, instance=branch)
    # return HttpResponse(form)
    if request.method == 'POST':

        if form.is_valid():
            branch.branch_name = request.POST.get('branch_name')
            branch.parent_id = request.POST.get('parent_id')
            branch.type = request.POST.get('type')
            branch.city = request.POST.get('city')
            branch.state = request.POST.get('state')
            branch.country = request.POST.get('country')
            branch.branch_code = request.POST.get('branch_code')
            branch.save()
            return redirect('branch:branch_list')


    else:
        form = BranchForm(instance=branch)
    return render(request, 'branch/branch_update.html', {'form': form, 'pk': pk})


def BranchDelete(request):

    branch = Branch.objects.get(id=request.POST.get('branchid'))
    branch.delete()
    return HttpResponse(True)

def branch_search(request):
    if request.method == 'GET':
        queryset = Branch.objects.all().order_by('-id')
        query = request.GET.get("q")
        if query:
                queryset = queryset.filter(
                Q(branch_name__icontains=query) |
                Q(branch_code__contains=query)
            ).distinct()
        paginator = Paginator(queryset, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
        branch = paginator.get_page(page)

    return render(request,"branch/branch_search.html",{"name":branch})
