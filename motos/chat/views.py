from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .forms import ChatMessageForm
from .models import Chat
# Create your views here.

@login_required
def new_chat(req, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == req.user:
        return redirect('dashboard:index')
    
    chats = Chat.objects.filter(item=item).filter(members__in=[req.user.id])
    
    if chats:
        return redirect('chat:detail', pk=chats.first().id)
        
    if req.method == 'POST':
        form = ChatMessageForm(req.POST)
        
        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(req.user)
            chat.members.add(item.created_by)
            chat.save()
            
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = req.user
            chat_message.save()
            
            return redirect('item:detail', pk=item_pk)
    
    else:
        form = ChatMessageForm()
    
    return render(req, 'chat/new.html', {
        'form': form,
    })
    
@login_required
def inbox(req):
    chats = Chat.objects.filter(members__in=[req.user.id])
    
    return render(req, 'chat/inbox.html',{
        'chats': chats
    })
    
@login_required
def detail(req, pk):
    chat = Chat.objects.filter(members__in=[req.user.id]).get(pk=pk)
    
    if req.method == 'POST':
        form = ChatMessageForm(req.POST)
        
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = req.user
            chat_message.save()
            
            chat.save()
            
            return redirect('chat:detail', pk=pk)
    else:
        form = ChatMessageForm()
    
    return render(req, 'chat/detail.html', {
        'chat':chat,
        'form':form,
    })
    