from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import FileData
from .forms import UploadForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
import os
from django.views import View
import datetime


# Create your views here.
messages = []

class Messages(object):
    def __init__(self,message):
        self.message = message

class Home(TemplateView):
    template_name = 'filelist.html'


def delete_file(request, pk):
    if request.method == 'POST':
        file = FileData.objects.get(pk=pk)
        name = os.path.basename(file.UploadedFile.name)
        file.delete()

        time = datetime.datetime.now()
        message = name + " deleted at " + str(time)
        messages.append(Messages(message))
    return redirect('file_list')


class FileListView(ListView,View):
    model = FileData
    template_name = 'filelist.html'
    context_object_name = 'files'






class FileUploadView(CreateView,View,SuccessMessageMixin):
    model = FileData
    form_class = UploadForm
    success_url = reverse_lazy('file_list')
    template_name = 'uploadfile.html'
    def post(self, request, *args, **kwargs):
        file = FileData(UploadedFile=request.FILES['UploadedFile'])
        file.save()
        name = os.path.basename(file.UploadedFile.name)
        time = datetime.datetime.now()
        message = name+" created at "+ str(time)
        messages.append(Messages(message))
        return redirect('file_list')





class FileUpdateview(UpdateView):
    model = FileData
    form_class = UploadForm
    message = ''

    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.GET)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.message = self.object
        return super().post(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        file = FileData.objects.get(pk=self.object.pk)
        time = datetime.datetime.now()
        nameprev = str(self.message)
        print(nameprev)

        namenow = os.path.basename(file.UploadedFile.name)
        message = nameprev + " updated to " + namenow + " at " + str(time)
        messages.append(Messages(message))
        return reverse_lazy('file_list')







def NotificationListView(request):

    return render(request, 'notifications.html', {'messages': messages})





