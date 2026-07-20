# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version represents songs and user preferences as data to determine what songs from a list of 20 to recommend to the user based on their preferences. A scoring rule helps determine the recommendablility of song to user. My system prioritizes mood over the other musical attributes of genre, energy, and acousticness. This mirrors how real world AI recommenders with content-based filtering because it recommends songs with similar charactertics of mood. 

---

## How The System Works

Real-world recommenders like Spotify and YouTube start with **input data**: features describing each item, such as genre, mood, tempo, and energy for a song, or length and topic for a video. They also collect **user preferences**, but instead of asking the user to state them directly, they infer preferences from **user history**, the songs skipped, replayed, saved, or watched to the end. These systems combine two main approaches. **Content-based filtering** recommends items whose features (genre, mood, tempo) are similar to what the user already liked. **Collaborative filtering** recommends items that users with similar histories enjoyed, even if the item's features look different. For the final ranking and selection, the system does not use fixed weights. It is a learned system where the weights are knobs adjusted automatically from user feedback so the songs users actually liked score the highest, and extra rules add diversity, break ties, and filter out low-quality items.

For this design I am **hand-tuning** the recommender instead of learning the weights from data, and I use content-based filtering only. Each `Song` has genre, energy, mood, and acoustic scale. 
The `UserProfile` will store favorite_genre, favorite_mood, target_energy, and likes_acoustic. 
The `Recommender` will compute a score for each song by the difference in weights of each musical attribute. The formula will be (0.35)Mood + (0.25)Genre + (0.25)Energy + (0.15)Acoustic = 1, or equivalently (+3.5) Mood, (+2.5) Genre, (+2.5) Energy, (+1.5) Acoustic, which adds up to 10.0 and is then divided by 10 to get a 0-1 score. This will prioritize mood over genre and energy, creating bias. 
It will choose what songs to recommend by having those songs that match mood first, then genre, and the rest is ranked out of energy + acoustic closeness.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 20

============================================================
                       Pop Party-goer                       
============================================================
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85, 'likes_acoustic': False}

1. Sunrise City — Neon Echo
   Score: 0.97
   Reasons:
     • mood match (+3.5)
     • genre match (+2.5)
     • energy fit (+2.4)
     • non-acoustic match (+1.2)

2. Rooftop Lights — Indigo Parade
   Score: 0.68
   Reasons:
     • mood match (+3.5)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • non-acoustic match (+1.0)

3. Gym Hero — Max Pulse
   Score: 0.62
   Reasons:
     • mood mismatch (+0.0)
     • genre match (+2.5)
     • energy fit (+2.3)
     • non-acoustic match (+1.4)

4. Storm Runner — Voltline
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • non-acoustic match (+1.4)

5. Concrete Kings — Blockwise
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • non-acoustic match (+1.3)

============================================================

============================================================
                        Lofi Studier                        
============================================================
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4, 'likes_acoustic': True}

1. Library Rain — Paper Lanterns
   Score: 0.97
   Reasons:
     • mood match (+3.5)
     • genre match (+2.5)
     • energy fit (+2.4)
     • acoustic match (+1.3)

2. Midnight Coding — LoRoom
   Score: 0.95
   Reasons:
     • mood match (+3.5)
     • genre match (+2.5)
     • energy fit (+2.5)
     • acoustic match (+1.1)

3. Spacewalk Thoughts — Orbit Bloom
   Score: 0.71
   Reasons:
     • mood match (+3.5)
     • genre mismatch (+0.0)
     • energy fit (+2.2)
     • acoustic match (+1.4)

4. Focus Flow — LoRoom
   Score: 0.62
   Reasons:
     • mood mismatch (+0.0)
     • genre match (+2.5)
     • energy fit (+2.5)
     • acoustic match (+1.2)

5. Harvest Hymn — The Willow Trio
   Score: 0.39
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.5)
     • acoustic match (+1.4)

============================================================

============================================================
                         Metalhead                          
============================================================
Preferences: {'genre': 'metal', 'mood': 'aggressive', 'energy': 0.95, 'likes_acoustic': False}

1. Iron Verdict — Ashen Crown
   Score: 0.99
   Reasons:
     • mood match (+3.5)
     • genre match (+2.5)
     • energy fit (+2.5)
     • non-acoustic match (+1.5)

2. Pulse Reactor — Kilovolt
   Score: 0.39
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.5)
     • non-acoustic match (+1.4)

3. Gym Hero — Max Pulse
   Score: 0.39
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.5)
     • non-acoustic match (+1.4)

4. Storm Runner — Voltline
   Score: 0.38
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • non-acoustic match (+1.4)

5. Carnival Heat — Ritmo Vivo
   Score: 0.34
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • non-acoustic match (+1.1)

============================================================

============================================================
                 [EDGE] Out-of-range energy                 
============================================================
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 5.0, 'likes_acoustic': False}

1. Sunrise City — Neon Echo
   Score: -0.07
   Reasons:
     • mood match (+3.5)
     • genre match (+2.5)
     • energy fit (+-7.9)
     • non-acoustic match (+1.2)

