#Created By Zero Byte
#OS: ParrotSec
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfeed.html')
  return HttpResponse(template.render())
