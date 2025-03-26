from django.shortcuts import redirect, render
from mixtext.forms import UploadFileForm
from mixtext.utils import process_file_content

def mixText(request):
    form = UploadFileForm(request.POST, request.FILES)

    if request.method == 'POST' and form.is_valid():
        uploaded_file = request.FILES.get('file')

        if not uploaded_file.name.endswith('.txt') or uploaded_file.content_type != 'text/plain':
            return render(request, 'mixtext/mixtext_form.html', {'form': form, 'error': 'File isn\'t a text file.'})
        
        if uploaded_file.size == 0:
             return render(request, 'mixtext/mixtext_form.html', {'form': form, 'error': 'Uploaded file is empty.'})
        
        try:
            file_content = uploaded_file.read().decode('utf-8')
        except:
            return render(request, 'mixtext/mixtext_form.html', {'form': form, 'error': 'Error reading file.'})
        
        request.session['mixed_words'] = process_file_content(file_content)
        return redirect('results')

    return render(request, 'mixtext/mixtext_form.html', {'form': form})

def results(request):
    mixed_words = request.session.get('mixed_words', [])
    return render(request, 'mixtext/mixtext_results.html', {'mixed_words': mixed_words})
