from django.shortcuts import render ,redirect
from django.views.generic import TemplateView,View,DetailView
from photos.models import Category,Photo

# Create your views here.


class GalleryHomeView(View):
    def get(self,request,*args,**kwargs):
        category=request.GET.get('category')
        if category==None:
           photos=Photo.objects.all()
        else:
           photos=Photo.objects.filter(category__name=category)
    
        categories=Category.objects.all()
        return render(request,"gallery-home.html",{"categories":categories,"photos":photos})


# class PhotoView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('pk')
#         photo=Photo.objects.get(id=id)
#         return render(request,"photo-detail.html",{"photos":photo})
    
class PhotoView(DetailView):
    model=Photo
    context_object_name="photo"
    template_name="photo-detail.html"


def addPhotoView(request):
        categories=Category.objects.all()
        if request.method == 'POST':
         
         data=request.POST
         image=request.FILES.get("image")

         if data['category'] != 'none':
             category=Category.objects.get(id=data['category'])
         elif data['category_new'] != '':
          category, created=Category.objects.get_or_create(name=data['category_new'])
         else:
          category=None

         photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
         )
         return redirect("home")
        #  print('data:',data)
        #  print('image',image)
        return render(request,"photo-add.html",{"categories":categories})