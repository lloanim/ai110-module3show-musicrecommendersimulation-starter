import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float
    # New audio features (defaulted so existing callers/tests stay valid)
    instrumentalness: float = 0.0
    speechiness: float = 0.0
    mode: int = 1

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k songs ranked for the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable explanation for why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """

    # Columns that hold whole numbers, and those that hold decimals.
    int_fields = {"id", "tempo_bpm", "mode"}
    float_fields = {
        "energy", "valence", "danceability", "acousticness",
        "instrumentalness", "speechiness",
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = dict(row)
            for field in int_fields:
                song[field] = int(song[field])
            for field in float_fields:
                song[field] = float(song[field])
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # Algorithm Recipe (Phase 2), weights out of 10 -> normalized to a 0-1 scale:
    #   Mood    (+3.5): 1.0 if match else 0.0
    #   Genre   (+2.5): 1.0 if match else 0.0
    #   Energy  (+2.5): 1 - abs(target_energy - song_energy)
    #   Acoustic(+1.5): acousticness if user likes acoustic, else 1 - acousticness
    # Component weights (points out of 10). Each reason shows the points earned
    # so the user understands why a song was recommended.
    MOOD_W, GENRE_W, ENERGY_W, ACOUSTIC_W = 3.5, 2.5, 2.5, 1.5
    reasons: List[str] = []

    # Mood (0.35)
    mood_match = user_prefs.get("mood") == song.get("mood")
    mood_score = 1.0 if mood_match else 0.0
    reasons.append(f"mood {'match' if mood_match else 'mismatch'} (+{mood_score * MOOD_W:.1f})")

    # Genre (0.25)
    genre_match = user_prefs.get("genre") == song.get("genre")
    genre_score = 1.0 if genre_match else 0.0
    reasons.append(f"genre {'match' if genre_match else 'mismatch'} (+{genre_score * GENRE_W:.1f})")

    # Energy (0.25)
    target_energy = user_prefs.get("energy", 0.0)
    energy_score = 1 - abs(target_energy - song["energy"])
    reasons.append(f"energy fit (+{energy_score * ENERGY_W:.1f})")

    # Acoustic (0.15)
    if user_prefs.get("likes_acoustic"):
        acoustic_score = song["acousticness"]
        reasons.append(f"acoustic match (+{acoustic_score * ACOUSTIC_W:.1f})")
    else:
        acoustic_score = 1 - song["acousticness"]
        reasons.append(f"non-acoustic match (+{acoustic_score * ACOUSTIC_W:.1f})")

    score = (
        0.35 * mood_score
        + 0.25 * genre_score
        + 0.25 * energy_score
        + 0.15 * acoustic_score
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = (
        (song, *score_song(user_prefs, song))
        for song in songs
    )
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in ranked[:k]
    ]
