from django.urls import path
from osmsapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('test/',views.test, name='test'),
    path('info/<str:id>', views.info, name="info"),
    path('login/',views.Login, name='login'),
    path('logout/',views.Logout, name='logout'),
    path('supplier_detail/',views.supplier_detail, name='supplier_detail'),
    path('supplier_details_update/',views.supplier_details_update, name='supplier_details_update'),
    path('hospital_details_update/',views.hospital_details_update, name='hospital_details_update'),
    path('oxygen_bed_update/',views.oxygen_bed_update, name='oxygen_bed_update'),
    path('oxygen_cylinder_update/',views.oxygen_cylinder_update, name='oxygen_cylinder_update'),
    # path('virudhunagar/', views.virudhunagar, name='virudhunagar'),
    # path('Theni/', views.Theni, name='Theni'),
    # path('Theni_hospital1/', views.Theni_hospital1, name='Theni_hospital1'),
    # path('Theni_hospital2/', views.Theni_hospital2, name='Theni_hospital2'),
    # path('Theni_hospital3/', views.Theni_hospital3, name='Theni_hospital3'),
    # path('Theni_hospital4/', views.Theni_hospital4, name='Theni_hospital4'),
    # path('Theni_hospital5/', views.Theni_hospital5, name='Theni_hospital5'),
    # path('Theni_hospital6/', views.Theni_hospital6, name='Theni_hospital6'),
    # path('Theni_hospital7/', views.Theni_hospital7, name='Theni_hospital7'),
    # path('Theni_hospital8/', views.Theni_hospital8, name='Theni_hospital8'),
    # path('Theni_hospital9/', views.Theni_hospital9, name='Theni_hospital9'),
    # path('Theni_hospital10/', views.Theni_hospital10, name='Theni_hospital10'),
    # path('Theni_hospital11/', views.Theni_hospital11, name='Theni_hospital11'),
    # path('Theni_hospital12/', views.Theni_hospital12, name='Theni_hospital12'),
    # path('Theni_hospital13/', views.Theni_hospital13, name='Theni_hospital13'),
    # path('Theni_hospital14/', views.Theni_hospital14, name='Theni_hospital14'),
    
]

