from .models import Todo
from rest_framework.views import APIView
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class TodoList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all()
        ser_data = TodoSerializer(todos, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser_data = TodoSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return None

    def get(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ser_data = TodoSerializer(todo).data
        return Response(ser_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ser_data = TodoSerializer(todo, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
