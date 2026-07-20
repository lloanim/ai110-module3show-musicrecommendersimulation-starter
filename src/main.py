"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# ---------------------------------------------------------------------------
# Three distinct "normal" user profiles.
# Each targets a different corner of the song catalog so the rankings should
# look clearly different from one another.
# ---------------------------------------------------------------------------
NORMAL_PROFILES = {
    "Pop Party-goer": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "likes_acoustic": False,
    },
    "Lofi Studier": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "likes_acoustic": True,
    },
    "Metalhead": {
        "genre": "metal",
        "mood": "aggressive",
        "energy": 0.95,
        "likes_acoustic": False,
    },
}

# ---------------------------------------------------------------------------
# Adversarial / edge-case profiles.
# These are deliberately built to probe weaknesses in score_song(). The
# comment on each says what it tests and the unexpected result to watch for.
# ---------------------------------------------------------------------------
EDGE_PROFILES = {
    # Energy is not clamped: 1 - abs(5.0 - 0.82) = -4.18, then * 0.25.
    # A perfect genre+mood match can end up with a NEGATIVE total score,
    # so ranking becomes "whichever song has the highest energy" and
    # genre/mood stop mattering.
    "Out-of-range energy": {
        "genre": "pop",
        "mood": "happy",
        "energy": 5.0,
        "likes_acoustic": False,
    },
    # Empty profile. Note the hidden defaults:
    #   energy -> 0.0  (secretly demands a near-silent song, penalizes energy)
    #   likes_acoustic -> falsy (secretly rewards NON-acoustic songs)
    # "No preference" is NOT neutral here — it's a strong opinion.
    "Empty profile": {},

    # Exact-match / case sensitivity trap. "Pop" != "pop" and "  happy "
    # != "happy", so genre and mood both score 0 even though a human would
    # call this a pop-happy fan.
    "Case & whitespace": {
        "genre": "Pop",
        "mood": "  happy ",
        "energy": 0.85,
        "likes_acoustic": False,
    },
    # Contradictory tastes: wants classical (a low-energy genre in the data)
    # but demands max energy. Genre points and energy points fight each
    # other, and the "winner" may be a song from neither camp.
    "Contradiction": {
        "genre": "classical",
        "mood": "melancholic",
        "energy": 1.0,
        "likes_acoustic": True,
    },
    # Genre/mood that exist in nobody's row. No song can earn those 0.60 of
    # weight, so results are decided purely by energy + acoustic — a good
    # test that the recommender degrades gracefully instead of erroring.
    "Nonexistent tags": {
        "genre": "k-pop",
        "mood": "vibey",
        "energy": 0.5,
        "likes_acoustic": True,
    },
}


def print_recommendations(name: str, user_prefs, songs) -> None:
    width = 60
    print()
    print("=" * width)
    print(f"{name}".center(width))
    print("=" * width)
    print(f"Preferences: {user_prefs}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for rank, rec in enumerate(recommendations, start=1):
        # Each returned item is (song, score, explanation), where explanation
        # is the scoring function's reasons joined by "; ".
        song, score, explanation = rec
        reasons = [r.strip() for r in explanation.split(";") if r.strip()]

        title_line = f"{rank}. {song['title']}"
        artist = song.get("artist")
        if artist:
            title_line += f" — {artist}"

        print()
        print(title_line)
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"     • {reason}")

    print()
    print("=" * width)


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, prefs in NORMAL_PROFILES.items():
        print_recommendations(name, prefs, songs)

    for name, prefs in EDGE_PROFILES.items():
        print_recommendations(f"[EDGE] {name}", prefs, songs)


if __name__ == "__main__":
    main()
