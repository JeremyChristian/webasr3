from frontend.models import *
from frontend.serializers import *
from frontend.permissions import *
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from frontend import fabfile
import re
from fabric.api import *
import string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from frontend.forms import *

env.user="webasr"
env.hosts=['squeal.dcs.shef.ac.uk',]

env.password="asr4daweb"

@api_view(('GET',))
def api_root(request, format = None):
    return Response({
        'users': reverse('users', request=request, format=format),
        'uploads': reverse('uploads', request=request, format=format),
        'systems': reverse('systems', request=request, format=format),
        'signup': reverse('signup', request=request, format=format),
        'newupload': reverse('newupload', request=request,format=format),
        })

# class UploadList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('transcripts', 'audiofiles')
#     # renderer_classes = (TemplateHTMLRenderer,)

#     def get_queryset(self):
        
#         user = self.request.user
#         return Upload.objects.filter(user=user)
    
#     def list(self,request):
#         serializer = FinishedUploadSerializer(self.get_queryset(), many=True)

#         # date_start = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3}))[-:\\/.](?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'
#         # file_start = '.*?((?:[a-z][a-z\\.\\d_]+)\\.(?:[a-z\\d]{3}))(?![\\w\\.])'
#         # date_regex = re.compile(date_start,re.IGNORECASE|re.DOTALL)
#         # file_regex = re.compile(file_start,re.IGNORECASE|re.DOTALL)
        
#         # for x in serializer.data:

#         #     date_search = date_regex.search(x['created'])
#         #     file_search = file_regex.search(x['audiofiles'])
#         #     metafile_search = file_regex.search(x['metadata'])

#         #     if date_search:
#         #         x['date'] = date_search.group(1)
#         #     if file_search:
#         #         x['filename'] = file_search.group(1)
#         #     if metafile_search:
#         #         x['metaname'] = metafile_search.group(1)

#         # return Response({'somedata': serializer.data},template_name='frontend/uploadlist.html',)


# class UploadCreate(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = UploadSerializer
#     # renderer_classes = (TemplateHTMLRenderer,)
#     # template_name='frontend/newupload.html'
    
#     def get_queryset(self):
        
#         user = self.request.user
#         return Upload.objects.filter(user=user)

#     # def create(self,request):
#     #     serializer = UploadSerializer(self.get_queryset(), many=True)
#     #     return Response({'somedata': serializer.data},template_name='frontend/newupload.html',)

#     def perform_create(self, serializer):
#         print self.request.data
        
#         serializer.save(user=self.request.user)
#         # localpath = serializer.data.get('audiofiles')
#         # user = serializer.data.get('user')
#         # system = serializer.data.get('systems')
        
#         # pk = str(CustomUser.objects.get(email=user).id)
#         # n = 5 - len(pk)
#         # pk =  ('0' * n) + pk

#         # command = System.objects.get(name=system).command
       
#         # timestamp = ''.join(i for i in serializer.data.get('created') if i.isdigit())
#         # filename = 'src-'+pk+'_ses-'+timestamp
#         # channels = 1

#         # fabfile.process_execute(localpath,filename,channels,command)

# class UploadDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsOwner,)
#     queryset = Upload.objects.all()
#     serializer_class = FinishedUploadSerializer

# class SystemList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     # renderer_classes = (TemplateHTMLRenderer,)
#     queryset = System.objects.all()
#     serializer_class = SystemSerializer
#     # def list(self,request):
#     #     serializer = SystemSerializer(self.get_queryset(), many=True)
#     #     # date_start = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3}))[-:\\/.](?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'
#     #     # file_start = '.*?((?:[a-z][a-z\\.\\d_]+)\\.(?:[a-z\\d]{3}))(?![\\w\\.])'
#     #     # date_regex = re.compile(date_start,re.IGNORECASE|re.DOTALL)
#     #     # file_regex = re.compile(file_start,re.IGNORECASE|re.DOTALL)
        
#     #     # for x in serializer.data:

#     #     #     date_search = date_regex.search(x['added'])
#     #     #     file_search = file_regex.search(x['audiofiles'])
#     #     #     metafile_search = file_regex.search(x['metadata'])

#     #     #     if date_search:
#     #     #         x['date'] = date_search.group(1)
#     #     #     if file_search:
#     #     #         x['filename'] = file_search.group(1)
#     #     #     if metafile_search:
#     #     #         x['metaname'] = metafile_search.group(1)

#     #     return Response({'somedata': serializer.data},template_name='frontend/systemlist.html',)

# class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = System.objects.all()
#     serializer_class = SystemSerializer

# class UserList(generics.ListAPIView):
#     # permission_classes = (permissions.IsAuthenticated,permissions.IsAdminUser)
#     # renderer_classes = (TemplateHTMLRenderer,)
#     queryset = CustomUser.objects.all()
#     serializer_class = AdminUserSerializer
#     # def list(self,request):
#     #     serializer = AdminUserSerializer(self.get_queryset(), many=True)
#         # date_start = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3}))[-:\\/.](?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'
#         # file_start = '.*?((?:[a-z][a-z\\.\\d_]+)\\.(?:[a-z\\d]{3}))(?![\\w\\.])'
#         # date_regex = re.compile(date_start,re.IGNORECASE|re.DOTALL)
#         # file_regex = re.compile(file_start,re.IGNORECASE|re.DOTALL)
        
