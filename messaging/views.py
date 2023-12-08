from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required

def message_list(request):                     # 내가 보낸 쪽지의 리스트를 보여주기 위함.
    sent_messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/message_list.html', {'sent_messages': sent_messages})

def create_message(request):    # 쪽지 폼을 작성하고 제출하면 실행되는 함수이다.
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 모델에 저장
            new_message = form.save(commit=False)
            new_message.sender = request.user  # 현재 로그인한 사용자를 보낸 사람으로 설정
            new_message.save()
            return redirect('message_list')  # 쪽지가 성공적으로 전송되었음을 나타내는 페이지로 리다이렉트
    else:
        form = MessageForm()
    return render(request, 'messaging/message_form.html', {'form': form})