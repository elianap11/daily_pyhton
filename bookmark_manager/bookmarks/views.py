from django.shortcuts import render, redirect
from .models import Bookmark
from .form import BookmarkForm

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmarks/bookmark_list.html', {'bookmarks': bookmarks})

def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/add_bookmark.html', {'form': form})

def delete_bookmark(request, id):
    bookmark = Bookmark.objects.get(id=id)
    bookmark.delete()
    return redirect('bookmark_list')