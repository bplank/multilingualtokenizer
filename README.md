# multilingualtokenizer

A trivial punctuation-based sentence splitter and tokenizer for
multi-lingual data.

Requires python3 and the regex package. Install with `pip install regex` or `conda install regex`.

Usage: 

```
python trivialssplitter.py FILE > OUTPUT.s
```

```
python tinytokenizer.py FILE > OUTPUT.s
python tinytokenizer.py --conll FILE > OUTPUT.t
```

The `--conll` option outputs one token per line. Default is to have one sentence per line.



