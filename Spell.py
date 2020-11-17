import itertools
import re
class Spell:
    name = ""
    stats = []
    description = []
    reference = ""

    misc=[]

    descriptionS=""
    classS=''
    spellLevelN=''
    timeS=''
    componentS=''
    durationS=''
    resistanceF='defenceNon.tex'
    targetS=''
    rangeS=''

    flagColor1=''
    flagColor2=''

    def setSpellFromText( self, text ):
        self.setListsFromText(text)
        self.parseStatsFromList()
        self.setDescriptionString()

    def setListsFromText( self, text):
        blocks=text.split("\n\n")
        # blocks.pop(0)
        print(blocks)
        self.name=blocks[0].replace("\n","")
        self.extractStatsFromBlock( blocks[1] )
        self.extractReferenceFromBlock( blocks[-1] )
        blocks.pop(0)
        blocks.pop(0)
        blocks.pop(-1)
        self.description=blocks

    def extractStatsFromBlock( self, block ):
        lines=block.splitlines()
        for line in lines:
            tmp=line.split("; ")
            for t in tmp:
                self.stats.append(t.split(": "))
        self.stats = [x for x in self.stats if x != ['']]

    def extractReferenceFromBlock( self, block ):
        line=block.splitlines()[1].split(": ")
        if line[0] in ['Referenz']:
            self.reference=line[1].replace('Seite ','\\bf ',1)
        else:
            print("ERROR: No reference page found!")

    def setDescriptionString( self ):
        for x in self.description:
            diceFormat = re.compile('\s\d*W\d*\s')
            diceList = diceFormat.findall(x)
            for d in diceList:
                x=x.replace( d, ' {\\bf%s}' % d, 1 )
            self.descriptionS+=x
            self.descriptionS+='\\\\\n\n'
        tmp=''
        print("self.misc")
        print(self.misc)
        for x in self.misc:
            print(x)
            if len(x) == 2:
                tmp += '{\\bf %s:} %s \\\\' % (x[0],x[1])
            else:
                print("omitted!")
        self.descriptionS = tmp + '\n\n' + self.descriptionS
        self.descriptionS.rstrip()

    def parseStatsFromList( self ):
        print("stats")
        print(self.stats)
        for stat in self.stats:
            if stat[0] in ('Schule'):
                print(stat)
            elif stat[0] in ('Grad'):
                self.setClassAndSpellLevelNumber(stat[1])
            elif stat[0] in ('Zeitaufwand'):
                self.setTime(stat[1])
            elif stat[0] in ('Komponenten'):
                self.setComponent(stat[1])
            elif stat[0] in ('Reichweite'):
                self.setRange(stat[1])
            elif stat[0] in ('Ziele'):
                self.setTarget( stat[1] )
            elif stat[0] in ('Wirkungsdauer'):
                self.setDuration( stat[1] )
            elif stat[0] in ('Rettungswurf'):
                self.misc.append(stat)
            elif stat[0] in ('Zauberresistenz'):
                self.setResistance(stat[1])
            else:
                self.misc.append(stat)

    def setClassAndSpellLevelNumber( self, text ):
        spellLevelFormat=re.compile('\d\d*')
        spellLevelList=spellLevelFormat.findall(text)
        self.spellLevelN=spellLevelList[0]
        text = text.replace(self.spellLevelN, '')
        self.classS=text.split(",")
        self.classS= [x.split("/") for x in self.classS]
        print("self.classS")
        print(self.classS)
        self.classS= list(itertools.chain.from_iterable(self.classS))
        self.classS = [x.strip() for x in self.classS]
        self.classS = [x.replace(u'\xa01', u'') for x in self.classS]

    def setTime( self, text ):
        print(text)
        text = text.replace("Standard-Aktion", "StdA")
        text = text.replace("Minuten", "Min")
        self.timeS = text

    def setComponent( self, text ):
        print(text)
        if text in ('V, G'):
            self.componentS = text.replace(" ", "")
        elif text in ('V, G, M (ein wenig Wolle oder ein ähnliches'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Ein wenig Wolle oder ein ähnliches Material'])
        elif text in ('V, G, M (ein Stückchen Wolle oder ein kleiner Klumpen Wachs)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Ein Stückchen Wolle oder ein kleiner Klumpen Wachs'])
        elif text in ('V, G, M (Butter)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Butter'])
        elif text in ('V, G, M/GF (ein wenig Ruß und Salz)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Ein wenig Ruß und Salz'])
        elif text in ('V, M/GF (das Lehmmodell einer Zikkurats)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Das Lehmmodell einer Zikkurats'])
        elif text in ('V, G, M (eine Feuerquelle)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Eine Feuerquelle'])
        elif text in ('V, G, F (ein Stückchen Pelz)'):
            self.componentS='V,G,F*'
            self.misc.append(['Fokus','Ein Stückchen Pelz'])
        elif text in ('V, M/GF (ein Glühwürmchen)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Ein Glühwürmchen'])
        elif text in ('V, G, F (ein Stückchen gehärtetes Leder)'):
            self.componentS='V,G,F*'
            self.misc.append(['Fokus','Ein Stückchen gehärtetes Leder'])
        elif text in ('V, G, M/GF (Talg, Schwefel und Eisenpulver)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Talg, Schwefel und Eisenpulver'])
        elif text in ('V, G, M (ein Kügelchen Fledermausdung und Schwefel)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Ein Kügelchen Fledermausdung und Schwefel'])
        elif text in ('V, G, M (ein Tropfen Öl und ein kleines Stück Feuerstein)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Ein Tropfen Öl und ein kleines Stück Feuerstein'])
        elif text in ('V, G, M/GF (eine in Gummiarabikum eingelassene Wimper)'):
            self.componentS='V,G,M*'
            self.misc.append(['Material','Eine in Gummiarabikum eingelassene Wimper'])
        else:
            self.componentS = text.replace(" ", "")


    def setRange( self, text ):
        print(text)
        if text in ('Nah (7,50 m + 1,50 m/2 Stufen)'):
            self.rangeS = '5F+1F/2 Stufen'
        elif text in ('Nah (7,50 m + 1,50 m/Stufe)'):
            self.rangeS = '5F+1F/Stufe'
        elif text in ('Mittel (30 m + 3 m/Stufe)'):
            self.rangeS = '20F+2F/Stufe'
        elif text in ('Lang (120 m + 12 m/Stufe)'):
            self.rangeS = '80F+8F/Stufe'
        elif text in ('3 m'):
            self.rangeS = '2F'
        elif text in ('18 m'):
            self.rangeS = '12F'
        elif text in ('Persönlich'):
            self.rangeS = text
        elif text in ('Berührung'):
            self.rangeS = text
        elif text in ('Persönlich oder Berührung'):
            self.rangeS = 'Persn. o. Berühr.'
        else:
            print(text)

    def setTarget( self, text ):
        print(text)
        if text in ('Eine oder mehrere berührte Kreaturen (bis zu 1/Stufe)'):
            self.targetS = '1 Ziel/Stufe'
        elif text in ('Ein nichtmagischer Gegenstand, der nicht benutzt wird und nicht mehr als 5 Pfund wiegt'):
            self.targetS = '1 nichtmag. Obj.*'
        elif text in ('Ein Gegenstand von bis zu 1 Pfd./Stufe'):
            self.targetS = '1 Obj.-1 Pfd./Stufe'
        elif text in ('Eine humanoide Kreatur mit 4 oder weniger TW'):
            self.targetS = '1 humanoides Ziel*'
        elif text in ('Ein Gegenstand oder ein Bereich von 3 m x 3 m'):
            self.targetS = '1 Obj. oder 2F$\\times$2F'
        elif text in ('Du'):
            self.targetS = text
        elif text in ('Berührte Kreatur'):
            self.targetS = '1 berührtes Ziel'
        elif text in ('Berührte lebende Kreatur'):
            self.targetS = '1 berührtes leb. Ziel'
        elif text in ('Eine Feuerquelle, bis zu einem Würfel mit 6 m Kantenlänge'):
            self.targetS = '1 Feuerquelle*'
        elif text in ('Berührter Gegenstand'):
            self.targetS = '1 berührtes Obj.'
        elif text in ('Bis zu fünf Kreaturen, von denen keine weiter als 4,50 m von den anderen entfernt sein darf'):
            self.targetS = '5 Ziele, 3F Abst.'
        elif text in ('Fünfzig Projektile, die sich beim Wirken des Zaubers alle berühren müssen'):
            self.targetS = '50 Projektile*'
        elif text in ('Du oder eine Kreatur oder ein Gegenstand, die nicht mehr als 100 Pfd./Stufe wiegen dürfen'):
            self.targetS = 'Du, 1 Ziel o. 1 Obj*'
        else:
            print("target not found!!!")

    def setDuration( self, text ):
        print(text)
        if text in ('Augenblicklich'):
            self.durationS='Agnbl.'
        elif text in ('Konzentration'):
            self.durationS='Konz.'
        elif text in ('1 Runde/Stufe'):
            self.durationS='1R/S'
        elif text in ('1 Min./Stufe'):
            self.durationS='1m/S'
        elif text in ('Konzentration + 1 Runde/Stufe (A)'):
            self.durationS='K+1R/S'
        elif text in ('1W4+1 Runden oder 1W4+1 Runden nachdem Kreaturen die\xa0Rauchwolke verlassen haben (siehe Text)'):
            self.durationS='1W4+1R'
        elif text in ('Konzentration, bis zu 1 Min./Stufe (A)'):
            self.durationS='K,1m/S'
        else:
            text=text.replace("Runde","R")
            text=text.replace("Stufe", "S")
            text=text.replace(" (A)", "")
            text=text.replace("Stunde","h")
            text=text.replace("Min.","m")
            text.strip()
            self.durationS=text

    def setResistance( self, text ):
        if text in ('Ja'):
            self.resistanceF='defence.tex'
        elif text in ('Ja (harmlos, Gegenstand)'):
            self.resistanceF='defence.tex'
        elif text in ('Ja (harmlos) (siehe Text)'):
            self.resistanceF='defence.tex'
        elif text in ('Nein'):
            self.resistanceF='defenceNon.tex'
        else:
            print(text)

    def setClass( self, text ):
        print(self.classS)
        if text in self.classS:
            if text in ('HXM'):
                self.classS = text
                self.flagColor1="A82816"
                self.flagColor2="ED431E"
            elif text in ('MAG'):
                self.classS = text
                self.flagColor1="14568F"
                self.flagColor2="338FA8"
            elif text in ('BAR'):
                self.classS = text
                self.flagColor1="FF9E56"
                self.flagColor2="FFDC59"
            elif text in ('PAL'):
                self.classS = text
                self.flagColor1="F6E497"
                self.flagColor2="FCFAE1"
            elif text in ('KLE'):
                self.classS = text
                self.flagColor1="F6E497"
                self.flagColor2="FCFAE1"
            elif text in ('WAL'):
                self.classS = text
                self.flagColor1="AAC123"
                self.flagColor2="DDE200"
            else:
                print("Color not defined!!!")
        else:
            print("No matching class!!!")
