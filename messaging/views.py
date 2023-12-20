from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User
from itertools import chain


# new_messaing -> 폼에서 작성 후 전송누르면 실행 (DB에 저장)
def create_message(request, using_app):  # 쪽지 폼을 작성하고 제출하면 실행되는 함수이다.
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


def message_list(request):
    all_users = User.objects.exclude(pk=request.user.pk)
    # users = User.objects.all()
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    all_messages = list(chain(received_messages, sent_messages))

    current_user = request.user.id

    # sender = User.objects.get(pk=sender_id)
    # receiver = User.objects.get(pk=receiver_id)
    # last_message = Message.get_last_message(sender, receiver)

    return render(request, 'messaging/message_list.html',
                  {'all_users': all_users,
                   'sent_messages': sent_messages, 'received_messages': received_messages,
                   'all_messages': all_messages, })
