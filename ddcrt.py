"""
    *************************************************************************
    *                                                                       *
    *                   DUNGEON MASTER'S PERSONNEL SERVICE                  *
    *                 (40 COLUMN BY 16 LINE CRT DISPLAY ONLY )              *
    *                   SAVE AS "ddcrt.py" - VERSION 1.2                    *
    *                                                                       *
    *************************************************************************
    *                GENERATES PLAYER CHARACTERISTICS FOR FANTASY           *
    *                ROLE - PLAYING GAME "DUNGEONS & DRAGONS" Tm            *
    *************************************************************************
    *               BY TROY SCOTT INSPIRED BY THE BASIC PROGRAM             *
    *                           BY JOSEPH C SPANN                           *
    *                      DRAGON MAGAZINE, JUNE 1983                       *
    *                                                                       *
    *************************************************************************
    * VERSION 1.2 - Object-oriented                                         *
    * VERSION 1.1 - Support for Character Files                             *
    * VERSION 1.0 - Original                                                *
    *************************************************************************
"""

import csv
import glob
import json
import os
import random

LOG=[]

AB=['unused','STRENGTH','CONSTITUTION','INTELLIGENCE','DEXTERITY','WISDOM','CHARISMA']
RC=['unused','FIGHTER','MAGIC USER','CLERIC','HALFLING','ELF','DWARF','THIEF']
SR=['unused','POISON or DEATH RAY','MAGIC WAND','TURN TO STONE or PARALYSIS','DRAGON BREATH','SPELLS or MAGIC STAFF']
ALT=['unused','LAWFUL','NEUTRAL','CHAOTIC']
GET=['unused','GOOD','EVIL']

