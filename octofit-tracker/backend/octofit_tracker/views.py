# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserView(APIView):
    def get(self, request):
        return Response({"message": "User endpoint", "url": "https://potential-succotash-5jxwpj97rqhp5w.github.dev-8000.app.github.dev"})

class TeamView(APIView):
    def get(self, request):
        return Response({"message": "Team endpoint", "url": "https://potential-succotash-5jxwpj97rqhp5w.github.dev-8000.app.github.dev"})

class ActivityView(APIView):
    def get(self, request):
        return Response({"message": "Activity endpoint", "url": "https://potential-succotash-5jxwpj97rqhp5w.github.dev-8000.app.github.dev"})

class LeaderboardView(APIView):
    def get(self, request):
        return Response({"message": "Leaderboard endpoint", "url": "https://potential-succotash-5jxwpj97rqhp5w.github.dev-8000.app.github.dev"})

class WorkoutView(APIView):
    def get(self, request):
        return Response({"message": "Workout endpoint", "url": "https://potential-succotash-5jxwpj97rqhp5w.github.dev-8000.app.github.dev"})
