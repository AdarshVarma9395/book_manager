from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def books(request):
    all_books = Book.objects.all()
    serializer = BookSerializer(all_books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book(request, pk):
    single_book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(single_book)
    return Response(serializer.data)


@api_view(['PUT'])
def update_book(request, pk):
    single_book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(instance=single_book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request, pk):
    single_book = get_object_or_404(Book, id=pk)
    single_book.delete()
    return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)













# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import BookSerializer
# from .models import Book
# from rest_framework import status




# @api_view(['POST'])
# def create_book(request):
#     serializer = BookSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def books(request):
#     all_books = Book.objects.all()
#     serializer = BookSerializer(all_books, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def book(request, pk):
#     single_books = Book.objects.get(id=pk)
#     serializer = BookSerializer(single_books, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def update_book(request, pk):
#     single_book = Book.objects.get(id=pk)
#     serializer = BookSerializer(instance = single_book, data = request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def delete_book(request, pk):
#     single_book = Book.objects.get(id=pk)
#     single_book.delete()
