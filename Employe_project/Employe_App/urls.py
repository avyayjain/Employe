from django.urls import path
from Employe_App import views

urlpatterns = [
   # path('',views.hello),
    #path('',views.add),
    path('',views.addForm,name='form'),
    path('data',views.showForm,name='data'),
    path('delete/<int:id>',views.deleteForm,name='delete'),
    path('<int:id>',views.addForm,name='edit')
]