# boxbot

a fun training tool for shadowboxing or bag work

## how it works

I transcribed every meaningful punch thrown in a few world-class boxing fights. This builds a Markov chain to model the frequencies of the six punches and the transitions between them (e.g. a cross is likely to come after a jab), then uses it to generate an infinite, realistic sequence of punches and combinations. Each punch is announced one at a time, so they can be followed while shadowboxing or working the bag.

To start:

```sh
python3 play.py
```

## other notes

- There are only two full fights transcribed (so far).
- The fight transcriptions also include the target of each of the punches (`h` for head, `b` for body). These aren't being used right now because there aren't enough data to effectively double the number of states, but head/body frequencies could be modelled in a separate Markov chain and used in combination with the punch chain.
- `tts.py` generates new audio files using the Google Cloud TTS service.
