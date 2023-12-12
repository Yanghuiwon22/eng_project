from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from itertools import chain


# new_messaing -> 폼에서 작성 후 전송누르면 실행 (DB에 저장)
def create_message(request):  # 쪽지 폼을 작성하고 제출하면 실행되는 함수이다.
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
    users = User.objects.exclude(pk=request.user.pk)
    # users = User.objects.all()
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    all_messages = list(chain(received_messages, sent_messages))

    if received_messages or sent_messages:
        has_messages = True
    else:
        has_messages = False
    return render(request, 'messaging/message_list.html',
                  {'users':users, 'has_messages':has_messages,
                   'sent_messages': sent_messages, 'received_messages':received_messages,
                   'all_messages':all_messages})

@login_required
def inbox(request):
    received_messages = get_user_messages(request.user)
    if received_messages.exists():
        has_messages = True
    else:
        has_messages = False
    return render(request, 'inbox.html', {'received_messages': received_messages, 'has_messages': has_messages})

def get_users_with_messages():
    users_with_messages = {}
    users = User.objects.all()

    for user in users:
        received_messages = Message.objects.filter(receiver=user)
        users_with_messages[user] = received_messages

    return users_with_messages


def get_user_messages(user):
    user_messages = Message.objects.filter(Q(sender=user) | Q(receiver=user))
    return user_messages

