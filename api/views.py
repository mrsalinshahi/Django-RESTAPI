from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


#  Student  with APIView
#  ---------------------------------------------------------------------------------------------------------------------
class StudentAPI(APIView):
    def get(self, request):
        student_data = Student.objects.all()
        student_serializers= StudentSerializers(student_data, many=True)
        return Response(student_serializers.data,200)

    def post(self, request):
        data = request.data
        serializer = StudentSerializers(data = data )

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Data is saved'})

        return Response({'status': 403, 'errors': serializer.errors,  'message': 'Something went wrong'})

    def put(self, request):
           try:
                student_data = Student.objects.get(id=request.data['id'])
                serializer = StudentSerializers(student_data, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': 200, 'payload': serializer.data, 'message': 'Data is saved'})

                return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

           except Exception as e:
                return Response({'status': 403, 'message': 'You have entered invalid ID'})

    def patch(self, request):
            try:
                student_data = Student.objects.get(id=request.data['id'])
                serializer = StudentSerializers(student_data, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': 200, 'payload': serializer.data, 'message': 'Data is saved'})

                return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

            except Exception as e:
                return Response({'status': 403, 'message': 'You have entered invalid ID'})

    def delete(self, request):
            try:
                id = request.GET.get('id')
                student_data = Student.objects.get(id=id)
                student_data.delete()
                return Response({'status': 200, 'message': 'Data has been deleted'})

            except Exception as e:
                return Response({'status': 403, 'message': 'You have entered invalid ID'})

#  -----------------------------------------------------------------------------------------


# API Decorator for book
# --------------------------------------
@api_view(['GET'])
def get_book(request):
    book_data = Book.objects.all()
    book_serializers = BookSerializers(book_data, many=True)
    return Response(book_serializers.data, 200)

# --------------------------------------


# # API Decorator for student
# # --------------------------------------
# @api_view(['GET'])
# def get_student(request):
#     student_data = Student.objects.all()
#     student_serializers= StudentSerializers(student_data, many=True)
#
#     return Response(student_serializers.data,200)
#
# @api_view(['POST'])
# def create_student(request):
#     data = request.data
#     serializer = StudentSerializers(data = data )
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'Data is saved'})
#
#     return Response({'status': 403, 'errors': serializer.errors,  'message': 'Something went wrong'})
#
# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_data = Student.objects.get(id=id)
#         serializer = StudentSerializers(student_data, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 200, 'payload': serializer.data, 'message': 'Data is saved'})
#
#         return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
#
#     except Exception as e:
#         return Response({'status': 403, 'message': 'You have entered invalid ID'})
#
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_data = Student.objects.get(id=id)
#         student_data.delete()
#         return Response({'status': 200, 'message': 'Data has been deleted'})
#
#     except Exception as e:
#         return Response({'status': 403, 'message': 'You have entered invalid ID'})
#
# # ------------------------------------------

