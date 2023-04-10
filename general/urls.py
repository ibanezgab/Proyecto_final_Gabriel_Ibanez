from django.urls import path
from general.views import inicio, register, contacto,bandas, sponsors, about_me,RegistradoList,RegistradoDetalle,RegistradoBorrar,RegistradoUpdate
from general import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', inicio, name ="index"),
    path('register/', register, name ="register"),
    path('contacto/', contacto, name ="contacto"),
    path('bandas/', bandas, name ="bandas"),
    path('sponsors/', sponsors, name ="sponsors"),
    path('about_me/', about_me, name ="about_me"),
 
]

#url´s de vistas basadas en clases
urlpatterns += [

path('lista_registrados/', RegistradoList.as_view(), name ="lista_registrados"),
path('detalle_registrados/<pk>/', RegistradoDetalle.as_view(), name ="detalle_registrados"),
path('borrar_registrados/<pk>/', RegistradoBorrar.as_view(), name ="borrar_registrados"),
path('editar_registrados/<pk>/', RegistradoUpdate.as_view(), name ="editar_registrados"),

#login y cierre de session
path ('login/', views.login_request, name ='login'),
path ('logout/', LogoutView.as_view(template_name='general/logout.html'), name ='logout')

]