# Hotel by Toby Fox
#
# Author: Collins Ramsey
# Email: ramseycs@g.cofc.edu
# Class: CITA 180   
# Assignment: Homework #3
# Due Date: February 21
#
# Purpose: Plays the first few measures of a cheery song
# called Hotel by Toby Fox, creater of Undertale
#
# Input: none
#
# Output: A Score of music with 3 Parts consisting of a bass,
# double bass, and melody.

from music import *

#### Organizes a list of Parts and Phrases used in the Score

hotelScore = Score(90)  # sets the tempo of the entire score to 90

bassPart = Part(PIANO, 0)          # Assigns Piano to bass
dblbassPart = Part(PICKED_BASS, 1)      # Assigns Bass to dblbass
riftPart = Part(TRUMPET, 2)      # Assigns Trumpet to melody

bassPhrase = Phrase(0.0)        # starts immediately
dblbassPhrase = Phrase(15.0)  # starts at 15 seconds
riftPhrase = Phrase(32.0) # starts at 32 seconds

# Bass notes and lists
basspitches1 =   [A2, REST, [C3, E3], REST, E2, [C3, E3], REST, A2, REST,
                 [C3, E3], REST, [C3, E3], REST, A2, [C3, E3], REST]
bassdurations1 = [SN, SN,    SN,      SN,   SN,  SN,      SN,   SN, SN,
                  SN,      SN,    SN,      SN,   SN,  SN,      SN]
basspitches2 = [G2, REST, [B2, D3], REST, D2, [B2, D3], REST, G2, REST,
               [B2, D3], REST, [B2, D3], REST, G2, [B2, D3], REST]
basspitches3 = [G2, REST, [B2, D3], REST, D2, [B2, D3], REST, G2, REST,
               [B2, D3], REST, [B2, D3], REST, GS2, [B2, D3], REST]
basspitches4 = [A2, REST, [C3, E3], REST, B2, [A2, D3], REST, C3, REST,
               [B2, E3, G3], REST, [B2, E3, G3], D3, REST, [B2, D3, FS3], REST]
basspitches5 =   [A1, A2, B1, B2, [C2, C3]]
bassdurations2 = [EN, EN, SN, EN,  QN    ]
# add bass list to Phrase then add to Part
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches2, bassdurations1)
bassPhrase.addNoteList(basspitches3, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches2, bassdurations1)
bassPhrase.addNoteList(basspitches4, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches2, bassdurations1)
bassPhrase.addNoteList(basspitches3, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches1, bassdurations1)
bassPhrase.addNoteList(basspitches2, bassdurations1)
bassPhrase.addNoteList(basspitches5, bassdurations2)
bassPart.addPhrase(bassPhrase)
bassPart.setDynamic(85) # change of dynamic for bass

# Double bass notes and lists
preBasspitch =    [REST, AF1]
preBassduration = [SN, DEN]
dblbasspitches1 =   [A1, A1, E1, A1, A1, A1, E1, B1]
dblbassdurations1 = [DEN,SN ,DEN,EN, EN, SN, EN, EN]
dblbasspitches2 = [G1, G1, D1, G1, G1, G1, D1, A1]
dblbasspitches3 =   [A1, B1, C2, REST, D2]
dblbassdurations2 = [QN, DEN,QN, SN,   QN]
# add double bass list to Phrase then add to Part
dblbassPhrase.addNoteList(preBasspitch, preBassduration)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches2, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches3, dblbassdurations2)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches2, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches1, dblbassdurations1)
dblbassPhrase.addNoteList(dblbasspitches2, dblbassdurations1)
dblbassPart.addPhrase(dblbassPhrase)
dblbassPart.setDynamic(120) # change of dynamic for dblbass

# Melody rift notes and lists
riftpitches1 =   [D3, D4, A3, REST]
riftdurations1 = [QN, DEN, HN, SN]
riftpitches2 =   [G3, D4, D3, REST]
riftpitches3 =   [D3, FS3, D4, REST, E4]
riftdurations3 = [QN, DEN, DQN,SN,   EN]
riftpitches4 =   [D4, A3, G3, G3, G4, A4, B4, A4, GS4, E4, B3]
riftdurations4 = [QN, DEN,SN, SN, SN, SN, SN, SN, SN,  SN, SN]
riftpitches5 =   [G3, D4, D3, D3, D4, G4, A4, B4, A4, G4, E4]
riftdurations5 = [QN, DEN,SN, SN, SN, SN, SN, SN, SN, SN, SN]
riftpitches6 =   [[D4, B3, A3, FS3], [FS4, D4, B3, A3], 
                 [D4, B3, A3, FS3], REST, [E4, B3, FS3]]
riftdurations6 = [ QN,                DEN, 
                  DQN,              SN,    EN]
riftpitches7 =   [[D4, B3, A3, FS3], [A3, E3], [G4, D4, B3]]
riftdurations7 = [QN,                 DEN,      HN]
# add melody rift list to Phrase then add to Part
riftPhrase.addNoteList(riftpitches1, riftdurations1)
riftPhrase.addNoteList(riftpitches2, riftdurations1)
riftPhrase.addNoteList(riftpitches3, riftdurations3)
riftPhrase.addNoteList(riftpitches4, riftdurations4)
riftPhrase.addNoteList(riftpitches1, riftdurations1)
riftPhrase.addNoteList(riftpitches5, riftdurations5)
riftPhrase.addNoteList(riftpitches6, riftdurations6)
riftPhrase.addNoteList(riftpitches7, riftdurations7)
riftPart.addPhrase(riftPhrase)
riftPart.setDynamic(115) # change in dynamic for rift

# add Parts to Score and play Score
hotelScore.addPart(bassPart)
hotelScore.addPart(dblbassPart)
hotelScore.addPart(riftPart)

Play.midi(hotelScore)