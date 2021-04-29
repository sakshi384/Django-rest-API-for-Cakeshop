from django.shortcuts import render
from .serializers import RegsiterSerializers,AddcakeSerilaizer,CartSerializer,CheckoutSerializer,ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Cake,AddCaketoCart,Checkout
from rest_framework import generics
from django.contrib.auth.models import User
# from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView
# from rest_framework.permissions import IsAuthenticated

# Create your views here.
def response_generator(data, message, status):
    return{'data': data, 'message':message,'status':status}

# this function is for sign up
class register_api(APIView):
    def post(self,request):
        data = request.data
        serializer=RegsiterSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_generator(data=serializer.data, message='success', status=201))
        return Response(response_generator(data=serializer.data, message='error', status=400))


# this function is for add cakes
class Addcake(APIView):

    def post(self,request):
        data=request.data
        serializer = AddcakeSerilaizer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(response_generator(data=serializer.data, message='success', status=201))


        return Response(response_generator(data=serializer.data, message='error', status=400))




# this function is for show all cakes
class Allcake(APIView):

    def get(self,request):

        queryset = Cake.objects.all()
        serializer= AddcakeSerilaizer(queryset,many=True,context={'request': request})
        return Response(response_generator(data=serializer.data, message='success', status=201))


# this function is for description of the cakes
class Descriptioncake(APIView):
    def get(self,request,pk):

        queryset = Cake.objects.get(cakeid=pk)
        serializer= AddcakeSerilaizer(queryset,context={'request': request})
        return Response(response_generator(data=serializer.data, message='success', status=201))

# this function is for search cakes
class Searchcake(APIView):
    def get(self,request):
        query = self.request.GET.get("q")
        print(query)

        cakes = Cake.objects.filter(name=query)
        serializer= AddcakeSerilaizer(cakes,context={'request': request},many=True)
        return Response(response_generator(data=serializer.data, message='success', status=201))


# this function is for Add Cake to cart
class Addcaketocart(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print("this is request data",data)
        # queryset = Cake.objects.get(email=data)

        serializer = CartSerializer(data=data, context={'request': request})
        print("this is serialized data",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(response_generator(data=serializer.data, message='success', status=201))
        # print(serializer.errors)
        return Response(response_generator(data=serializer.errors, message='error', status=400))




#  this function is for Cart
class Cart(APIView):
    def post(self,request):
        data = request.data
        print("this is data",data)
        cakes=AddCaketoCart.objects.filter(email=data['email'])
        print("this is cakes",cakes)

        serializer = AddcakeSerilaizer(cakes, context={'request': request}, many=True)
        Data = []
        for i in serializer.data:
            print(i['cakeid'])
            j=i['cakeid']
            # for j in i:
            #     print(j)
            query1 = Cake.objects.get(cakeid=j)
            Data.append(query1)
        print("before serialized data",Data)
        serializer1 = AddcakeSerilaizer(Data, context={'request': request}, many=True)

        return Response(response_generator(data=serializer1.data, message='success', status=201))




        # return Response(data)
        # ID=Addcaketocart.objects.get(email=data['email'])
        # print(ID)

        # serializer = AddcakeSerilaizer(data=data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(response_generator(data=serializer.data, message='success', status=201))

        # return Response(response_generator(data=serializer.data, message='error', status=400))

# this function is for remove cake from cart
class RemoveCakefromCart(APIView):
    def post(self,request):
        data=request.data
        print(data)
        cakes_remove = AddCaketoCart.objects.filter(email=data['email'],cakeid=data['cakeid']).first()
        cakes=cakes_remove.delete()
        print("cake remove",cakes_remove)

        # query1=Addcaketocart.remove(email=data['email'], cakeid=data[cakeid])
        # query=Addcaketocart.objects.filter(email=data['email'], cakeid=data[cakeid])
        print("item remove ")
        # return Response(data)
        # serializer=CartSerializer(cakes_remove,partial=True)
        return Response(response_generator(data=data, message='success', status=201))



# this function is for checkout
class CheckOut(APIView):
    def post(self,request):
        data=request.data
        serializer = CheckoutSerializer(data=data, context={'request': request})
        print("this is serialized data", serializer)
        cakes_id = AddCaketoCart.objects.filter(email=data['email']).delete()
        # cakes_id.Add
        # cakes_id.clear()

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(response_generator(data=serializer.data, message='success', status=201))


        # print(serializer.errors)
        return Response(response_generator(data=serializer.errors, message='error', status=400))


        # print("all cakes here ", data['cakes'])
        # serializer = AddcakeSerilaizer(data=data['cakes'], context={'request': request})
        # order = {}
        # if serializer.is_valid():
        #
        #     order.name = serializer.data
        #     return Response(response_generator(data=order, message='success', status=201))
        # return Response(response_generator(data=serializer.errors, message='error', status=400))





class MyOrder(APIView):
    def post(self,request):
        data=request.data
        # Email_get=data['email']

        cakes_id = AddCaketoCart.objects.filter(email=data['email'])
        print("this is cakes", cakes_id)
        # order_id=Checkout.objects.filter(email=data['email'])
        # print("this is order id", order_id)
        #
        # serializer2 = CheckoutSerializer(order_id,context={'request': request},many=True,)
        # order_list=[]
        # for i in serializer2.data:
        #     # print(i)
        #     for j in i:
        #         if("orderid"==j):
        #             order_list.append(j)
        #             break
        #
        #             # print(j)
        # print(order_list)
        serializer = AddcakeSerilaizer(cakes_id, context={'request': request}, many=True)
        # print("before serialized data",serializer.data)
        Data = []
        for i in serializer.data:
            print(i['cakeid'])
            j = i['cakeid']
            query1 = Cake.objects.get(cakeid=j)
            Data.append(query1)
        # print("before serialized data", Data)
        serializer1 = AddcakeSerilaizer(Data, context={'request': request}, many=True)
        return Response(response_generator(data=serializer1.data, message='success', status=201))

        # return Response(data)



        # print(data)
        # query = Checkout.objects.filter(email=data['email'])
        # print("this is cakes", query)
        #
        # serializer = CheckoutSerializer(query, context={'request': request}, many=True)
        # print(serializer)
        # return Response(response_generator(data=serializer.data, message='success', status=201))




# class PasswordReset(APIView):

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    # permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
