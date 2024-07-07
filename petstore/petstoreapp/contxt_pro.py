from .models import Carts

def count_context(request):
    if request.user.is_authenticated:
        count = Carts.objects.filter(user_id=request.user,status="in-cart").count()
        return {'count':count}