from .models import Branches

def branch_link(request):
    blist = Branches.objects.all()
    return dict(blist=blist)