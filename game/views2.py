from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import player, gamemaster
from .serializers import playerSerializer, gamemasterSerializer

# Create your views here.
class playerList(APIView):
    def get(self, request):
        player1=player.objects.all()
        serializer=playerSerializer(player1, many=True)
        return Response(serializer.data)

class gamemasterList(APIView):

    def get(self, request,*args, **kwargs):

        try:
            id = self.kwargs["id"]
            if id != None:
                gamemaster1 = gamemaster.objects.get(id=id)
                serializer = gamemasterSerializer(gamemaster1)
        except:
            gamemaster1 = gamemaster.objects.all()
            serializer = gamemasterSerializer(gamemaster1, many=True)

        return Response(serializer.data)
       

        # gamemaster1=gamemaster.objects.all()
        # serializer=gamemasterSerializer(gamemaster1, many=True)
        # return Response(serializer.data)

    def post(self, request,*args, **kwargs ):
        
        serializer = gamemasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def play(request):
    if request.method=='POST':
    
        guessed_number=request.POST.get('guessed_number')
        firstname=request.POST.get('firstname')
        email=request.POST.get('email')
        pl=player(firstname=firstname,email=email,guessed_number=guessed_number)
        pl.save()
        return HttpResponse('let gamemaster selecting the number')
    else:
        return render(request, "play.html")

def result(request):
    obj = player.objects.latest('id')
    gm= gamemaster.objects.get(player=obj)
    print (gm.selected_number)
    print(obj.guessed_number)
    print(gm.player)
    print(obj)
    

    if gm.player==obj:
        no_of_guess=0
        while no_of_guess<3:
            if gm.selected_number==obj.guessed_number:
        
                return HttpResponse("you guessed the number right!!")
            else:
                if request.method=='POST':
                    guessed_number=request.POST.get('guessed_number')
                    print(guessed_number)
                    obj.guessed_number=guessed_number
                    
                    obj.save()

                return render(request,"play2.html")
        no_of_guess += 1

    
    return render(request, "result.html",{'id':obj,'name':obj.firstname,'number':obj.guessed_number})
    

