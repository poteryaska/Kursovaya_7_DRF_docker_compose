from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, AllowAny
from users.models import User
from users.serializers import UserSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.pk == request.user.pk


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UsersDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UsersRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    # permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)