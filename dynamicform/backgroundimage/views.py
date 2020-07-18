from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from .forms import FeedbackBackgroundImageForm
from dynamicform.models import FeedbackBackgroundImage, DynamicFormMaster



class BackgroundImageList(View):
    template_name = 'backgroundimage/backgroundimage_list.html'

    def get(self,request,formmasterid=None):
        list = FeedbackBackgroundImage.objects.filter(form_master_id=formmasterid)
        return render(request,self.template_name,{'list':list, 'formmasterid': formmasterid})

class BackgroundImageCreate(CreateView):
    model = FeedbackBackgroundImage
    fields = ('image_title', 'image_name', 'imageUrl')
    form_class = FeedbackBackgroundImageForm
    template_name = 'backgroundimage/backgroundimage_create.html'

    def get(self, request, formmasterid):
        imageform = FeedbackBackgroundImageForm()

        context = {
            'imageform': imageform,
            'formmasterid': formmasterid,

        }
        return render(self.request, self.template_name, context)

    def post(self, request, formmasterid):
        form=FeedbackBackgroundImageForm(request.POST,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.form_master_id=formmasterid
            data.save()

        # backgroundimage = FeedbackBackgroundImage()
        # print( self.request.POST.get('imageUrl'))
        # backgroundimage.form_master = DynamicFormMaster.objects.filter(id__iexact=formmasterid).first()
        # backgroundimage.image_title = self.request.POST.get('image_title')
        # backgroundimage.image_name = self.request.POST.get('image_name')
        # backgroundimage.imageUrl = self.request.POST.get('imageUrl')
        # backgroundimage.save()

        return redirect('dynamicform:backgroundimage:backgroundimage_list', formmasterid)


def backgroundimage_delete(request):
    imageform = FeedbackBackgroundImage.objects.get(id=request.POST.get('backgroundimageid'))
    imageform.delete()
    return HttpResponse(True)