class Wizard():
    def __init__(self):
        pass

    def welcomeScreen(self,any_PC):

        any_PC.writeline('             \                  /               ')
        any_PC.writeline('    _________))                ((_________      ')
        any_PC.writeline('   /.-------./\    \    /    //\.-------.\\     ')
        any_PC.writeline('  //#######//##\   ))  ((   //##))#######\\\    ')
        any_PC.writeline(' //#######//###(( ((    ))  ))###\\\########\\\ ')
        any_PC.writeline('((#######((#####\  \\\  //  //#####))########)) ')
        any_PC.writeline(' \##   ###\######\   \)(/  //#####/###`    ##/  ')
        any_PC.writeline('  )      #)    ###\->oo<- /##      (#       (   ')
        any_PC.writeline('         (         \`..` /          )           ')
        any_PC.writeline('                    \\""(                       ')
        any_PC.writeline('                     - )                        ')
        any_PC.writeline('                     / /                        ')
        any_PC.writeline('                    ( /\                        ')
        any_PC.writeline('                    /\| \                       ')
        any_PC.writeline('                   (  \                         ')
        any_PC.writeline('                       )                        ')
        any_PC.writeline('                      /                         ')
        any_PC.writeline('                     (                          ')
        any_PC.writeline('                     `~                         ')

        any_PC.writeline('')
        any_PC.writeline('-------------------------------------------------')
        any_PC.writeline('            DM\'S PERSONNEL SERVICE              ')
        any_PC.writeline('                 Version 1.0                     ')
        any_PC.writeline('')
        any_PC.writeline('        PRODUCES CHAR. ABILITY SCORES            ')
        any_PC.writeline('                     FOR                         ')
        any_PC.writeline('             DUNGEONS & DRAGONS Tm               ')
        any_PC.writeline('          3RD EDITION, DECEMBER 1979             ')
        any_PC.writeline('             AKA THE \'BLUE BOOK\'               ')
        any_PC.writeline('')
        any_PC.writeline('       BY GARY GYGAX AND DAVE ARNESON            ')
        any_PC.writeline('            EDITED BY ERIC HOLMES                ')
        any_PC.writeline('')
        any_PC.writeline('        Dragon ASCII Art by Ed Zahurak           ')
        any_PC.writeline('-------------------------------------------------')

    def actionScreen(self,any_PC):

        ACCEPTACTION=False
        while ACCEPTACTION!=True:
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('       ACTION LIST           ')
            any_PC.writeline('  (1) LOAD CHARACTER FILE    ')
            any_PC.writeline('  (2) CREATE NEW CHARACTER   ')
            any_PC.writeline('  (3) EDIT CHARACTER         ')
            any_PC.writeline('  (0) EXIT                   ')
            any_PC.writeline('')
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('SELECT AN ACTION')
            try:
                AC = int(input('NUMBER FROM THE TABLE ABOVE:')) 
            except:
                any_PC.writeline('ERROR: INVALID INPUT, TYPE A VALUE FROM 0 TO 3')
            if AC < 0 or AC > 3:
                any_PC.writeline('ERROR: INVALID RANGE, TYPE A VALUE FROM 0 TO 3')
                ACCEPTACTION = False
            else:
                ACCEPTACTION = True

        return AC

    def loadScreen(self,any_PC):

        chflist = glob.glob('*.chf')
        if len(chflist) != 0:
            LOADCHAR = True
            chardict = loadcharfile(any_PC)
        else:
            any_PC.writeline("NO CHARACTER FILES FOUND.")

    def genabsScreen(self,any_PC):

        ACCEPTABILITIES=False
        while ACCEPTABILITIES!=True:

            # STRENGTH & CONSTITUTION RATIO CHECK
            A=0
            while A<0.67 or A>1.5:
                ST=any_PC.roll3d6()
                CO=any_PC.roll3d6()
                A=ST/CO
            any_PC.strength(ST)
            any_PC.constitution(CO)
            DX=any_PC.roll3d6()
            any_PC.dexterity(DX)

            # INTELLIGENCE & WISDOM RATIO CHECK
            B=0
            while B<0.67 or B>1.5:
                IN=any_PC.roll3d6()
                WI=any_PC.roll3d6()
                B=IN/WI
            any_PC.intelligence(IN)
            any_PC.wisdom(WI)
            CH=any_PC.roll3d6()
            any_PC.charisma(CH)

            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('PRESS Y TO ACCEPT CHARACTER ABILITIES')
            any_PC.writeline('OR ANY OTHER KEY TO RETRY: ')
            C = input()
            any_PC.writeline(C)

            if C=='Y':
                ACCEPTABILITIES=True

        # Assign abilities to character instance
        any_PC.ST = ST
        any_PC.CO = CO
        any_PC.IN = IN
        any_PC.DX = DX
        any_PC.WI = WI
        any_PC.CH = CH

    def raceclassScreen(self,any_PC):

        # RACE/CLASS SELECTION & CHECKING
        ACCEPTRACECLASS=False
        while ACCEPTRACECLASS!=True:
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('          CLASS/RACE LIST               ')
            any_PC.writeline('  (1) FIGHTER          (4) HALFLING     ')
            any_PC.writeline('  (2) MAGIC USER       (5) ELF          ')
            any_PC.writeline('  (3) CLERIC           (6) DWARF        ')
            any_PC.writeline('            (7) THIEF                   ')
            any_PC.writeline('')
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('SELECT THE RACE/CLASS THAT YOU WISH')
            any_PC.writeline('YOUR CHARACTER TO HAVE AND ENTER THE')
            try:
                CN=int(input('NUMBER FROM THE TABLE ABOVE:')) # Class/Race
            except:
                any_PC.writeline('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 7')
            if CN < 1 or CN > 7:
                any_PC.writeline('ERROR: INVALID RANGE, TYPE A VALUE FROM 1 TO 7')
                ACCEPTLVL = False
            else:
                ACCEPTLVL = True
            ACCEPTRACECLASS=any_PC.raceclass(CN,any_PC)

        # Assign RACE/CLASS and HIT DICE to character instance
        any_PC.CN = CN
        any_PC.HF = any_PC.hitdice(CN)

    def levelScreen(self,any_PC):

        # CHARACTER LEVEL ASSIGNED AND HIT POINTS CALCULATED
        ACCEPTLVL=False
        while ACCEPTLVL!=True:
            any_PC.writeline('CHARACTER LEVEL RANGE..ONE (1) TO FIVE (5)')
            try:
                LL=int(input('AT WHICH LEVEL WILL CHARACTER START:'))
            except:
                any_PC.writeline('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 5')
            if LL < 1 or LL > 5:
                any_PC.writeline('ERROR: INVALID RANGE, TYPE A VALUE FROM 1 TO 5')
                ACCEPTLVL = False
            else:
                ACCEPTLVL = True
    
        # Assign character level and hit points to character instance
        any_PC.LL = LL
        any_PC.PT = any_PC.chlevel(LL,any_PC.CO,any_PC.HF)

        # CLERIC SKILLS ASSIGNED BY LEVEL
        if any_PC.CN==3:
            any_PC.clericskills(LL)

        # THIEF'S SKILLS ASSIGNED BY LEVEL
        if any_PC.CN==7:
            any_PC.thiefskills(LL)

    def behavScreen(self,any_PC):
        ACCEPTCODE=False
        while ACCEPTCODE!=True:
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('CHARACTER CODE OF BEHAVIOR LIST ')
            any_PC.writeline('  (1) GOOD     ')
            any_PC.writeline('  (2) EVIL    ')
            any_PC.writeline('')
            any_PC.writeline('SELECT THE CODE THAT YOU WISH')
            any_PC.writeline('YOUR CHARACTER TO HAVE AND ENTER THE')
            any_PC.writeline('CHARACTER CODE RANGE..ONE (1) TO TWO (2)')
            try:
                GE=int(input('NUMBER FROM THE TABLE ABOVE:'))
            except:
                any_PC.writeline('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 2')
                ACCEPTCODE = False
            if GE < 1 or GE > 2:
                any_PC.writeline('ERROR: INVALID RANGE, TYPE A VALUE FROM 1 TO 2')
                ACCEPTCODE = False
            else:
                ACCEPTCODE = True
        any_PC.GE = GE

    def alignScreen(self,any_PC):
        ACCEPTALGN=False
        while ACCEPTALGN!=True:
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('CHARACTER ALIGNMENT LIST ')
            any_PC.writeline('  (1) LAWFUL     ')
            any_PC.writeline('  (2) NEUTRAL    ')
            any_PC.writeline('  (3) CHAOTIC    ')
            any_PC.writeline('')
            any_PC.writeline('-------------------------------------------------')
            any_PC.writeline('SELECT THE ALIGNMENT THAT YOU WISH')
            any_PC.writeline('YOUR CHARACTER TO HAVE AND ENTER THE')
            any_PC.writeline('CHARACTER ALIGNMENT RANGE..ONE (1) TO THREE (3)')
            try:
                AL=int(input('NUMBER FROM THE TABLE ABOVE:'))
            except:
                any_PC.writeline('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 3')
                ACCEPTALGN = False
            if AL < 1 or AL > 3:
                any_PC.writeline('ERROR: INVALID RANGE, TYPE A VALUE FROM 1 TO 3')
                ACCEPTALGN = False
            else:
                ACCEPTALGN = True
        any_PC.AL = AL

