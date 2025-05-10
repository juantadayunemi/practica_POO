from ast import Not
from decimal import Decimal
from http.client import NON_AUTHORITATIVE_INFORMATION
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from core.models import Doctor
from django.shortcuts import get_object_or_404


def home(request):
    data = {
        'title': 'App Medica',
        'description': 'Gesion de citas medicas',
        'author': 'Daniel Vera',
        'year': 2025,
    }
    return render(request, 'home.html', data)

def doctor_list(request):

    q  = request.GET.get('q')
    
    if  q is None:
       doctors =  Doctor.objects.all()
    else :
        doctors = Doctor.objects.filter(name__icontains=q)

    data= {'doctors': doctors, 'Title': 'Listado de doctores'}

    return render (request, 'doctors/list_doctor.html', data)


@csrf_exempt
def doctor_create(request):

    if request.method == "POST":
        name = request.POST.get('name')
        specialty = request.POST.get('specialty')
        honorarios = request.POST.get('honorarios')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Basic validation
        if not all([name, specialty, honorarios, phone]):
            return JsonResponse({'success': False, 'errors': 'All fields are required'})
            
        doctor = Doctor.objects.create(
            name=name,
            specialty=specialty,
            honorarios=honorarios,
            phone=phone,
            address=address
        )
        return JsonResponse({'success': True})

    # GET request - return the modal HTML
    html = render_to_string('doctors/modal_create_doctor.html', request=request)
    return HttpResponse(html)  # Changed from JsonResponse to HttpResponse

    
@csrf_exempt
def doctor_update(request, id):
    print("enter on doctor_update")
    doctor = get_object_or_404(Doctor, pk=id)

   
    if request.method == "POST":
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        try:
            # Obtener datos del formulario
            name = request.POST.get('name', '').strip()
            specialty = request.POST.get('specialty', '').strip()
            honorarios = request.POST.get('honorarios', '').strip()
            phone = request.POST.get('phone', '').strip()
            address = request.POST.get('address', '').strip()
            
            # Validación
            errors = []
            if not name: errors.append("El nombre es requerido")
            if not specialty: errors.append("La especialidad es requerida")
            if not honorarios: errors.append("Los honorarios son requeridos")
            if not phone: errors.append("El teléfono es requerido")
            
            if errors:
                return JsonResponse({
                    'success': False, 
                    'errors': ", ".join(errors)
                }, status=400)
            
            # Convertir honorarios a decimal
            try:
                honorarios_decimal = Decimal(honorarios)
            except:
                return JsonResponse({
                    'success': False,
                    'errors': "Formato inválido para honorarios"
                }, status=400)
            
            # Actualizar doctor
            doctor.name = name
            doctor.specialty = specialty
            doctor.honorarios = honorarios_decimal
            doctor.phone = phone
            doctor.address = address
            doctor.save()
            
            return JsonResponse({'success': True})
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'errors': str(e)
            }, status=500)

    # GET request - mostrar formulario
    context = {'doctor': doctor , 'title':'Actualizar doctor'}
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print("AJAX request detected")
        html = render_to_string('doctors/modal_update_doctor.html', context, request=request)
        print("create html")
        return HttpResponse(html)
    else:
        print("not AJAX request detected")
        return render(request, 'doctors/modal_update_doctor.html', context)

def doctor_delete(request, id):...