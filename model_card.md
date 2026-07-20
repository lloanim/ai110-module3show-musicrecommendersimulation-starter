# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

MoodCheck 1.0

---

## 2. Intended Use  

MoodCheck is designed to recommend songs based on a listener's stated preferences, with the most weight placed on the **mood** they're in. Given a user's favorite mood, favorite genre, target energy level, and whether they enjoy acoustic music, it ranks a catalog of songs and returns the top matches along with a short reason for each pick. It recommends a short, ranked list of songs that best fit the user's mood, genre, energy, and acoustic preferences. Mood counts the most, so two songs that share the user's mood will usually rise above ones that only match genre or energy. It assumes that the user can describe their taste as a single favorite mood and genre, a rough energy level, and a yes/no preference for acoustic music. It assumes these few signals are a good stand-in for what someone actually wants to hear right now. This is a classroom exploration project, not a production app for real listeners.

---

## 3. How the Model Works  

MoodCheck gives each song a score between 0 and 1, where a score closer to 1 means the song fits the user's preferences better. (Internally the four attributes are worth points out of 10, which is then divided by 10 to land on the 0-1 scale.) The songs are lined up from highest recommendation to lowest. In every song four musical attributes are compared mood, genre, energy, and acoustic feel.

But this recommender adds those four attributes together into one number. Mood and genre are simple yes/no matches, while energy and acoustic feel are measured on a sliding scale, so a song can partly win points even when it isn't a perfect fit. The songs with the highest totals float to the top, and along with each pick the model prints a plain-English reason (for example, "mood match, genre mismatch, good energy fit, acoustic match") so you can see why it chose that song.

The biggest change from the starter version is that I gave it a real scoring recipe, decided how much each of the four factors should count (mood the most, then genre and energy, then acoustic feel), and made it explain its reasoning for every recommendation.

---

## 4. Data   

MoodCheck uses a small hand-built catalog of 20 songs, stored in a spreadsheet (`data/songs.csv`). Each row is one song with details like its title, artist, genre, mood, energy level, tempo, and how acoustic it sounds.
The catalog covers a wide spread of styles of about 17 genres including pop, lofi, rock, jazz, hip-hop, classical, reggae, country, metal, edm, blues, folk, r&b, and latin. A similar range of moods in the songs are happy, chill, intense, focused, melancholic, romantic, and energetic. I added 10 extra songs to this dataset for more diverse songs. There are parts of musical taste missing because it only captures a certain range from the given dataset. Since these songs are mostly diverse there is not much comparison between similar types or closely similar.

---

## 5. Strengths  

MoodCheck works best for users who have a clear, specific taste. If someone says they want chill lofi with low energy, the songs that come back fit that description, and the mood-first weighting means the results feel right rather than random. I think the patterns that my scoring captures correctly are mood driven listeners and energy matching. The acousticness also helps determine if the user likes it or not and scores based on their decision of yes or no. The cases where the recommendation matched my intuition was the lofi studier one, where the five songs match the profile most at top and the ones at the bottom rank based on genre and energy, with acoustic last.  

---

## 6. Limitations and Bias 

MoodCheck only scores four attributes: mood, genre, energy, and acousticness. The limitation is that the songs store data on tempo_bpm, valence, and dancablilty but it is not considered into the score_song function. So a person wanting a song more based on the missing attributes creates limiation of the system. There is also no way to ask for a certain artist, so someone who just want to listen to songs from one artist can't.
There is bias with mood carring the most of the weight (3.5 of 10) while genre and energy share (2.5 of 10). If mood is not a match the next position is taken based on match from genre and energy with acoustiness if chosen as last resort of ranking. This is a bias I chose on purpose, but it means the system quietly assumes everyone picks music by mood first. A user who thinks in terms of genre or energy is served worse than a mood-first listener.
Underrepresented genres can happen because matching is exact and the catalog only has 20 songs with 17 different genres and each with one or two songs. So if a user's favorite genre only has one match, it is ranked first easily with no comparison to others. Also for when their is no match it sorts from energy/acoustic sorting. If mood appears on only a couple songs also limits this system. Scoring also favors users who input their full information on their prefences and hinders those who dont put full information like shown in edge case user profiles where input is blank and missing an input. Changing what is recommended and may recommend something that the user may not want. 

---

## 7. Evaluation  

Since my recommender is hand set weights on the musical attributes. I experimented with changing the weight of genre and energy by taking 10 away from genre and giving it to energy. I think that mood and energy go well with each other that would help recommend songs closer to what the user may want to hear. 

