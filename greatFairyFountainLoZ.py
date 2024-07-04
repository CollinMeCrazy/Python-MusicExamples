# greatFairyFountainLoZ.py
#
# Author:  Collins Ramsey
# Email:   ramseycs@g.cofc.edu
# Class:   CITA 180   
# Assignment: Homework #2
# Due Date:   February 10
#
# Purpose: Plays the melody Great Fairy Fountain from
# the series Legend of Zelda
#
# Input:   Many notes piled into a set of lists then put into 
# a Phrase
#
# Output:  A rather legnthy, high pitched melody played at 
# 75 beats per minute

from music import *     # add music library

pitches1 = [A6, D6, BF5, G5, G6, D6, BF5, G5, FS6, D6, BF5, G5]   # a bunch of notes
durations1 = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN]     # assigned to a phrase

pitches2 = [G6, D6, BF5, G5, G6, C6, A5, F5, F6, C6, A5, F5]

pitches3 = [E6, C6, A5, F5, F6, C6, A5, F5, F6, BF5, G5, E5]

pitches4 = [E6, BF5, G5, EF5, EF6, BF5, G5, E5, E6, BF5, G5, EF5]

pitches5 = [E6, A5, F5, D5, D6, A5, F5, D5, CS6, A5, F5, D5, D6, A5, F5, D5]
durations2 = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN]

pitches6 = [G6, D6, BF5, G5, BF6, EF6, C6, A5, A6, EF6, C6, A5]

pitches7 = [GS6, EF6, C6, A5, A6, EF6, C6, A5, C7, D6, BF5, G5]

pitches8 = [BF6, D6, BF5, G5, A6, D6, BF5, G5, BF6, D6, BF5, G5]

pitches9 = [A6, BF5, G5, E5, G6, BF5, G5, EF5, F6, BF5, G5, E5, E6, BF5, G5, EF5]

melody = Phrase()    # creates an empty phrase

melody.setTempo(75)     # sets the tempo a little faster to blend notes together 

melody.addNoteList(pitches1, durations1)  # adds the notes to the phrase
melody.addNoteList(pitches2, durations1)
melody.addNoteList(pitches3, durations1)
melody.addNoteList(pitches4, durations1)
melody.addNoteList(pitches5, durations2)  # only needs two types of duration
melody.addNoteList(pitches1, durations1)
melody.addNoteList(pitches6, durations1)
melody.addNoteList(pitches7, durations1)
melody.addNoteList(pitches8, durations1)
melody.addNoteList(pitches9, durations2)

Play.midi(melody)    # plays melody 