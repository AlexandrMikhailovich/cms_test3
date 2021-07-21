from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View


class PageApiView(View):

    def get(self, request):
        # object = get_object_or_404(self.model,slug__iexact=slug)
        return render(request, "base.html", context={"number": 888888})
