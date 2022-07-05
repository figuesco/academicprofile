from django.shortcuts import render

# Create your views here.
Class notificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    user = User.objects.filter(is_active=True)

def post(self, request):
        data = request.data
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
   
        user_id = serializer.data
        empleador = serializer.data['empleador']
        area = serializer.data['area']
        rol =serializer.dta['rol']
        mensaje =serializer.data['mensaje']

        user_id = request.user.id