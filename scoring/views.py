from pprint import pprint
from models import Player
from serializers import PlayerSerializer
from rest_framework import renderers, viewsets, generics, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from random import random, choice


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'players': reverse('player-list', request=request, format=format)})


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlighted(self, request, *args, **kwargs):
        player = self.get_object()
        return Response(player.highlighted)


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerBowl(APIView):

    def get_queryset(self, *args, **kwargs):
        print args, kwargs

    def get(self, request, pk):
        print 'query_params: {}'.format(request.query_params)
        player = Player.objects.get(pk=pk)

        first_roll = int(random() * 10)
        try:
            second_roll = choice(range(11 - player.first_roll))
        except:
            second_roll = choice(range(11 - first_roll))
        if request.query_params:
            if 'first_roll' in request.query_params:
                first_roll = int(request.query_params.get('first_roll'))
            if 'second_roll' in request.query_params:
                second_roll = int(request.query_params.get('second_roll'))
        if first_roll == 10:
            second_roll = 0

        pprint(vars(player))

        if player.first_roll == None:
            player.first_roll = first_roll
            if player.first_roll == 10:
                player.strike_reserve += 10
                player.strike_frame = player.current_frame
                player = self.advance_frame(player)
        elif player.second_roll == None:
            player.second_roll = second_roll
            if player.first_roll + player.second_roll == 10:
                player.spare_reserve += 10
                player.spare_frame = player.current_frame
            print 'player.second_roll: {}'.format(player.second_roll)
        else:
            player = self.advance_frame(player)
            player = self.reset_game(player)

        try:
            if player.strike_reserve:
                if player.current_frame - player.strike_frame <= 2:
                    player.strike_reserve += player.first_roll
                    player.strike_reserve += player.second_roll
                else:
                    player.score += player.strike_reserve
                    player.strike_reserve = 0
                if player.current_frame % 3 == 0 or player.current_frame == 10:
                    player.score += player.strike_reserve
            elif player.spare_reserve:
                if player.current_frame - player.spare_frame <= 1:
                    player.spare_reserve += player.first_roll + player.second_roll
                else:
                    player.score += player.spare_reserve
                    player.spare_reserve = 0
                if player.current_frame % 2 == 0 or player.current_frame == 10:
                    player.score += player.spare_reserve
            else:
                player.score += player.first_roll + player.second_roll
        except:
            pass

        pprint(vars(player))

        serializer = self._serialize(player)
        return Response(serializer.validated_data)

    def _serialize(self, player):
        player_serializer = PlayerSerializer(data=vars(player))
        if player_serializer.is_valid():
            player_serializer.update(player, player_serializer.validated_data)
        return player_serializer

    def advance_frame(self, player):
        print player.first_roll, player.second_roll
        if player.first_roll != None and player.second_roll != None:
            player.current_frame += 1
            player.first_roll, player.second_roll = (None,) * 2
        return player

    def reset_game(self, player):
        if player.current_frame >= 11:
            player.current_frame = 1
            player.first_roll = None
            player.second_roll = None
            player.strike_frame = None
            player.strike_reserve = 0
            player.spare_frame = None
            player.spare_reserve = 0
            player.all_time_score += player.score
            player.score = 0
            player.games_bowled += 1
        return player
