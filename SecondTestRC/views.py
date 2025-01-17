from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from SecondTestRC.models import SecondReceiver
from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import action
from DjangoProject.send_base import SendBase


class SecondHomePageView(GenericViewSet):
    @extend_schema(
        parameters=[
            OpenApiParameter('value', OpenApiTypes.BOOL, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def get_bool_second(self, value):
        SecondReceiver.objects.create(cost=100,bool=value)
        return Response(status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[
            OpenApiParameter('cost', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def get_cost_second(self, cost):
        SecondReceiver.objects.create(cost=cost,bool=True)
        return Response(status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[
            OpenApiParameter('number_1', OpenApiTypes.INT, OpenApiParameter.QUERY),
            OpenApiParameter('number_2', OpenApiTypes.INT, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def get_sum(self,request):
        number_1,number_2 = self.request.query_params.get('number_1'),self.request.query_params.get('number_2')
        task = SendBase(task_name='test_app.tasks.sum_numbers',args=[number_1,number_2])
        result = task.get_result()
        return JsonResponse({'result':result})