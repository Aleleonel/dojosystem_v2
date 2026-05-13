class AcademiaFilterMixin:

    def get_academia(self):

        return self.request.user.academia