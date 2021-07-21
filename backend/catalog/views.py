from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Catalog


class CatalogView(View):

    def get(self, request):
        # object = get_object_or_404(self.model,slug__iexact=slug)
        return render(request, "index.html", context={"number": 888888})
