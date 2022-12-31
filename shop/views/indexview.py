from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product


class IndexView(TemplateView):
    template_name = "shop/index.html"

    def get(self, request):
        products = Product.objects.order_by("name")
        for p in products:
            print(p)
        context = {
            "title": "Welcome to Django Web Shop",
            "products": [{
                "id": p.id, "name": p.name, "price": p.price} for p in products],
            }

        template = loader.get_template(self.template_name)
        # return HttpResponse("<h1>Django Webshop</h1>")
        return HttpResponse(template.render(context, request))