class Character():
    def __init__(self):

        # Character attributes
        ST=0 # STRENGTH
        CO=0 # CONSTITUTION
        IN=0 # INTELLIGENCE
        DX=0 # DEXTERITY
        WI=0 # WISDOM
        CH=0 # CHARISMA

        CN=0 # RACE/CLASS
        HF=0 # HIT DICE

        LL=0 # LEVEL
        PT=0 # HIT POINTS

        GE='unassigned good/evil' # GOOD/EVIL
        AL='unassigned alignment' # ALIGNMENT

        NA='unassigned name' # NAME
        SE='unassigned gender' # GENDER

        GC=0 # GOLD

    # Class methods
    def roll3d6(self):
        Z1 = random.randint(1, 6)
        Z2 = random.randint(1, 6)
        Z3 = random.randint(1, 6)
        ZZ = Z1+Z2+Z3
        return ZZ

    def writeline(self,line):
        LOG.append(line)
        print(LOG[len(LOG)-1])

    def strength(self,ST):
        if ST<3:
            SF=-3
        if ST>3 and ST<6:
            SF=-2
        if ST>5 and ST<9:
            SF=-1
        if ST>8 and ST<13:
            SF=0
        if ST>12 and ST<16:
            SF=1
        if ST>15 and ST<18:
            SF=2
        if ST==18:
            SF=3
 
        self.writeline(str(ST) + '\N{tab}- STRENGTH')
        self.writeline('\N{tab} * ADD ' + str(SF) + ' TO ROLLS TO HIT, DAMAGE, OPEN DOORS')

    def constitution(self,CO):
        self.writeline(str(CO) + '\N{tab}- CONSTITUTION')

    def intelligence(self,IN):
        self.writeline(str(IN) + '\N{tab}- INTELLIGENCE')

        # LITERACY MODIFIER
        if IN==3:
            self.writeline('\N{tab} * DIFFICULT SPEECH-ILLITERATE.')
        if IN>3 and IN<6:
            self.writeline('\N{tab} * EASY SPEECH BUT ILLITERATE')
        if IN>5 and IN<9:
            self.writeline('\N{tab} * BARELY LITERATE')
        if IN>8 and IN<13:
            self.writeline('\N{tab} * LITERATE IN NATIVE TONGUE')
        if IN>12 and IN<16:
            self.writeline('\N{tab} * LITERATE AND FLUENT IN 2 LANGUAGES')
        if IN>15 and IN<18:
            self.writeline('\N{tab} * LITERATE AND FLUENT IN 3 LANGUAGES')
        if IN==18:
            self.writeline('\N{tab} * LITERATE AND FLUENT IN 4 LANGUAGES')

        # MAGIC USER RESTRICTIONS
        if IN<9:
            self.writeline('\N{tab} * INTELLIGENCE TOO LOW FOR MAGIC USER')
        if IN==9:
            self.writeline('\N{tab} * 35% TO KNOW SPELL-MIN/MAX PER LVL:4/6')
        if IN>9 and IN<13:
            self.writeline('\N{tab} * 45% TO KNOW SPELL-MIN/MAX PER LVL:5/7')
        if IN>12 and IN<15:
            self.writeline('\N{tab} * 55% TO KNOW SPELL-MIN/MAX PER LVL:6/9')
        if IN>14 and IN<17:
            self.writeline('\N{tab} * 65% TO KNOW SPELL-MIN/MAX PER LVL:7/11')
        if IN==17:
            self.writeline('\N{tab} * 75% TO KNOW SPELL-MIN/MAX PER LVL:8/14')
        if IN==18:
            self.writeline('\N{tab} * 85% TO KNOW SPELL-MIN/MAX PER LVL:9/18')
        if IN==3:
            self.writeline('\N{tab} * INTELLIGENCE TOO LOW FOR MAGIC USER')

    def dexterity(self,DX):
        self.writeline(str(DX) + '\N{tab}- DEXTERITY')

        # DEXTERITY MODIFIER
        if DX==3:
            DF=-3
            self.writeline('\N{tab} * ADD 3 TO ARMOR CLASS')
            
        if DX>3 and DX<6:
            DF=-2
            self.writeline('\N{tab} * ADD 2 TO ARMOR CLASS')
            
        if DX>5 and DX<9:
            DF=-1
            self.writeline('\N{tab} * ADD 1 TO ARMOR CLASS')
            
        if DX>8 and DX<13:
            DF=0
        if DX>12 and DX<16:
            DF=1
            self.writeline('\N{tab} * SUBTRACT 1 FROM ARMOR CLASS.')
            
        if DX>15 and DX<18:
            DF=2
            self.writeline('\N{tab} * SUBTRACT 2 FROM ARMOR CLASS.')
            
        if DX==18:
            DF=3
            self.writeline('\N{tab} * SUBTRACT 3 FROM ARMOR CLASS.')
            
        self.writeline('\N{tab} * ADD '+ str(DF) + ' TO MISSLE FIRE ROLLS \'TO HIT\'')

    def wisdom(self,WI):
        self.writeline(str(WI) + '\N{tab}- WISDOM')

        # WISDOM MODIFIER
        if WI==3:
            WF=-3
        if WI>3 and WI<6:
            WF=-2
        if WI>5 and WI<9:
            WF=-1
        if WI>8 and WI<13:
            WF=0
        if WI>12 and WI<16:
            WF=1
        if WI>15 and WI<18:
            WF=2
        if WI==18:
            WF=3
        self.writeline('\N{tab} * ADD ' + str(WF) + ' TO MAGIC-BASED SAVING THROW')

    def charisma(self,CH):
        self.writeline(str(CH) + '\N{tab}- CHARISMA')

        # CHARISMA MODIFIER
        if CH==3:
            CF=1
        if CH>3 and CH<6:
            CF=2
        if CH>5 and CH<9:
            CF=3
        if CH>8 and CH<13:
            CF=4
        if CH>12 and CH<16:
            CF=5
        if CH>15 and CH<18:
            CF=6
        if CH==18:
            CF=7
        self.writeline('\N{tab} * CAN HAVE ' + str(CF) + ' RETAINER(S) WITH MORALE OF ' + str(CF))

    def raceclass(self,CN,any_PC):
        ACCEPTRACECLASS=True
        if CN==4:
            if any_PC.DX<9 or any_PC.CO<9:
                self.writeline('')
                self.writeline('DEXTERITY AND/OR CONSTITUTION')
                self.writeline('TOO LOW FOR HALFLING')
                ACCEPTRACECLASS=False
        if CN==5:
            if any_PC.IN<9:
                self.writeline('')
                self.writeline('INTELLIGENCE TOO LOW FOR ELF')
                ACCEPTRACECLASS=False
        if CN==6:
            if any_PC.CO<9:
                self.writeline('')
                self.writeline('CONSTITUTION TOO LOW FOR DWARF')
                ACCEPTRACECLASS=False
        return ACCEPTRACECLASS
    
    # HIT DICE ASSIGNED BY RACE/CLASS
    def hitdice(self,CN):
        if CN==1:
            HF=8
        if CN==2:
            HF=4
        if CN==3:
            HF=6
        if CN==4:
            HF=6
        if CN==5:
            HF=6
        if CN==6:
            HF=8
        if CN==7:
            HF=4
        return HF

    def chlevel(self,LL,CO,HF):
   
        # Constitution Factor
        if CO == 3:
            PF=-3
        if CO>3 and CO<6:
            PF=-2
        if CO>5 and CO<9:
            PF=-1
        if CO>8 and CO<13:
            PF=0
        if CO>12 and CO<16:
            PF=1
        if CO>15 and CO<18:
            PF=2
        if CO==18:
            PF=3

        #print('Constitution factor PF=',PF)
        self.writeline('-------------------------------------------------')
        chlevelstr = 'YOUR CHARACTER HAS ',LL,',',HF,'-SIDED HIT DICE'
        self.writeline(chlevelstr)
        PT = self.hitpts(HF,LL,PF)
        return PT
    
    def hitpts(self,HF,LL,PF):
        PT=LL # Initial hit points = level

        # HIT DICE AND CONSTITUTION ADJUSTMENTS
        if HF==4:
            for i in range(LL):
                PT = PT + random.randint(1,4) + PF
        elif HF==6:
            for i in range(LL):
                PT = PT + random.randint(1,6) + PF
        elif HF==8:
            for i in range(LL):
                PT = PT + random.randint(1,8) + PF
        hitptsstr = 'YOUR CHARACTER HAS ',PT,'HIT POINTS'
        self.writeline(hitptsstr)
        return PT
    
    def clericskills(self,LL):
        self.writeline('----------------------------------------')
        self.writeline('    CLERIC VS. UNDEAD TABLE (1D20)')
        self.writeline('SKEL\N{tab}ZOMB\N{tab}GHOU\N{tab}WIGT\N{tab}WRAI\N{tab}MUMM\N{tab}SPEC\N{tab}VAMP')
        Z1='7\N{tab}9\N{tab}11\N{tab}--\N{tab}--\N{tab}--\N{tab}--\N{tab}--'
        Z2='T\N{tab}7\N{tab}9\N{tab}11\N{tab}--\N{tab}--\N{tab}--\N{tab}--'
        Z3='T\N{tab}T\N{tab}7\N{tab}9\N{tab}11\N{tab}--\N{tab}--\N{tab}--'
        Z4='D\N{tab}T\N{tab}T\N{tab}7\N{tab}9\N{tab}11\N{tab}--\N{tab}--'
        Z5='D\N{tab}D\N{tab}T\N{tab}T\N{tab}7\N{tab}9\N{tab}11\N{tab}--'
        if LL==1:
            self.writeline(Z1)
        if LL==2:
            self.writeline(Z2)
        if LL==3:
            self.writeline(Z3)
        if LL==4:
            self.writeline(Z4)
        if LL==5:
            self.writeline(Z5)
    
    def thiefskills(self,LL):
        self.writeline('----------------------------------------')
        self.writeline('    THIEF\'S ABILITIES')
        self.writeline('PICK\N{tab}REMV\N{tab}PICK\N{tab}MOVE\N{tab}CLIM\N{tab}HIDE\N{tab}HEAR')
        self.writeline('LOCK\N{tab}TRAP\N{tab}PCKT\N{tab}SILT\N{tab}SURF\N{tab}SHDW\N{tab}NOISE')
        Z1='15%\N{tab}10%\N{tab}20%\N{tab}20%\N{tab}87%\N{tab}10%\N{tab}1-2'
        Z2='20%\N{tab}15%\N{tab}25%\N{tab}25%\N{tab}88%\N{tab}15%\N{tab}1-2'
        Z3='25%\N{tab}20%\N{tab}30%\N{tab}30%\N{tab}89%\N{tab}20%\N{tab}1-3'
        Z4='30%\N{tab}25%\N{tab}35%\N{tab}35%\N{tab}90%\N{tab}25%\N{tab}1-3'
        Z5='35%\N{tab}30%\N{tab}40%\N{tab}40%\N{tab}91%\N{tab}30%\N{tab}1-3'
        if LL==1:
            self.writeline(Z1)
        if LL==2:
            self.writeline(Z2)
        if LL==3:
            self.writeline(Z3)
        if LL==4:
            self.writeline(Z4)
        if LL==5:
            self.writeline(Z5)
    
    def savingthrowtab(self,):
        #print('----------------------------------------')
        #print('    SAVING THROW TABLE                  ')
        self.writeline('DEATH\N{tab}\N{tab}PARALYSIS\N{tab}\N{tab}RODS')
        self.writeline('RAY OR\N{tab}MAGIC\N{tab}OR TURN \N{tab}DRAGON\N{tab}STAVES')
        self.writeline('POISON\N{tab}WANDS\N{tab}TO STONE\N{tab}BREATH\N{tab}OR SPELLS')
        self.writeline('------\N{tab}-----\N{tab}--------\N{tab}------\N{tab}---------')
        #print(SR[1],'\N{tab}',SR[2],'\N{tab}',SR[3],'\N{tab}',SR[4],'\N{tab}',SR[5])
    
    def fightersave(self,LL):
        if LL<4:
            self.writeline('12\N{tab}13\N{tab}14\N{tab}\N{tab}15\N{tab}16')
        if LL >3 and LL<6:
            self.writeline('10\N{tab}11\N{tab}12\N{tab}\N{tab}13\N{tab}14')
        self.writeline('MAY WEAR ANY ARMOR AND USE SHIELD')
        self.writeline('MAY USE ANY WEAPON')
        self.writeline('NO SPELLS BUT MAY USE ANY MAGIC ARTICLE')
    
    def clericsave(self,LL):
        if LL<5:
            self.writeline('11\N{tab}12\N{tab}14\N{tab}\N{tab}16\N{tab}15')
        if LL==5:
            self.writeline('9\N{tab}10\N{tab}12\N{tab}\N{tab}14\N{tab}12')
        self.writeline('MAY WEAR ANY ARMOR AND USE SHIELD')
        self.writeline('MAY NOT USE EDGED WEAPONS')
        self.writeline('MAY USE SLING')
        self.writeline('HAS ABILITY TO TURN UNDEAD')
        self.writeline('USES CLERICAL SPELLS ONLY')
    
    def halflingsave(self,LL):
        if LL<4:
            self.writeline('8\N{tab}9\N{tab}10\N{tab}\N{tab}13\N{tab}12')
        if LL>3 and LL<6:
            self.writeline('6\N{tab}7\N{tab}8\N{tab}\N{tab}10\N{tab}10')
        self.writeline('CANNOT USE LONGBOW OR 2 HANDED SWORD')
        self.writeline('ADJUST MISSLE ATTACK TO HIT BY +1')
        self.writeline('ADJ AC BY -1 VS. MORE THAN MAN-SIZE OPP')
        self.writeline('ONLY 10% CHANCE OF DETECTION IN WOODS')
        self.writeline('REMAINS UNSEEN IN DUNGEON ON 1-2 (1D6)')
    
    def elfsave(self,LL):
        if LL<4:
            self.writeline('12\N{tab}13\N{tab}13\N{tab}\N{tab}15\N{tab}15')
        if LL>3 and LL<6:
            self.writeline('10\N{tab}11\N{tab}11\N{tab}\N{tab}13\N{tab}12')
        self.writeline('HAS 60\' INFRA-VISION')
        self.writeline('DETECTS OR SECRET DOORS ON 1-2(1D6)')
        self.writeline('IMMUNE TO PARALYSIS FROM GHOUL ATTACK')
        self.writeline('SPEAKS ELVISH, ORC, HOB-GOBLIN, AND GNOLL')
        self.writeline('MAY USE SPELLS AND MAGIC ARTICLES')
    
    def dwarfsave(self,LL):
        if LL<4:
            self.writeline('8\N{tab}9\N{tab}10\N{tab}\N{tab}13\N{tab}12')
        if LL>3 and LL<6:
            self.writeline('6\N{tab}7\N{tab}8\N{tab}\N{tab}10\N{tab}10')
        self.writeline('HAS 60\' INFRA-VISION')
        self.writeline('DETS\' TRAPS, DUNGEON ANOMALIES,@ 1-2(1D6)')
        self.writeline('SPEAKS DWARVISH, GNOME, KOBOLD, AND GOBLIN')
        self.writeline('MAY NOT USE LONGBOW OR 2 HANDED SWORD')
    
    def thiefsave(self,LL):
        if LL<5:
            self.writeline('13\N{tab}14\N{tab}13\N{tab}\N{tab}16\N{tab}15')
        if LL==5:
            self.writeline('12\N{tab}13\N{tab}11\N{tab}\N{tab}14\N{tab}13')
        self.writeline('LEATHER ARMOR ONLY-NO SHIELD')
        self.writeline('BACKSTABBING ADDS +4 TO \'TO HIT\' ROLL')
        self.writeline('BACKSTABBING DOES TWICE NORMAL DAMAGE')
        self.writeline('SEE TABLE FOR OTHER SKILLS')
    
    def magicusersave(self,LL):
        self.writeline('13\N{tab}14\N{tab}13\N{tab}\N{tab}16\N{tab}15')
        self.writeline('MAY NOT USE SHIELD OR WEAR ARMOR')
        self.writeline('MAY ONLY USE DAGGER AS A WEAPON')
        self.writeline('CHECK INTELLIGENCE FOR ABILITY TO')
        self.writeline('TO LEARN SPELLS AND # OF SPELLS/LEVEL')

