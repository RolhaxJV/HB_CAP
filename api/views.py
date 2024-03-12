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
        """
        Returns the serializer class based on the 'table' parameter provided in the kwargs.

        Parameters:
            self: The instance of the class.
        
        Return:
            The serializer class based on the 'table' parameter. Returns None if the 'table' parameter is not recognized.
        """
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
        """
        This function returns the queryset based on the table and primary key provided as parameters.
        """
        table = self.kwargs['table']
        pk = self.kwargs['pk']
        
        if table == 'date':
            return D_Date.objects.filter(date=pk)
        elif table == 'type':
            return D_Type.objects.filter(pk=pk)
        elif table == 'departement':
            return D_Depart.objects.filter(pk=pk)
        elif table == 'dose':
            return F_Dose.objects.filter(pk=pk)
        else:
            return None

    def get(self, request, *args, **kwargs):
        """
        A description of the entire function, its parameters, and its return types.
        """
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
        """
        A function to handle GET requests with optional format parameter.
        
        Parameters:
            request: The HTTP request object
            format: The format of the response (default is None)
        
        Returns:
            A response containing data from the specified table
        """
        table = self.request.query_params.get('table', None)
        match table:
            case 'dose':
                queryset = F_Dose.objects.all()
                serializer_class = F_Dose_Serializer
            case 'date':
                queryset = D_Date.objects.all()
                serializer_class = D_Date_Serializer
            case 'departement':
                queryset = D_Depart.objects.all()
                serializer_class = D_Depart_Serializer
            case 'type':
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