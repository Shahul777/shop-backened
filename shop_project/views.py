# import pytesseract
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from PIL import Image
# import cv2
# @csrf_exempt
# def extract_text(request):
    
#     image_file = request.FILES['image']
    
 
#     image = Image.open(image_file)
    
 
#     text = pytesseract.image_to_string(image)
    
   
#     return JsonResponse({'text': text})