#         # for x in serializer.data:

#             # date_search = date_regex.search(x['created'])
#             # file_search = file_regex.search(x['audiofiles'])
#             # metafile_search = file_regex.search(x['metadata'])

#             # if date_search:
#             #     x['date'] = date_search.group(1)
#             # if file_search:
#             #     x['filename'] = file_search.group(1)
#             # if metafile_search:
#             #     x['metaname'] = metafile_search.group(1)

#         # return Response({'somedata': serializer.data},template_name='frontend/userlist.html',)
from django.views.generic.detail import DetailView
class UserDetail(DetailView):
    
    model = CustomUser

    def post(self,request,pk):
        if not request.user.is_staff:
            return HttpResponseRedirect('/login')
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        user = CustomUser.objects.filter(pk=pk)[0]
        if 'is_staff' in request.POST:
            user.is_staff = True
            user.save()
        else:
            user.is_staff = False
            user.save()
        if 'is_active' in request.POST:
            user.is_active = True
            user.save()
        else:
            user.is_active = False
            user.save()
        return HttpResponseRedirect('/user/'+pk+'/')

class UploadDetail(DetailView):
    model = Upload
     
    def get(self,request,pk):

        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        template = loader.get_template('frontend/upload_detail.html')
        audiofiles = Audiofile.objects.filter(upload=self.get_object())
        return HttpResponse(render(request,'frontend/upload_detail.html',{'audiofiles':audiofiles,'object':self.get_object()}))