2. Rooftop Lights — Indigo Parade
   Score: -0.36
   Reasons:
     • mood match (+3.5)
     • genre mismatch (+0.0)
     • energy fit (+-8.1)
     • non-acoustic match (+1.0)

3. Gym Hero — Max Pulse
   Score: -0.38
   Reasons:
     • mood mismatch (+0.0)
     • genre match (+2.5)
     • energy fit (+-7.7)
     • non-acoustic match (+1.4)

4. Iron Verdict — Ashen Crown
   Score: -0.61
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+-7.6)
     • non-acoustic match (+1.5)

5. Pulse Reactor — Kilovolt
   Score: -0.62
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+-7.6)
     • non-acoustic match (+1.4)

============================================================

============================================================
                    [EDGE] Empty profile                    
============================================================
Preferences: {}

1. Velvet Hours — Selah Rose
   Score: 0.21
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+1.2)
     • non-acoustic match (+0.9)

2. Spacewalk Thoughts — Orbit Bloom
   Score: 0.19
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+1.8)
     • non-acoustic match (+0.1)

3. Island Time — Sunroot Collective
   Score: 0.19
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+1.1)
     • non-acoustic match (+0.8)

4. Midnight Coding — LoRoom
   Score: 0.19
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+1.5)
     • non-acoustic match (+0.4)

5. Library Rain — Paper Lanterns
   Score: 0.18
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+1.6)
     • non-acoustic match (+0.2)

============================================================

============================================================
                  [EDGE] Case & whitespace                  
============================================================
Preferences: {'genre': 'Pop', 'mood': '  happy ', 'energy': 0.85, 'likes_acoustic': False}

1. Gym Hero — Max Pulse
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • non-acoustic match (+1.4)

2. Storm Runner — Voltline
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • non-acoustic match (+1.4)

3. Concrete Kings — Blockwise
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • non-acoustic match (+1.3)

4. Pulse Reactor — Kilovolt
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.2)
     • non-acoustic match (+1.4)

5. Sunrise City — Neon Echo
   Score: 0.37
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • non-acoustic match (+1.2)

============================================================

============================================================
                    [EDGE] Contradiction                    
============================================================
Preferences: {'genre': 'classical', 'mood': 'melancholic', 'energy': 1.0, 'likes_acoustic': True}

1. Moonlit Sonata Drift — Aria Fields
   Score: 0.82
   Reasons:
     • mood match (+3.5)
     • genre match (+2.5)
     • energy fit (+0.8)
     • acoustic match (+1.4)

2. Carnival Heat — Ritmo Vivo
   Score: 0.26
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.2)
     • acoustic match (+0.4)

3. Iron Verdict — Ashen Crown
   Score: 0.25
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • acoustic match (+0.0)

4. Pulse Reactor — Kilovolt
   Score: 0.24
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • acoustic match (+0.1)

5. Storm Runner — Voltline
   Score: 0.24
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • acoustic match (+0.2)

============================================================

============================================================
                  [EDGE] Nonexistent tags                   
============================================================
Preferences: {'genre': 'k-pop', 'mood': 'vibey', 'energy': 0.5, 'likes_acoustic': True}

1. Harvest Hymn — The Willow Trio
   Score: 0.36
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.2)
     • acoustic match (+1.4)

2. Delta Blues Lament — Cotton Field Sam
   Score: 0.36
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • acoustic match (+1.2)

3. Coffee Shop Stories — Slow Stereo
   Score: 0.35
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.2)
     • acoustic match (+1.3)

4. Moonlit Sonata Drift — Aria Fields
   Score: 0.34
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.0)
     • acoustic match (+1.4)

5. Focus Flow — LoRoom
   Score: 0.34
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.2)
     • acoustic match (+1.2)

