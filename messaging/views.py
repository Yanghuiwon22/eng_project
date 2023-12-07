from django.shortcuts import render
from .forms import MessageForm


def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 데이터 처리 (저장 등)
            form.save()  # 예시로 폼 데이터를 바로 저장하는 방법입니다. 필요에 따라 다르게 처리 가능
            # 이후 리디렉션 또는 다른 처리
    else:
        form = MessageForm()

    return render(request, 'messaging/new_message.html', {'form': form})
