from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from .models import Orga_Structure
from .serializer import Orga_srializer
# Create your views here.

@api_view(['GET'])
def get_orga_sturcture(request):
    instance = Orga_Structure.objects.all()
    serializer = Orga_srializer(instance,many=True)
    return Response(serializer.data)
      
@api_view(['POST'])    
def create_orga_member(request):
    try:
        serializer = Orga_srializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

   
@api_view(['GET','PUT','DELETE'])
def crud_orga(request,pk):
    try:
        orga_member = Orga_Structure.objects.get(id=pk)
        serializer = Orga_srializer(orga_member)
    except Orga_Structure.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
            return Response(serializer.data)

    if request.method == 'PUT':
        serializer = Orga_srializer(orga_member, request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        orga_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def make_logic(request):
    orgas = Orga_Structure.objects.all()
    serializer = Orga_srializer(orgas, many=True).data
    orga_hierarchy = []
    orga_hierarchy.append(serializer)  
    for x in orga_hierarchy:
        print(typeof(x))  
    return render(request,"orga_structure.html",{"orgas":"orgas"})
