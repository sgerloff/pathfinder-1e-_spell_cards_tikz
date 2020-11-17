# pathfinder-1e-_spell_cards_tikz
These scripts can be used to fetch data from http://prd.5footstep.de/, which is used to generate PDF's of spell cards using LaTeX and specifically Tikz. I have created these scripts to become familar with python, as such they are very basic. Due to the lack of further P&P sessions in pathfinder 1e, I do not plan to improve the code further. If anyone wants to use these scripts as a starting point: Use a better source of spell data to prevent messy parsing of the html code.

# Basic Usage
To generate a new spell card, such as for the spell "Kalte Hand", use
```sh
./generateSpellCard.sh KalteHand MAG
```
where the second argument is an identifier string for the intended class. (HXM,MAG,BAR,PAL,KLE,WAL)

![Alt text](https://github.com/sgerloff/pathfinder-1e-_spell_cards_tikz/blob/master/example.jpg?raw=true "Title")

This should generate the spell card and move it to the "cards" folder.

# Common Cleanup Step
When the automatic generation produces undesired results, such as clipping the rule text due to its length, the best approach is to quickly change the generated TeX-file. For the example above the file can be found at ```KalteHand_MAG/KalteHand_MAG.tex```. Just simply change the text blocks and save. Then compile the latex code again using
```sh
./compileSpellLatex.sh KalteHand MAG
```
