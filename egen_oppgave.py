#Oppgave: Skriv tre på rad spill :-)

import random

class Brett():
    def __init__(self):
        #Definerer spillebrettet som en liste med 9 indexer
        list = []
        for i in range(9):
            list.append('')
        self._brett = list

    def tegnBrett(self):
        i = 0
        #print(self._brett)
        print('[ '+ str(self._brett[i]) + ' ]' + '[ ' + str(self._brett[i+1]) + ' ]' + '[ '+ str(self._brett[i+2]) + ' ]')
        print('[ '+ str(self._brett[i+3]) + ' ]' + '[ ' + str(self._brett[i+4]) + ' ]' + '[ '+ str(self._brett[i+5]) + ' ]')
        print('[ '+ str(self._brett[i+6]) + ' ]' + '[ ' + str(self._brett[i+7]) + ' ]' + '[ '+ str(self._brett[i+8]) + ' ]')

    def endreBrett(self,index,verdi):
        self._brett[index] = verdi

    def sjekkTrePaaRaad(self):
        #012  #036 #048
        #345  #147 #246
        #678  #258
        winValues = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #Definerer alle kombinasjoner som gir tre på rad
        spillerListe = []
        fiendeListe = []
        x = self._brett

        #Fungerer som den skal - lager en liste over indexer som er fylt av spiller
        i = 0
        for elem in x:
            if elem == 'x':
                spillerListe.append(i)
            i += 1

        #Fungerer som den skal - lager en liste over indexer som er fylt av fiende
        i = 0
        for elem in x:
            if elem == 'o':
                fiendeListe.append(i)
            i += 1

        #Sjekk hver "tre på rad kombinasjon"
        for elem in winValues:
            if elem[0] in spillerListe and elem[1] in spillerListe and elem[2] in spillerListe:
                print("Spiller fikk tre på rad! Gratulerer!")

        for elem in winValues:
            if elem[0] in fiendeListe and elem[1] in fiendeListe and elem[2] in fiendeListe:
                print("Fiende fikk tre på rad! Å nei!")



spilleBrett = Brett()

def spillerTur():
    spilleBrett.sjekkTrePaaRaad()
    spilleBrett.tegnBrett()
    svar = int(input('Velg en index (1-9)')) - 1 #trekk fra 1 pga. nullindeksering
    if spilleBrett._brett[svar] != 'x' and spilleBrett._brett[svar] != 'o':
        spilleBrett.endreBrett(svar,'x')
    else:
        print('Feltet er opptatt!')
        spillerTur()
    fiendeTur()

def fiendeTur():
    muligeValg = []
    for i in range(len(spilleBrett._brett)):
        if spilleBrett._brett[i] != 'x' and spilleBrett._brett[i] != 'o':
            muligeValg.append(i)
    print(muligeValg)
    random.shuffle(muligeValg)
    if muligeValg:
        spilleBrett._brett[muligeValg[0]] = 'o'
    else:
        print('Spillet er over!')
    spillerTur()



spillerTur()
