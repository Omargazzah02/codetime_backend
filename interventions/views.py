from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Intervention
from .serializers import InterventionSerializer
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import IsOwner , IsManager
from charges_app.models import Charge
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from documents_app.models import Invoice




class InterventionListByResidenceAPIView(APIView):
    permission_classes = [IsAuthenticated , IsOwner]

    def get(self, request, residence_id):
        status_param = request.query_params.get('status')

        interventions = Intervention.objects.filter( residence_id=residence_id)
        if status_param:
            interventions = interventions.filter(status=status_param)

        serializer = InterventionSerializer(interventions.order_by('-created_at'), many=True)
        data = serializer.data
      

        return Response(data)



class CreateInterventionAPIView(APIView):
    permission_classes = [IsAuthenticated , IsOwner]

    def post(self, request):
        serializer = InterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InterventionDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            intervention = Intervention.objects.get(pk=pk)
            intervention.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Intervention.DoesNotExist:
            return Response({'error': 'Intervention non trouvée'}, status=404)



class AcceptInterventionView(APIView) : 
       permission_classes = [IsAuthenticated , IsManager ]
       
       def post(self , request , intervention_id ) : 
         intervention = Intervention.objects.get(id = intervention_id)
         if intervention is None:
           return Response({"error": "Cette intervention n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
         
         managers = intervention.residence.managers.all()

         exists =  managers.filter(id=request.user.id).exists()
         
         if (exists is not True  ) : 
              return Response({"error": "Vous n'avez pas un manager dans cette résidance."}, status=status.HTTP_401_UNAUTHORIZED)
         
         title = request.data.get("charge_title")
         category =request.data.get("category")
         price = float (request.data.get("charge_price"))
         pdf_file = request.FILES.get('pdf_file')
     



         intervention.status = "en_cours"
         intervention.save()

         charge =    Charge.objects.create(residence = intervention.residence , title = title , category = category , price = price)

         if pdf_file is not None :
             Invoice.objects.create(residence = intervention.residence , category = "Invoice" ,  title = "Invoice " + charge.title , pdf_file = pdf_file , charge = charge )
             



  
         return Response({"message":"Vous avez confimé cette intervention avec succées"}, status=status.HTTP_200_OK)




class RefuseInterventionView (APIView) :
     permission_classes = [IsAuthenticated , IsManager ]
       
     def post(self , request , intervention_id ) : 
         intervention = Intervention.objects.get(id = intervention_id)
         if intervention is None:
           return Response({"error": "Cette intervention n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
         
         managers = intervention.residence.managers.all()

         exists =  managers.filter(id=request.user.id).exists()
         
         if (exists is not True  ) : 
              return Response({"error": "Vous n'avez pas un manager dans cette résidance."}, status=status.HTTP_401_UNAUTHORIZED)
         
         intervention.status = "refusée"
         intervention.save()
         return Response({"message":"Vous avez refusé cette intervention"}, status=status.HTTP_200_OK)



class TerminateInterventionView (APIView) :
     permission_classes = [IsAuthenticated , IsManager ]
       
     def post(self , request , intervention_id ) : 
         intervention = Intervention.objects.get(id = intervention_id)
         if intervention is None:
           return Response({"error": "Cette intervention n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
         
         managers = intervention.residence.managers.all()

         exists =  managers.filter(id=request.user.id).exists()
         
         if (exists is not True  ) : 
              return Response({"error": "Vous n'avez pas un manager dans cette résidance."}, status=status.HTTP_401_UNAUTHORIZED)
         
         intervention.status = "terminée"
         intervention.save()
         return Response({"message":"Vous avez terminée cette intervention"}, status=status.HTTP_200_OK)






             