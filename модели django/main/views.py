from django.shortcuts import (
    render, redirect
)
from .models import (
    Message,
)  


def index(request):  
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        text_content = request.POST.get('text')
    
        Message.objects.create(
            author=request.user,
            text=text_content
        )
        return redirect('index')
    
    all_messages = Message.objects.all().order_by('-created_at')
    
    return render(request, 'index.html', {'messages': all_messages})



    
def admin_panel(request):
    messages = Message.objects.all()

    return render(
        request,
        'admin.html',
        {'messages': messages}
    )
    

def delete_message(request, msg_id):

    if not request.user.is_staff:
        return redirect('/admin-panel/')

    msg = Message.objects.get(id=msg_id)

    msg.delete()

    return redirect('/admin-panel/')