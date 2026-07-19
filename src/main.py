"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    print(f"\nUser Preferences: {user_prefs} \n")
    recommendations = recommend_songs(user_prefs, songs, k=5)

    width = 60
    print()
    print("=" * width)
    print("TOP RECOMMENDATIONS".center(width))
    print("=" * width)

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


if __name__ == "__main__":
    main()
