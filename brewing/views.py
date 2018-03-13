from django.shortcuts import render

# Create your views here.
from .models import Batch, Container, Recipe

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_batches=Batch.objects.all().count()
    num_containers=Container.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_batches':num_batches,'num_containers':num_containers},
        #context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )


from django.views import generic

class ContainerListView(generic.ListView):
    model = Container
    queryset = Container.objects.filter(name__icontains='F') # Get all Fermentation containers containing



class ContainerDetailView(generic.DetailView):
    model = Container



class BatchListView(generic.ListView):
    model = Batch



class BatchDetailView(generic.DetailView):
    model = Batch



class RecipeListView(generic.ListView):
    model = Recipe



class RecipeDetailView(generic.DetailView):
    model = Recipe