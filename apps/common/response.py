from typing import Dict, List
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.template import loader


class TemplateResponse(HttpResponse):
    ''' This class represents django template response. '''

    def __init__(self, request: HttpRequest, template: str, context: dict):
        content = loader.render_to_string(template, context, request)
        super().__init__(content=content)


class TemplateFormResponse(TemplateResponse):
    ''' This class represents django template response with form. '''

    def __init__(self, request: HttpRequest, template: str, form: Form):
        super().__init__(request, template, {'form': form})
