
from django.shortcuts import get_object_or_404

from pricing_plan.models import PricingPlan
from pricing_plan.serializers import PricingPlanSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class PricingPlanViewSet(viewsets.ModelViewSet):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer