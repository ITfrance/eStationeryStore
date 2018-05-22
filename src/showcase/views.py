from django.views import generic
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery,SearchRank,SearchVector

class ResultView(generic.ListView):
    #name='result'
    template_name = 'showcase/results.html'
    def get_queryset(self):
        qs=Item.objects.order_by('stock')         
        keywords = self.request.GET.get('q')
        if keywords:
            query=SearchQuery(keywords)
            vector=SearchVector('product','description')
            qs=qs.annotate(search=vector).filter(search=query)
           
        #return qs
        return sorted(qs,key=lambda t: t.stock_ok())
        
class IndexView(generic.ListView):
    template_name = 'showcase/results.html'    
    
    def get_queryset(self):    
            
        return Item.objects.none()