def loadcharfile(any_PC):
    FN=0 # File number
    FI=[] # Filename list
    print('ENTER A NUMBER FROM THE CHARACTER FILENAME LIST:')

    for x in os.listdir():
        if x.endswith(".chf"):
            FN+=1 
            print(str(FN) + ') ' + x)
            FI.append(x)
    FN = input()
    FL=FI[int(FN)-1]
    with open(FL) as CHARFILE:
        data = CHARFILE.read()

    #print("Data type before reconstruction : ", type(data))
    # reconstructing the data as a dictionary
    chardict = json.loads(data)

    #print("Data type after reconstruction : ", type(chardict))
    #print(chardict)

    # Update the character instance
    any_PC.ST = chardict['ST'] 
    any_PC.CO = chardict['CO'] 
    any_PC.IN = chardict['IN'] 
    any_PC.WI = chardict['WI'] 
    any_PC.CH = chardict['CH'] 

    any_PC.CN = chardict['CN']  
    any_PC.HF = chardict['HF']  
    any_PC.LL = chardict['LL']  

    any_PC.NA = chardict['NA']  
    any_PC.GE = chardict['GE']  
    any_PC.AL = chardict['AL']  

    any_PC.GC = chardict['GC']  

def charsheet(any_PC):
    print('----------------------------------------')
    print('\N{tab}  DUNGEONS & DRAGONS             ')
    print('\N{tab}Character Record Sheet           ')
    print('')
    print('Character Name \N{tab}',any_PC.NA)
    print('Gold           \N{tab}',any_PC.GC)
    print('Alignment      \N{tab}',ALT[any_PC.AL],GET[any_PC.GE])
    print('Class/Race     \N{tab}',RC[any_PC.CN])
    print('Level          \N{tab}',any_PC.LL)
    print('HIT POINTS     \N{tab}',any_PC.PT)
    print('HIT DICE       \N{tab}','1d',any_PC.HF)
    print('----------------------------------------')
    print('\N{tab}ABILITIES                        ')
    any_PC.ST
    any_PC.CO
    any_PC.DX
    any_PC.IN
    any_PC.WI
    any_PC.CH
    print('----------------------------------------')
    print('\N{tab}SAVING THROWS & SPECIAL ABILITIES')
    any_PC.savingthrowtab()
    if any_PC.CN==1:
        any_PC.fightersave(any_PC.LL)
    if any_PC.CN==2:
        any_PC.magicusersave(any_PC.LL)
    if any_PC.CN==3:
        any_PC.clericsave(any_PC.LL)
    if any_PC.CN==4:
        any_PC.halflingsave(any_PC.LL)
    if any_PC.CN==5:
        any_PC.elfsave(any_PC.LL)
    if any_PC.CN==6:
        any_PC.dwarfsave(any_PC.LL)
    if any_PC.CN==7:
        any_PC.thiefsave(any_PC.LL)
    print('----------------------------------------')
    print('----------------------------------------')

