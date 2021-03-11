from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter
from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404
from .filters import (
    AwardFilter, CircuitFilter, DynastyFilter, EventFilter, LeagueFilter,
    MatchFilter, PlayerFilter, SeasonFilter, TeamFilter, StreamFilter)
from .serializers.awards import AwardSerializer
from .serializers.casters import CasterSerializer
from .serializers.leagues import (
    LeagueSerializer, SeasonSerializer, CircuitSerializer,
    RoundSerializer)
from api import permissions
from .serializers.beegame import PlayingSerializer, ReleaseSerializer
from .serializers.matches import (
    GameSerializer, MatchSerializer, ResultSerializer, SetSerializer)
from .serializers.teams import DynastySerializer, TeamSerializer
from .serializers.players import PlayerSerializer
from .serializers.events import EventSerializer
from .serializers.streams import StreamSerializer
from .serializers.users import MeSerializer, UserSerializer
from awards.models import Award
from beegame.models import Playing, Release
from events.models import Event
from leagues.models import League, Season, Circuit, Round
from matches.models import Game, Match, Result, Set
from casters.models import Caster
from players.models import Player
from streams.models import Stream
from teams.models import Dynasty, Team


class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Award.objects.all().order_by('round__round_number')
    serializer_class = AwardSerializer
    filterset_class = AwardFilter

class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = League.objects.all().order_by('name')
    filterset_class = LeagueFilter
    serializer_class = LeagueSerializer

class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Season.objects.all().order_by('name')
    filterset_class = SeasonFilter
    serializer_class = SeasonSerializer

class CircuitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Circuit.objects.all().order_by('name')
    filterset_class = CircuitFilter
    serializer_class = CircuitSerializer

class RoundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Round.objects.all().order_by('name')
    serializer_class = RoundSerializer

class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all().order_by('round__round_number', 'start_time')
    serializer_class = MatchSerializer
    filterset_class = MatchFilter

class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Result.objects.all().order_by('id')
    serializer_class = ResultSerializer

class SetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Set.objects.all().order_by('id')
    serializer_class = SetSerializer

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('id')
    
    permission_classes = [
        permissions.CanReadTeam|permissions.CanUpdateTeam
    ]
    serializer_class = TeamSerializer
    filterset_class = TeamFilter

    def perform_create(self, serializer):
        player, created = Player.objects.get_or_create(user=self.request.user)
        team = serializer.save(captain=player)
        team.members.add(player)

class DynastyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dynasty.objects.all().order_by('name').distinct()
    serializer_class = DynastySerializer
    filterset_class = DynastyFilter

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('name')
    permission_classes = [permissions.CanReadPlayer|permissions.CanEditPlayer]
    serializer_class = PlayerSerializer
    filterset_class = PlayerFilter

class CasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Caster.objects.all().order_by('player__name')
    serializer_class = CasterSerializer

class StreamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stream.objects.all().order_by('-start_time')
    serializer_class = StreamSerializer
    filterset_class = StreamFilter

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter

class PlayingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Playing.objects.all().order_by('-updated')
    serializer_class = PlayingSerializer

class ReleaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Release.objects.all().order_by('-released_on')
    serializer_class = ReleaseSerializer

class MeViewSet(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        
        serializer = MeSerializer(request.user, context={'request': request})
        return Response(serializer.data)

