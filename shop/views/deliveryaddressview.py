from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from shop.models import Category
from shop.visitor import Visitor
from shop.models import City

from django import forms


class DeliveryAddressForm(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    address = forms.CharField(label="Address", max_length=50)

    cities = City.objects.order_by("name")
    # todo: is it possible not to hardcode the Euro Symbol
    choices = [(c.id, f"{c.name} (€{c.delivery_costs:.2f} delivery cost)") for c in cities]
    city = forms.IntegerField(label="City", widget=forms.Select(choices=choices))


class DeliveryAddressView(TemplateView):
    template_name = "shop/deliveryaddress.html"

    def get(self, request):
        visitor = Visitor(request)
        categories = Category.objects.order_by("name")

        form = DeliveryAddressForm()

        context = {
            "visitor": visitor,
            "title": "Delivery address",
            "categories": [{"id": c.id, "name": c.name} for c in categories],
            "form": form,
        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))

    def post(self, request):
        form = DeliveryAddressForm(request.POST)
        # print(form["name"].value())
        # print(form["address"].value())
        # print(form["city"].value())

        visitor = Visitor(request)
        visitor.save_delivery_address(
            form["name"].value(),
            form["address"].value(),
            form["city"].value()
        )

        if "previous" in request.POST:
            return HttpResponseRedirect(reverse("shoppingcart"))
        else:
            return HttpResponseRedirect(reverse("orderconfirm"))
