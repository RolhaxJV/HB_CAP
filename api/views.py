from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from app.models import D_Date,D_Depart,D_Type,F_Dose
from api.serializers import D_Depart_Serializer,D_Date_Serializer,D_Type_Serializer,F_Dose_Serializer



class Detail_Table(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        table = self.kwargs['table']
        serializer_class = None

        if table == 'date':
            serializer_class = D_Date_Serializer
        elif table == 'type':
            serializer_class = D_Type_Serializer
        elif table == 'departement':
            serializer_class = D_Depart_Serializer
        elif table == 'dose':
            serializer_class = F_Dose_Serializer
        else:
            serializer_class = None

        return serializer_class

    def get_queryset(self):
        table = self.kwargs['table']
        pk = self.kwargs['pk']
        
        if table == 'date':
            return D_Date.objects.filter(date=pk)
        elif table == 'type':
            return D_Type.objects.filter(pk=pk)
        elif table == 'departement':
            return D_Departement.objects.filter(pk=pk)
        elif table == 'dose':
            return F_Dose.objects.filter(pk=pk)
        else:
            return None

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        queryset = self.get_queryset()

        if queryset is None:
            return Response({'message': 'queryset nonetype'}, status=status.HTTP_404_NOT_FOUND)
        if serializer_class is None:
            return Response({'message': 'serializer_class nonetype'}, status=status.HTTP_404_NOT_FOUND)
            
        if queryset.exists():
            serializer = serializer_class(queryset.first())
            return Response(serializer.data)
        else:
            return Response({'message': 'Objet non trouvé'}, status=status.HTTP_404_NOT_FOUND)


class List_Table(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        table = self.request.query_params.get('table', None)
        match table:
            case 'Dose':
                queryset = F_Dose.objects.all()
                serializer_class = F_Dose_Serializer
            case 'Date':
                queryset = D_Date.objects.all()
                serializer_class = D_Date_Serializer
            case 'Departement':
                queryset = D_Departement.objects.all()
                serializer_class = D_Departement_Serializer
            case 'Type':
                queryset = D_Type.objects.all()
                serializer_class = D_Type_Serializer
            case _:
                return Response({'message': 'Table invalide'}, status=400)
        
        nombre_de_lignes = queryset.count()
        
        paginator = PageNumberPagination()
        paginator.page_size = 25
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = serializer_class(paginated_queryset, many=True)
        result = {
            'home' : 'http://localhost:8000/admin',
            'nombre_de_lignes': nombre_de_lignes,
            'nom_de_table': table,
            'data': serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }
        return Response(result, status=status.HTTP_200_OK)