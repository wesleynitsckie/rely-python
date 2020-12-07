from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('SC/<id>', views.sc, name="SC"),
    path('SCC/<id>', views.scc, name="SCC"),
    path('PC/<id>', views.pc, name="PC"),
    path('PCC/<id>', views.pcc, name="PCC"),
    path('AS/<id>', views.assessment, name="AS"),
    path('pepcheck/<id>', views.pep_check, name="pep_check"),
    path('pcc_confirm/<id>/<confirm>', views.pcc_confirm, name="pcc_confirm"),
    path('DENIED/<id>', views.deny, name="deny"),
    path('ACCEPTED/<id>', views.accepted, name="accepted"),
]