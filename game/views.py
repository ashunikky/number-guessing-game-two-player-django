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
        attempts= 1
        pl=player(firstname=firstname,email=email,guessed_number=guessed_number,attempts=attempts)
        pl.save()
        return render(request,"waiting.html")
    else:
        return render(request, "play.html")

def fetch(request):
    obj= player.objects.latest('id')
    if gamemaster.objects.filter(player=obj).exists():
        gm=gamemaster.objects.get(player=obj)
        print(obj.attempts)

        if obj.attempts<4:
            if gm.player==obj: 
                if gm.selected_number==obj.guessed_number:
                    name=obj.firstname
                    attempts=obj.attempts
                    return render(request,"result.html",{'name':name,'attempts':attempts})

                elif request.method=='POST':
                            
                    guessed_number=request.POST.get('guessed_number')
                    print(f'guessed number: {guessed_number}')
                    
                    obj.guessed_number=guessed_number
                    
                    
                    obj.attempts +=1
                    print(f'incresed attempt:{obj.attempts}')
                    
                    obj.save()
                    return HttpResponseRedirect('/fetch')
                            
                else:  
                    attempts=obj.attempts      
                    return render(request,"play2.html",{'attempts':attempts})
                
            return HttpResponse("gamemaster has not selected any number yet!!")
        return HttpResponse("you have out of the attempts!!")
    else:
        return render(request, "waiting.html")











