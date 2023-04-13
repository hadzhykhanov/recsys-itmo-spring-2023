from .toppop import TopPop
from .recommender import Recommender
import random


class ContextualUpdated(Recommender):
    """
    Recommend tracks closest to the previous one.
    Fall back to the random recommender if no
    recommendations found for the track.
    """

    def __init__(self, tracks_redis, catalog, start_tracks):
        self.tracks_redis = tracks_redis
        self.fallback = TopPop(tracks_redis, catalog.top_tracks[:100])
        self.catalog = catalog
        self.start_tracks = start_tracks

    def recommend_next(self, user: int, prev_track: int, prev_track_time: float) -> int:
        start_track_from_redis = self.tracks_redis.get(self.start_tracks[user])

        if not start_track_from_redis:
            return self.fallback.recommend_next(user, prev_track, prev_track_time)

        recommendations = self.catalog.from_bytes(start_track_from_redis).recommendations
        if not recommendations:
            return self.fallback.recommend_next(user, prev_track, prev_track_time)

        shuffled = list(recommendations)
        random.shuffle(shuffled)
        return shuffled[0]
