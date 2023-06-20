from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import NoteSerializer, UserSerializer

from base.models import Note
from django.contrib.auth.models import User
from api.models import NewDriver

from rest_framework.authtoken.models import Token
#from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.tokens import RefreshToken



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        driver = NewDriver.objects.get(driver_name=user.username)
        token['driver_id'] = driver.driver_id
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/authapi/token',
        '/authapi/token/refresh',
	]
    
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    #notes = Note.objects.all()
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

class RegisterUser(APIView):
    def post(self , request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
        
            return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'Something went wrong'})
        
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        #token_obj , _ = Token.objects.get_or_create(user=user)

        refresh = RefreshToken.for_user(user)
        refresh['username'] = user.username
        


        return Response({'status': 200, 'payload': serializer.data,
                         'refresh':str(refresh),
                         'access':str(refresh.access_token),
                          #'token' : str(token_obj),
                          'messge': 'your data is saved'})
    




    # def your_view(request):
    # # Get the token from the Authorization header
    # auth_header = request.headers.get('Authorization')
    # if auth_header:
    #     # Extract the token from the header (e.g., "Bearer <token>")
    #     token = auth_header.split(' ')[1]
        
    #     try:
    #         # Verify and decode the token using your secret key
    #         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    #         # Access the claims or data from the payload
    #         user_id = payload['user_id']
            
    #         # ... Your code here ...
            
    #         # Return a JSON response or perform other actions
    #         return JsonResponse({'message': 'Token verified and processed successfully.'})
    #     except jwt.ExpiredSignatureError:
    #         return JsonResponse({'error': 'Token expired.'}, status=401)
    #     except jwt.InvalidTokenError:
    #         return JsonResponse({'error': 'Invalid token.'}, status=401)
    # else:
    #     return JsonResponse({'error': 'Authorization header not found.'}, status=401)
