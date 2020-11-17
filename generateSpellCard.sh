#!/bin/bash
spellName=$1
class=$2
python3 cardFromURL.py http://prd.5footstep.de/Grundregelwerk/Zauber/${spellName} ${class}

./compileSpellLatex.sh $1 $2
