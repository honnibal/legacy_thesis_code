#!/usr/bin/env bash
python scripts/getLexicon.py $1
python scripts/markedupAbsences.py $1
python scripts/extractGrammar.py $1
python scripts/validateGrammar.py $1
