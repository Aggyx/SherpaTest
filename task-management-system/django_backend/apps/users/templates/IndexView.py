from django.shortcuts import render
from django.views import View


class IndexView(View):
    """
    View to render the main index page
    """
    def get(self, request):
        """
        GET /
        Render the main index page
        """
        return render(request, 'index.html')
