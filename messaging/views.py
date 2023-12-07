from django.shortcuts import render
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required


def new_message(request):              # 새로운 쪽지를 보내는 폼
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 데이터 처리 (저장 등)
            form.save()  # 예시로 폼 데이터를 바로 저장하는 방법입니다. 필요에 따라 다르게 처리 가능
            # 이후 리디렉션 또는 다른 처리
    else:
        form = MessageForm()

    return render(request, 'messaging/templates/messaging/message_form.html', {'form': form})

def message_list(request):                     # 내가 보낸 쪽지의 리스트를 보여주기 위함.
    sent_messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/message_list.html', {'sent_messages': sent_messages})
