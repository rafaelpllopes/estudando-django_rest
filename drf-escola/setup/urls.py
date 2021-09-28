from django.contrib import admin
from django.urls import include, path
from escola.views import (
    AlunosViewSet,
    CursosViewSet,
    ListaAlunosMatriculados,
    ListaMatriculasAluno,
    MatriculaViewSet,
)
from rest_framework import routers

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="Matriculas")

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("token/", TokenObtainPairView.as_view()),
    # path("token/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas/", ListaMatriculasAluno.as_view()),
    path("cursos/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view()),
]
