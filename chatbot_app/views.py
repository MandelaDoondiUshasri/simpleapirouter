from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dispatcher import process_query

@api_view(['POST'])
def chatbot(request):
    query = request.data.get("query", "")
    return Response(process_query(query))
