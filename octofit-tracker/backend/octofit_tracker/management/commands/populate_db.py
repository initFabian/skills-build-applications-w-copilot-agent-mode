from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']


        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Populate users collection
        db.users.insert_many([
            {"email": "user1@example.com", "name": "User One", "age": 25},
            {"email": "user2@example.com", "name": "User Two", "age": 30}
        ])

        # Populate teams collection
        db.teams.insert_many([
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
            {"name": "Team Beta", "members": []}
        ])

        # Populate activity collection
        db.activity.insert_many([
            {"user": "user1@example.com", "type": "Running", "duration": 30},
            {"user": "user2@example.com", "type": "Cycling", "duration": 45}
        ])

        # Populate leaderboard collection
        db.leaderboard.insert_many([
            {"team": "Team Alpha", "points": 100},
            {"team": "Team Beta", "points": 50}
        ])

        # Populate workouts collection
        db.workouts.insert_many([
            {"name": "Workout A", "description": "Full body workout"},
            {"name": "Workout B", "description": "Cardio workout"}
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
