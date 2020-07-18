from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView
from account.models import Account
from organization.models import Organization
from account.forms import AccountForm, UserRoleForm
from django.urls import reverse_lazy
from account.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from role.models import UserRole


# Create your views here.

class AccountUserList(TemplateView):
    model = Account
    context_object_name = 'accountuser_list'
    template_name = 'account/accountuser_list.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        paginator = Paginator(queryset, 10)  # Show 10 contacts per page
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return contacts

    def get_context_data(self, **kwargs):
        context = super(AccountUserList, self).get_context_data(**kwargs)
        context['accountusers'] = self.get_queryset()
        context['role_form'] =  UserRoleForm(self.request.POST or None)
        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class AccountUserDetails(DetailView):

    model = Account
    form_class = AccountForm
    template_name = "account/accountuser_details.html"


    def get(self, request, pk):

        user_details = User.objects.get(id=pk)
        account_user = Account.objects.get(user=pk)

        context = {
            'user_details': user_details,
            'account_user': account_user

        }

        return render(request, self.template_name, context)

class AccountCreate(CreateView):
    model = User, Account
    fields = '__all__'
    form_class = AccountForm, UserForm
    template_name = 'account/accountuser_create.html'

    def get(self, request):
        accountform = AccountForm()
        userform = UserForm()

        context = {
            'account_form': accountform,
            'user_form': userform
        }
        return render(self.request, self.template_name, context)

    def post(self, request):
        user = User()
        user.username = self.request.POST.get('username')
        user.first_name = self.request.POST.get('first_name')
        user.last_name = self.request.POST.get('last_name')
        user.email = self.request.POST.get('email')
        user.password = make_password(self.request.POST.get('password'))
        user.save()

        account = Account()
        account.user = user
        account.organization = Organization.objects.get(id=request.POST.get('organization'))
        account.mobile = self.request.POST.get('mobile')
        account.gender = self.request.POST.get('gender')
        account.start_date = self.request.POST.get('start_date')
        account.end_date = self.request.POST.get('end_date')
        account.role = self.request.POST.get('role')
        account.save()
        return redirect('account:accountuser_list')


def account_user_update(request, pk):
    user = User.objects.get(id=pk)
    account = Account.objects.get(user=pk)
    user_form = UserForm(request.POST or None, instance=user)
    user_account_form = AccountForm(request.POST or None, instance=account)
    if request.method == 'POST':
        if user_form.is_valid():
            user.username = request.POST.get('username')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.password = make_password(request.POST.get('password'))
            user.save()
        if user_account_form.is_valid():
            account.mobile = request.POST.get('mobile')
            account.gender = request.POST.get('gender')
            account.start_date = request.POST.get('start_date')
            account.end_date = request.POST.get('end_date')
            account.role = request.POST.get('role')
            account.save()
        return redirect('account:accountuser_list')
    else:
        user_form = UserForm(instance=user)
        user_account_form = AccountForm(instance=account)
    return render(request, 'account/accountuser_update.html', {'user_form':user_form, 'user_account_form':user_account_form})

def delete_user_details(request):

    account = Account.objects.get(id=request.POST.get('accountid'))
    account.delete()
    user = User.objects.get(id=request.POST.get('userid'))
    user.delete()
    return HttpResponse(True)

def account_search(request):
    if request.method == 'GET':
        queryset = Account.objects.all().order_by('-id')
        query = request.GET.get("q")
        if query:
                queryset = queryset.filter(
                Q(username__icontains=query) |
                Q(mobile__icontains=query) |
                Q(first_name__icontains=query)
            ).distinct()
        paginator = Paginator(queryset, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        account = paginator.get_page(page)

    return render(request,"account/account_search.html",{"name":account})

def role_assign(request):
    user_role = UserRole.objects.get(id=request.POST.get('role'))
    role_form = UserRoleForm(request.POST or None, instance=user_role)
    if request.method == 'POST':
        if role_form.is_valid():
            user_role.role = request.POST.get('role')
            user_role.save()
            return redirect('account:accountuser_list')
    else:
        role_form = UserRoleForm(instance=user_role)
    return render(request, 'account/accountuser_list.html', {'role_form': role_form})


def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            user_detail = User.objects.filter(username__iexact=username).first()
            user_id = user_detail.id
            account_detail = Account.objects.filter(user__exact=user_id).first()
            # role = account_detail.role
            # request.session['role'] = role
            return redirect('dynamicform:dynamicform_list')
        else:
            data['error'] = "Your email and password didn't match. Please try again."
            return render(request, 'account/account_login.html', data)
    return render(request, 'account/account_login.html')


@login_required(redirect_field_name='my_redirect_field', login_url='/accounts/login')
def log_out(request):
    logout(request)
    request.session.flush()
    return redirect('account:login')
