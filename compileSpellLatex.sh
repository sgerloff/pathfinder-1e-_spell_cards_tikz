#!/bin/bash
spellName=$1
class=$2

cd ${spellName}_${class}
pdflatex ${spellName}_${class}.tex
mv ${spellName}_${class}.pdf ../cards/${spellName}_${class}.pdf
