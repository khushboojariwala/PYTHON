from .models import book
from .serializers import bookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def bookListAPI(request):
    if request.method == 'GET':
        querySet=book.objects.all()
        serializer = bookSerializer(querySet, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer=bookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','PATCH','DELETE'])
def bookDetailAPI(request,book_id):
    try:
        querySet=book.objects.get(id=book_id)
    except book.DoesNotExist:
        return Response({'message':"Book Doesn't Found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=bookSerializer(querySet)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer=bookSerializer(querySet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializer = bookSerializer(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            context = {
                'data':serializer.data,
                'message':f"{querySet.title} - Updated successfully."
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        querySet.delete()
        return Response({'message': 'Book deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)