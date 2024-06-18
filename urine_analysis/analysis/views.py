from django.http import JsonResponse
from .models import ImageUpload
from .color_analysis import analyze_colors
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.shortcuts import render

def index(request):
    return render(request, 'analysis/index.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_image_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Process the image to analyze colors and get image details
        test_results = analyze_colors(uploaded_image_path)

        return JsonResponse({
            'status': 'success',
            'test_results': test_results
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