So the weights where (0.35)Mood + (0.15)Genre + (0.35)Energy + (0.15)Acoustic = 1
This is the output:
```
Loaded songs: 20

============================================================
                       Pop Party-goer                       
============================================================
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85, 'likes_acoustic': False}

1. Sunrise City — Neon Echo
   Score: 0.96
   Reasons:
     • mood match (+3.5)
     • genre match (+1.5)
     • energy fit (+3.4)
     • non-acoustic match (+1.2)

2. Rooftop Lights — Indigo Parade
   Score: 0.77
   Reasons:
     • mood match (+3.5)
     • genre mismatch (+0.0)
     • energy fit (+3.2)
     • non-acoustic match (+1.0)

3. Gym Hero — Max Pulse
   Score: 0.61
   Reasons:
     • mood mismatch (+0.0)
     • genre match (+1.5)
     • energy fit (+3.2)
     • non-acoustic match (+1.4)

4. Concrete Kings — Blockwise
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • non-acoustic match (+1.3)

5. Storm Runner — Voltline
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • non-acoustic match (+1.4)

============================================================

============================================================
                        Lofi Studier                        
============================================================
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4, 'likes_acoustic': True}

1. Library Rain — Paper Lanterns
   Score: 0.96
   Reasons:
     • mood match (+3.5)
     • genre match (+1.5)
     • energy fit (+3.3)
     • acoustic match (+1.3)

2. Midnight Coding — LoRoom
   Score: 0.95
   Reasons:
     • mood match (+3.5)
     • genre match (+1.5)
     • energy fit (+3.4)
     • acoustic match (+1.1)

3. Spacewalk Thoughts — Orbit Bloom
   Score: 0.80
   Reasons:
     • mood match (+3.5)
     • genre mismatch (+0.0)
     • energy fit (+3.1)
     • acoustic match (+1.4)

4. Focus Flow — LoRoom
   Score: 0.62
   Reasons:
     • mood mismatch (+0.0)
     • genre match (+1.5)
     • energy fit (+3.5)
     • acoustic match (+1.2)

5. Harvest Hymn — The Willow Trio
   Score: 0.48
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.5)
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
     • genre match (+1.5)
     • energy fit (+3.4)
     • non-acoustic match (+1.5)

2. Pulse Reactor — Kilovolt
   Score: 0.49
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.5)
     • non-acoustic match (+1.4)

3. Gym Hero — Max Pulse
   Score: 0.49
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.4)
     • non-acoustic match (+1.4)

4. Storm Runner — Voltline
   Score: 0.47
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.4)
     • non-acoustic match (+1.4)

5. Carnival Heat — Ritmo Vivo
   Score: 0.44
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • non-acoustic match (+1.1)

============================================================

============================================================
                 [EDGE] Out-of-range energy                 
============================================================
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 5.0, 'likes_acoustic': False}

1. Sunrise City — Neon Echo
   Score: -0.49
   Reasons:
     • mood match (+3.5)
     • genre match (+1.5)
     • energy fit (+-11.1)
     • non-acoustic match (+1.2)

2. Rooftop Lights — Indigo Parade
   Score: -0.69
   Reasons:
     • mood match (+3.5)
     • genre mismatch (+0.0)
     • energy fit (+-11.3)
     • non-acoustic match (+1.0)

3. Gym Hero — Max Pulse
   Score: -0.78
   Reasons:
     • mood mismatch (+0.0)
     • genre match (+1.5)
     • energy fit (+-10.7)
     • non-acoustic match (+1.4)

4. Iron Verdict — Ashen Crown
   Score: -0.92
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+-10.6)
     • non-acoustic match (+1.5)

5. Pulse Reactor — Kilovolt
   Score: -0.92
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+-10.7)
     • non-acoustic match (+1.4)

============================================================

============================================================
                    [EDGE] Empty profile                    
============================================================
Preferences: {}

1. Spacewalk Thoughts — Orbit Bloom
   Score: 0.26
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.5)
     • non-acoustic match (+0.1)

2. Velvet Hours — Selah Rose
   Score: 0.26
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+1.7)
     • non-acoustic match (+0.9)

3. Moonlit Sonata Drift — Aria Fields
   Score: 0.25
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.4)
     • non-acoustic match (+0.1)

4. Library Rain — Paper Lanterns
   Score: 0.25
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.3)
     • non-acoustic match (+0.2)

5. Midnight Coding — LoRoom
   Score: 0.25
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+2.0)
     • non-acoustic match (+0.4)

============================================================

============================================================
                  [EDGE] Case & whitespace                  
============================================================
Preferences: {'genre': 'Pop', 'mood': '  happy ', 'energy': 0.85, 'likes_acoustic': False}

1. Concrete Kings — Blockwise
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • non-acoustic match (+1.3)

2. Gym Hero — Max Pulse
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.2)
     • non-acoustic match (+1.4)

3. Storm Runner — Voltline
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • non-acoustic match (+1.4)

4. Sunrise City — Neon Echo
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.4)
     • non-acoustic match (+1.2)

5. Pulse Reactor — Kilovolt
   Score: 0.46
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.1)
     • non-acoustic match (+1.4)

============================================================

============================================================
                    [EDGE] Contradiction                    
============================================================
Preferences: {'genre': 'classical', 'mood': 'melancholic', 'energy': 1.0, 'likes_acoustic': True}

1. Moonlit Sonata Drift — Aria Fields
   Score: 0.75
   Reasons:
     • mood match (+3.5)
     • genre match (+1.5)
     • energy fit (+1.1)
     • acoustic match (+1.4)

2. Carnival Heat — Ritmo Vivo
   Score: 0.35
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.1)
     • acoustic match (+0.4)

3. Iron Verdict — Ashen Crown
   Score: 0.34
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.4)
     • acoustic match (+0.0)

4. Pulse Reactor — Kilovolt
   Score: 0.34
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • acoustic match (+0.1)

5. Storm Runner — Voltline
   Score: 0.33
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.2)
     • acoustic match (+0.2)

============================================================

============================================================
                  [EDGE] Nonexistent tags                   
============================================================
Preferences: {'genre': 'k-pop', 'mood': 'vibey', 'energy': 0.5, 'likes_acoustic': True}

1. Delta Blues Lament — Cotton Field Sam
   Score: 0.45
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.3)
     • acoustic match (+1.2)

2. Harvest Hymn — The Willow Trio
   Score: 0.45
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.1)
     • acoustic match (+1.4)

3. Coffee Shop Stories — Slow Stereo
   Score: 0.44
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.0)
     • acoustic match (+1.3)

4. Focus Flow — LoRoom
   Score: 0.43
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.1)
     • acoustic match (+1.2)

5. Midnight Coding — LoRoom
   Score: 0.43
   Reasons:
     • mood mismatch (+0.0)
     • genre mismatch (+0.0)
     • energy fit (+3.2)
     • acoustic match (+1.1)

============================================================
```

