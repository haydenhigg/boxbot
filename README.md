# boxbot

a fun training tool for shadowboxing or bag work

## how it works

I transcribed every meaningful punch thrown in a few world-class boxing fights. `play.py` builds a Markov chain to model the frequencies of the six punches and the transitions between them (e.g. a cross is likely to come after a jab), then generates an infinite sequence of punches and combinations with those same frequencies. This creates realistic punches and combinations to follow while shadowboxing or working the bag, and each punch is announced one at a time, as by a coach.

## other notes

- There are only two full fights transcribed (so far).
- The fight transcriptions also include the target of each of the punches (`h` for head, `b` for body). These aren't being used right now because there aren't enough data to effectively double the number of states, but head/body frequencies could be modelled in a separate Markov chain and used in combination with the punch chain.
- `tts.py` generates new audio files using the Google Cloud TTS service.
