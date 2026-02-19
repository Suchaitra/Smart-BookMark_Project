from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'myapp/list.html', {'bookmarks': bookmarks})



def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        Bookmark.objects.create(title=title, url=url)
        return redirect('bookmark_list')
    return render(request, 'myapp/add.html')



def update_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    if request.method == 'POST':
        bookmark.title = request.POST['title']
        bookmark.url = request.POST['url']
        bookmark.save()
        return redirect('bookmark_list')
    return render(request, 'myapp/update.html', {'bookmark': bookmark})



def delete_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    bookmark.delete()
    return redirect('bookmark_list')
