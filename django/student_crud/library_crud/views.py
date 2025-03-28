from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Library
from .forms import LibraryForm
from django.contrib import messages # type: ignore

# Create your views here.
def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library_crud/library_list.html', {'libraries': libraries})

def create_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'library added successfully!')
            return redirect('library_list')
    else:
        form = LibraryForm()
    return render(request, 'library_crud/create_library.html', {'form': form})

def view_library(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'library_crud/view_library.html', {'library': library})

def edit_library(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=library)
        if form.is_valid():
            form.save()
            messages.success(request, 'Library updated successfully!')
            return redirect('library_list')
        else:
            messages.error(request, 'Error updating library. Please check the form.')
    else:
        form = LibraryForm(instance=library)
    
    return render(request, 'library_crud/create_library.html', {'form': form, 'update': True, 'library': library})

def delete_library(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if  request.method == 'POST':
        library.delete()
        messages.success(request, 'Library deleted successfully!')
        return redirect('library_list')
    return render(request, 'library_crud/delete_library.html', {'library': library})






