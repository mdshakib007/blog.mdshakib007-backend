from django.shortcuts import render
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from subscription.models import Subscribe
from subscription.serializers import SubscribeSerializer


class SubscribeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubscribeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Subscription successful!'}, status=status.HTTP_201_CREATED)
        
        try:
            email = request.data.get('email')
            subscription = Subscribe.objects.get(email=email, is_active=False)
            subscription.is_active = True
            subscription.save(update_fields=['is_active'])
            return Response({'success': 'Resubscribe success!'}, status=status.HTTP_200_OK)
        except Subscribe.DoesNotExist:
            pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnsubscribeView(View):
    def get(self, request, email, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(email=email, is_active=True)
            subscription.is_active = False
            subscription.save(update_fields=['is_active'])
            context = {'email': email, 'success': True}
        except Subscribe.DoesNotExist:
            context = {'email': email, 'success': False}
        
        return render(request, 'unsubscribe_done.html', context)