class SystemDetail(DetailView):

    model = System
    def get(self,request,pk):
        if not request.user.is_staff:
            return HttpResponseRedirect('/login')
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        print self.get_object()
        template = loader.get_template('frontend/system_detail.html')
        form = SystemEditForm(instance=self.get_object())
        return HttpResponse(render(request,'frontend/system_detail.html',{'form':form,'object':self.get_object()}))

    def post(self,request,pk):
        form = SystemEditForm(instance=self.get_object(),data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/systems')
        else:
            return render(request, 'frontend/system_detail.html', {'form': form,'object':self.get_object()},)

    

# class UserCreate(generics.CreateAPIView):
#     serializer_class = NewUserSerializer
#     def perform_create(self, serializer):
#         serializer.save()

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# from frontend.forms import DocumentForm
# 
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import RequestContext, loader

class ListUser(View):
    def get(self,request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        if not request.user.is_staff:
            return HttpResponseRedirect('/login')
        users = CustomUser.objects.all()
        template = loader.get_template('frontend/listuser.html')
        context = RequestContext(request, {
        'users': users,
        })
        return HttpResponse(template.render(context))

            

def download(request,pk):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
    upload = Upload.objects.filter(pk=pk)
    response = HttpResponse(upload[0].transcripts, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename='+upload[0].created.isoformat()+'_Transcript.zip'
    return response
    

def create_system(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
    if not request.user.is_staff:
            return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = SystemForm(request.POST)
        print form
        if form.is_valid():
            system = System(
            name = form.cleaned_data['name'],
            language = form.cleaned_data['language'],
            environment = form.cleaned_data['environment'],
            command = form.cleaned_data['command'],
            )
            system.save()
            return HttpResponseRedirect('/systems')
    else:
        form = SystemForm()

    systemlist = System.objects.all()
    context = RequestContext(request, {
    'form': form,
    'systemlist': systemlist,
    })

    return render(request, 'frontend/systemlist.html', context)

def user_login(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return HttpResponseRedirect('/newupload')
    else:
        form = forms.AuthenticationForm()

    return render(request, 'frontend/authentication.html', {'form': form})

def user_edit(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = UserEditForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account')
        else:
            return render(request, 'frontend/user_edit.html', {'form': form})
    if request.method == 'GET':
        form = UserEditForm(instance=request.user)
        return render(request, 'frontend/user_edit.html', {'form': form})

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = UserCreationForm()

    return render(request, 'frontend/register.html', {'form': form})

class UpdateUpload(View):
    def post(self,request):
        print request.POST
        print request.FILES
        transcript = request.FILES.__getitem__('upload')
        userpk = request.POST.__getitem__('source').lstrip('0')
        
        session = request.POST.__getitem__('session')
        user = CustomUser.objects.filter(pk=userpk)
        
        uploads = Upload.objects.filter(user=user)
        print uploads
        for upload in uploads:
            timestamp = ''.join(i for i in upload.created.isoformat() if i.isdigit())
            print timestamp
            print session
            if timestamp == session:
                upload.transcripts = transcript
                upload.save()
                return HttpResponse('success\n')
        return HttpResponse('failure\n')
    # def get(self,request):
    #     testfiles = TestFile.objects.all()
    #     context = RequestContext(request, {
    #     'testfiles': testfiles,
    #     })
    #     template = loader.get_template('frontend/testfile.html')
    #     return HttpResponse(template.render(context))

import json   
from django.core import serializers
class CreateUpload(View):

    @csrf_exempt
    def post(self,request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        form = UploadForm(data=request.POST)
        if form.is_valid():
            upload = Upload(
                user = request.user,
                language = form.cleaned_data['language'],
                environment = form.cleaned_data['environment'],
                systems = form.cleaned_data['systems'],
            )

            if form.cleaned_data['metadata']:
                upload.metadata = form.cleaned_data['metadata']

            upload.save()

            localpaths = []

            print request.FILES

            for x in range(1,(len(request.FILES)+1)):
                try:
                    audioupload = Audiofile(audiofile = request.FILES.__getitem__('file'+str(x)), upload = upload)
                    audioupload.save()
                    localpaths.append(audioupload.audiofile.url)
                except:
                    pass

            message = Audiofile.objects.all()
            user = request.user
            system = upload.systems
            
            pk = str(CustomUser.objects.get(email=user).id)
            n = 5 - len(pk)
            pk =  ('0' * n) + pk

            command = System.objects.get(name=system).command
           
            timestamp = ''.join(i for i in upload.created.isoformat() if i.isdigit())
            filename = 'src-'+pk+'_ses-'+timestamp

            fabfile.process_execute(localpaths,filename,command)
            
            return HttpResponseRedirect('/newupload')

        else:
            systemObjects = System.objects.all()
            languages = set()
            systems = set()
            environments = set()
            for system in System.objects.all():
                languages.add(system.language)
                systems.add(system.name)
                environments.add(system.environment)
            uploadlist = Upload.objects.filter(user=request.user)
            uploads = []
            for upload in uploadlist:
                files = []
                for audiofile in Audiofile.objects.filter(upload = upload):
                    file_start = '(/[^/]*\.wav)'
                    file_regex = re.compile(file_start,re.IGNORECASE|re.DOTALL)
                    file_search = file_regex.search(audiofile.audiofile.url)
                    if file_search:
                        files.append(file_search.group(1))
                uploads.append((upload,files))
            template = loader.get_template('frontend/newupload.html')
            context = RequestContext(request, {
            'languages': languages,
            'systems': systems,
            'environments': environments,
            'uploads': list(reversed(uploads)),
            'systemObjects': systemObjects,
            'form':form,
            })
            return render(request, 'frontend/newupload.html', context)

        


        

        return HttpResponse(message)
    
    def get(self,request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        form = UploadForm()
        systemObjects = System.objects.all()
        languages = set()
        systems = set()
        environments = set()
        for system in System.objects.all():
            languages.add(system.language)
            systems.add(system.name)
            environments.add(system.environment)
        uploadlist = Upload.objects.filter(user=request.user)
        uploads = []
        for upload in uploadlist:
            files = []
            for audiofile in Audiofile.objects.filter(upload = upload):
                file_start = '(/[^/]*\.wav)'
                file_regex = re.compile(file_start,re.IGNORECASE|re.DOTALL)
                file_search = file_regex.search(audiofile.audiofile.url)
                if file_search:
                    files.append(file_search.group(1))
            uploads.append((upload,files))
        template = loader.get_template('frontend/newupload.html')
        context = RequestContext(request, {
        'languages': languages,
        'systems': systems,
        'environments': environments,
        'uploads': list(reversed(uploads)),
        'systemObjects': systemObjects,
        'form':form,
        })
        return HttpResponse(template.render(context))

class Authentication(View):
    def get(self,request):
        return HttpResponseRedirect('/login')

from django.contrib.auth import authenticate, login, forms




from django.contrib.auth import logout
class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login')

class Account(View):
    def get(self,request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        context = RequestContext(request,{
            'user': request.user,
        }) 
        return render(request,'frontend/account.html')

class RegistrationSuccess(View):
    def get(self,request):
        return render(request,'frontend/registration_success.html')

class About(View):
    def get(self,request):
        return render(request,'frontend/about.html')
class News(View):
    def get(self,request):
        return render(request,'frontend/news.html')
class Conditions(View):
    def get(self,request):
        return render(request,'frontend/conditions.html')
class Projects(View):
    def get(self,request):
        return render(request,'frontend/projects.html')
class Research(View):
    def get(self,request):
        return render(request,'frontend/research.html')
class Publications(View):
    def get(self,request):
        return render(request,'frontend/publications.html')


# @api_view(['GET', 'POST'])
# def upload_list(request,format = 'html',):
   
#     if request.method == 'GET':
#         uploads = Upload.objects.all()
#         serializer = UploadSerializer(uploads, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UploadSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def upload_detail(request, pk, format = 'html'):
  
#     try:
#         upload = Upload.objects.get(pk=pk)
#     except Upload.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UploadSerializer(upload)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = UploadSerializer(upload, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         upload.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET', 'POST'])
# def system_list(request,format = 'html'):
   
#     if request.method == 'GET':
#         systems = System.objects.all()
#         serializer = SystemSerializer(systems, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SystemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def system_detail(request, pk, format = 'html'):
  
#     try:
#         system = System.objects.get(pk=pk)
#     except System.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SystemSerializer(upload)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SystemSerializer(system, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     system.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)