============================================================
```

Why These Songs Were Recommended

- **Sunrise City — Neon Echo** (Pop Party-goer, score 0.97): recommended because
  it matches the listener's **happy mood** and **pop genre** (the two biggest
  weights), sits almost exactly at their **high target energy** (0.85 vs. 0.82),
  and is **non-acoustic**, which is what this profile prefers. All four
  components line up, so it earns nearly the maximum score.

- **Library Rain — Paper Lanterns** (Lofi Studier, score 0.97): picked for its
  **chill mood** and **lofi genre** match, a **low energy** level that fits the
  studier's calm 0.40 target, and a **high acousticness** that matches their
  "likes acoustic" preference. It beats other lofi tracks mainly on the acoustic
  fit.

- **Iron Verdict — Ashen Crown** (Metalhead, score 0.99): the strongest pick in
  the whole run because it matches the **aggressive mood** and **metal genre**,
  has **very high energy** right at the 0.95 target, and is **non-acoustic** as
  preferred — a perfect fit on all four axes.


Comparing The Three Profiles

I ran the recommender for three distinct listeners — a **Pop Party-goer**
(pop / happy / high energy 0.85 / non-acoustic), a **Lofi Studier**
(lofi / chill / low energy 0.40 / acoustic), and a **Metalhead**
(metal / aggressive / very high energy 0.95 / non-acoustic). The outputs above
differ in clear, expected ways:

- **Each profile gets a completely different top song.** The Pop Party-goer
  lands on *Sunrise City* (upbeat pop), the Lofi Studier on *Library Rain*
  (quiet acoustic lofi), and the Metalhead on *Iron Verdict* (loud metal). No
  song tops more than one list, which shows the scoring genuinely responds to
  preferences instead of always surfacing the same "popular" track.


- **Energy pulls the lists in opposite directions.** The Metalhead and Pop
  lists fill up with high-energy tracks (*Gym Hero*, *Storm Runner*,
  *Pulse Reactor*), while the Lofi Studier's list shifts toward calm, low-energy
  songs (*Midnight Coding*, *Spacewalk Thoughts*, *Focus Flow*). This is the
  energy-similarity component working as designed.

- **Acousticness flips the tie-breakers.** Because the Lofi Studier sets
  `likes_acoustic = True`, acoustic songs gain points (*Library Rain*,
  *Harvest Hymn* earn their acoustic bonus), whereas the two non-acoustic
  profiles reward the opposite, so electronic/produced tracks edge ahead on
  their lists.

- **Mood decides the ceiling.** Only songs that match the listener's mood reach
  the top scores (~0.97-0.99), because mood carries the heaviest weight (3.5).
  Songs that miss on mood but match genre or energy cluster in the mid-0.3s to
  0.6s, which is why the drop-off after the #1 pick is steep on every list.

Overall the Pop profile prefers upbeat, high-energy non-acoustic songs,
the Lofi profile shifts toward low-energy acoustic tracks, and the Metalhead profile favors the highest-energy, most aggressive songs. Which is what the mood first, energy/genre, and acousticness scoring rule wass built to do. 

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Since my recommender uses hand-set weights for each musical attribute, I experimented with changing the scoring formula. I reduced the genre weight by 0.10 and increased the energy weight by 0.10 because I believed that mood and energy together better represent what a user wants to hear than genre alone.
- Original formula: (0.35)Mood + (0.25)Genre + (0.25)Energy + (0.15)Acoustic = 1
- Adjusted formula: (0.35)Mood + (0.15)Genre + (0.35)Energy + (0.15)Acoustic = 1
I evaluated the recommender using two types of tests: realistic user profiles and edge-case profiles. I checked whether the recommendations matched each user's preferences, whether the same song appeared at the top of every list, and whether the recommendation reasons made sense.The weight change had little effect on profiles where mood, genre, and energy already agreed. However, when genre and mood conflicted, the increased energy weight caused mood- and energy-matching songs to rank higher while genre-only matches ranked lower. The edge-case profiles revealed the biggest weaknesses in the scoring function. An out-of-range energy value produced negative scores because the energy value was not clamped to a valid range, causing the rankings to become unreliable. I also found that an empty user profile was not treated as neutral. Instead, the default values unintentionally favored songs with very low energy and low acousticness.
More details in `model_card.md`.

---

## Limitations and Risks

MoodCheck only uses four song attributes to make recommendations: mood, genre, energy, and acousticness. However, the dataset also includes tempo, valence, and danceability, which are not used in the scoring function. This limits the system because users who care more about those attributes will not receive recommendations that match their preferences. There is also no way to filter songs by artist, so users who want to listen to a specific artist cannot do so. The recommender is also biased because mood has the highest weight (3.5 out of 10), while genre and energy each have a weight of 2.5 out of 10. This means the system assumes that mood is the most important factor when choosing music. Users who care more about genre or energy may receive less accurate recommendations. Another limitation is the small music catalog. There are only 20 songs with 17 different genres, so some genres only have one or two songs. If a user's favorite genre has only one matching song, it will almost always be recommended first. If there are no genre or mood matches, the system falls back on energy and acousticness. Finally, users who leave some preferences blank may receive weaker recommendations because the scoring function has less information to work with, as shown in the edge-case tests.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

This project gave me better understanding of how recommendation systems turn data into predictions. My recommender uses a simple weighted scoring formula to compare a user's preference with each song's attributes. While this approach works, it also showed me how much the results depend on the choices made me designing the system creating bias. When experimenting with the weights I initially expected that increasing the weight of energy and decreasing it from genre would significanly change the recommendations from the original prioritization of mood. But this changes little to nothing because mood had the largest influence on the final score. This showed me that even small design decisions can greatly affect the recommendations users receive. AI tools helped me understand more on how this system differs from real world systems. It helped me understand how the weighting on the attributes should be based on what I wanted the system to prioritize. I needed to double check AI's suggestions when implementing functions with the weights I had set. Real world systems deal with this with deep learning and neural networks that allow them recommend more based on each users actions. However, this system is not prefect because it may recommend the same stuff over again with no new songs or recommend new songs when the user does not want to hear it. This project showed me that recommendation systems are not completely ojective but are shaped by both the data they use and the design decisions behind them. I would try extending this project by implementing the other attributes to create a more accurate recommendation system. 

