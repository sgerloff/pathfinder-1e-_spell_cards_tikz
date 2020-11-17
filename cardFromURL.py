#!/usr/bin/python3.6
from getTextFromURL import getTextFromURL
from Spell import Spell
import re
import os
import sys

print(str(sys.argv))
argumentList=sys.argv
argumentList=[x.rstrip() for x in argumentList]
print(argumentList)
url = str(argumentList[1])
classIn = str(argumentList[2])
# url = 'http://prd.5footstep.de/Grundregelwerk/Zauber/KalteHand'
#url= 'http://prd.5footstep.de/Grundregelwerk/Zauber/Chaoshammer'
tag = getTextFromURL( url )

mySpell = Spell()
mySpell.setSpellFromText(tag.text())
mySpell.setClass( classIn )

fileName=mySpell.name.replace(" ","")
if not os.path.exists("%s_%s" %(fileName,classIn)):
    os.makedirs("%s_%s" %(fileName,classIn))

templateFile = open("spellCardLayout/main.tex","r")
templateString = templateFile.read()

templateString = templateString.replace( "_flagColor1R_", mySpell.flagColor1)
templateString = templateString.replace( "_flagColor2R_", mySpell.flagColor2)

templateString = templateString.replace( "_spellNameR_", mySpell.name)
templateString = templateString.replace( "_descriptionR_", mySpell.descriptionS)
templateString = templateString.replace( "_classR_", mySpell.classS)
templateString = templateString.replace( "_spellLevelR_", mySpell.spellLevelN)
templateString = templateString.replace( "_timeR_", mySpell.timeS)
templateString = templateString.replace( "_componentR_", mySpell.componentS)
templateString = templateString.replace( "_durationR_", mySpell.durationS)
templateString = templateString.replace( "_resistanceR_", mySpell.resistanceF)
templateString = templateString.replace( "_targetR_", mySpell.targetS)
templateString = templateString.replace( "_rangeR_", mySpell.rangeS)
templateString = templateString.replace( "_pageR_", mySpell.reference)

file=open("%s_%s/%s_%s.tex"% (fileName, classIn, fileName, classIn),"w+")
file.write(templateString)
file.close()

# import subprocess
# subprocess.check_output("cd KalteHand_HXM; pdflatex KalteHand.tex", shell=True)
