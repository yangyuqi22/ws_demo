from django.shortcuts import render

# Create your views here.
def index(request):
    group_id = request.GET.get('group_id')
    
    return render(request, 'index.html', {'group_id': group_id})