The original formula is (0.35)Mood + (0.25)Genre + (0.25)Energy + (0.15)Acoustic = 1

The output is: 
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

I evaluated the recommender in two ways: a set of realistic user profiles run through the CLI, and adversarial edge-case profiles designed to break the scoring function. The user profiles I tested were three normal profiles that had different tastes of "Pop Party-goer", "Lofi Studier", and "Metalhead". I looked to see if the recommended songs was dominated by match in its mood. I also wanted to see that same song did not top every list and that there was reasons for each choice of recommendation. What surpised me were the adversal profiles where it shows the weakness in "score_song()". The out of range energy showed that energy isn't clamped, so "1 - abs(5.0 - 0.82)" goes deeply negative. A better genre+mood match can end up with a negative total, and ranking collapses to "whichever song has the highest energy." Also the empty profile shows that it is not neutral. Defaults make it secretly demand a near-silent (energy 0.0), non-acoustic song.

Because my scores come from hand-set weights, I ran a comparison to see how sensitive the rankings are to them. I moved 10 points from genre to energy because I believe that mood + energy together captures what someone wants to hear right now than genre labels do. What this showed was that for "clean" profiles (Lofi Studier, Metalhead) the top-5 order was identical in both versions because when mood, genre, and energy agree, the weights don't change the outcome. The change only mattered when genre and mood disagreed. The energy pushed mood-matching songs up (e.g. Rooftop Lights, 0.68 → 0.77) and pulled genre-only matches down. It made the out-of-range-energy edge case worse (top score -0.07 → -0.49), since a heavier energy weight amplifies the unclamped energy penalty.

---

## 8. Future Work   

To imporve the model additional user preferences would help create a closer to realisitic music recommender. This model relies heavily on matching a user's mood, but many people choose music based on genre, temp, or artist. Having more to the model would also give better reasonings to why a song is recommended which the user can understand more in. The model could also increase diversity among its top recommendations by including a wider variety of artists, genres, or styles while sitll matching the user's preference. This would help the user to discover new music that may shift their preferences. Rather than consistently listening to the same songs.  

---

## 9. Personal Reflection  

This project helped me take a deeper understanding to how music recommenders work at a basic level. Real world systems like spotify have large databases of user feedback that allows them to implement a more accurate music recommender. Than what I did for this project where I created bias in having mood be prioritized more than the other musical attributes like genre, energy, and acousticness. When I tried to experiment by chaning the weights to have both mood and energy priotized, I expected major changes to the user profiles. But not much was changed only the genre and acousticness caused minor changes because they had lower prioritization. I see not much can be done to have both mood and energy create a better recommendation system. One has to dominate in this system in order to have what the user may want based on the creator's bias of whats important when listening to music. This made me think more on how every action I do in these apps changes the outcome of what is recommened to me. Which I had in mind when using apps like YouTube because once you search something up a couple times. The videos on that topic start showing up soon after. But it does shows how access to significant amount of user data leads to what I mentioned about YouTube videos. Not everyone likes that this happens because eventually it will take out the videos that actally interest the user. In this case it is a better option because my project has bias which not everyone will agree with. 
