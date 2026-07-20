from src.recommender import Song, UserProfile, Recommender

def make_small_recommender() -> Recommender:
    # The lofi track is listed FIRST on purpose: a recommend() that doesn't
    # actually sort (e.g. returns songs[:k]) would put it at position 0 and
    # fail the assertions below.
    songs = [
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # The pop, happy, high-energy song matches the profile and must rank first,
    # even though it is listed second in the fixture.
    assert results[0].id == 1
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"
    # The worse match must come after it — i.e. the list is actually sorted.
    assert results[1].id == 2


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""
    # The explanation must actually reflect this song, not be a fixed placeholder.
    assert song.title in explanation
    assert "mood" in explanation