def storeAbilities(any_PC):
    # STORE ABILITIES AS A DICTIONARY
    chardict = {}
    chardict['ST'] = any_PC.ST
    chardict['CO'] = any_PC.CO
    chardict['IN'] = any_PC.IN
    chardict['WI'] = any_PC.WI
    chardict['CH'] = any_PC.CH

    chardict['CN'] = any_PC.CN # Class/Race
    chardict['HF'] = any_PC.HF # Hit Dice
    chardict['LL'] = any_PC.LL # Level

    chardict['NA'] = any_PC.NA # Name
    chardict['GE'] = any_PC.GE # Good/Evil
    chardict['AL'] = any_PC.AL # Alignment

    chardict['GC'] = any_PC.GC # Gold

    with open(f'{any_PC.NA}.chf', 'w') as convert_file:
        convert_file.write(json.dumps(chardict))

def writelog(LOG,fout):
    for LINE in LOG:
        fout.write(str(LINE)+'\n')

"""
ddcrt.py main()

"""
def main():

    # Create a character object instance based on the base class Character 
    my_PC = Character() 
    # Create a wizard object instance based on the base class Wizard 
    my_WIZ = Wizard()
    my_WIZ.welcomeScreen(my_PC)     # Display artwork and title screen

    ACTIVESESSION=True
    while ACTIVESESSION!=False:

        fout = open('ddcrtlog.txt', 'w')
        AC = my_WIZ.actionScreen(my_PC)     # Prompt for action
        if AC == 0:        
            ACTIVESESSION=False
        elif AC == 1:
            my_WIZ.loadScreen(my_PC)
            charsheet(my_PC)                # SUMMARIZE WITH A FORMATTED CHARACTER SHEET
            writelog(LOG,fout)              # WRITE SESSION LOG TO ddcrtlog.txt
            fout.close()
        elif AC == 2:
            my_WIZ.genabsScreen(my_PC)      # Generate and assign abilities to character instance
            my_WIZ.raceclassScreen(my_PC)   # Prompt for race/class and hit dice to character instance
            my_WIZ.levelScreen(my_PC)       # Prompt for level and assign hit points to character instance
            my_WIZ.behavScreen(my_PC)       # Prompt for behavior and assign to character instance
            my_WIZ.alignScreen(my_PC)       # Prompt for alignment and assign to character instance
            my_PC.writeline('-------------------------------------------------')
            NA=input('WHAT IS CHARACTER\'S NAME: ')
            # Assign character name to character instance
            my_PC.NA = NA
            SE=input('WHAT IS CHARACTER\'S GENDER: ')
            my_PC.SE = SE

            MT=my_PC.roll3d6() + 3           # CALCULATE CHARACTER'S GOLD
            GC=10*MT
            my_PC.GC = GC

            charsheet(my_PC)                 # SUMMARIZE WITH A FORMATTED CHARACTER SHEET
            writelog(LOG,fout)               # WRITE SESSION LOG TO ddcrtlog.txt
            fout.close()
            storeAbilities(my_PC)            # Write abilities as a JSON file
        elif AC == 3:
            print('Edit Character Feature Not implemented ')
        else:
            print('Unknown Action')

if __name__ == "__main__":
    main()
