from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from TestRC.task import add_name, add_age
from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import action

class HomePageView(GenericViewSet):
    @extend_schema(
        parameters=[
            OpenApiParameter('name', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def get_name(self, request):
        name = self.request.query_params.get('name')
        add_name.delay(name)
        return Response(status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[
            OpenApiParameter('age', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def get_age(self, request):
        age = self.request.query_params.get('age')
        add_age.delay(age)
        return Response(status=status.HTTP_200_OK)
