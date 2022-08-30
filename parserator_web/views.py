from typing import Type
import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AddressForm


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    # def get(self, request):
    #     # TODO: Flesh out this method to parse an address string using the
    #     # parse() method and return the parsed components to the frontend.

    #     # parsed_address = self.get_address_from_request(request, 'address')
    #     parsed_address = self.get_address(request, 'address')

    #     address_components, address_type = self.parse('address')
    #     return Response({
    #         'address': parsed_address,
    #         'address_components': address_components,
    #         'address_type': address_type
    #     })

    def get_address(request):
        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/received/')
        else: 
            form = AddressForm()
        return render(request, 'index.html', {'form': form})
    
    # def get_address(self, request, key):
    #     # api_key = 'r9061RRU.QN3l5Bz7QrLcAocv8erzH8ofr16YT0B5'
    #     # url = 'https://parserator.datamade.us/api/usaddress/'
    
    #     try:
    #         address = request.GET[key]
    #     except KeyError:
    #         raise ParseError('Request is missing required key: %s' % key)

    #     # try:    
    #     #     assert <check address validity>
    #     # except (AssertionError, TypeError):
    #     #     raise ParseError(
    #     #         "Request is not a valid U.S. address."
    #     #     )
    #     return address


    def extract_address_from_components(component_list):
        #takes the components returned by usaddress' parse() method and returns
        # the address string as a list
        return list(list(zip(*component_list))[0])
        

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        address_components = usaddress.parse(address)
        tagged_address, address_type = usaddress.tag(address)
        return address_components, address_type
