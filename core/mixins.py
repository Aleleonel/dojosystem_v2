#class AcademiaFilterMixin:

    #def get_academia(self):

        #return self.request.user.academia
    

from alunos.models import Aluno
from accounts.models import User
from aulas.models import Aula
from financeiro.models import Mensalidade


class AcademiaMixin:

    def get_academia(self):

        return self.request.user.academia

    def alunos(self):

        return Aluno.objects.filter(
            academia=self.get_academia()
        )

    def usuarios(self):

        return User.objects.filter(
            academia=self.get_academia()
        )

    def aulas(self):

        return Aula.objects.filter(
            academia=self.get_academia()
        )

    def mensalidades(self):

        return Mensalidade.objects.filter(
            academia=self.get_academia()
        )