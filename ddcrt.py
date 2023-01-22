"""
    *************************************************************************
    *                                                                       *
    *                   DUNGEON MASTER'S PERSONNEL SERVICE                  *
    *                 (40 COLUMN BY 16 LINE CRT DISPLAY ONLY )              *
    *                   SAVE AS "ddcrt.py" - VERSION 1.0                    *
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
"""

import csv
import random
L=0 # ABILITY COUNTER (STRENGTH, CONSTITUTION, AND SO ON.)
ST=0 # STRENGTH
CO=0 # CONSTITUTION
IN=0 # INTELLIGENCE
DX=0 # DEXTERITY
WI=0 # WISDOM
CH=0 # CHARISMA

AB=['unused','STRENGTH','CONSTITUTION','INTELLIGENCE','DEXTERITY','WISDOM','CHARISMA']
RC=['unused','FIGHTER','MAGIC USER','CLERIC','HALFLING','ELF','DWARF','THIEF']
SR=['unused','POISON or DEATH RAY','MAGIC WAND','TURN TO STONE or PARALYSIS','DRAGON BREATH','SPELLS or MAGIC STAFF']
ALT=['unused','LAWFUL','NEUTRAL','CHAOTIC']
GET=['unused','GOOD','EVIL']

def roll3d6():
    Z1=random.randint(1, 6)
    Z2=random.randint(1, 6)
    Z3=random.randint(1, 6)
    ZZ=Z1+Z2+Z3
    return ZZ

def strength(ST):
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
    LOG.append(str(ST) + '\N{tab}- STRENGTH')
    print(LOG[len(LOG)-1])
    LOG.append('\N{tab} * ADD ' + str(SF) + ' TO ROLLS TO HIT, DAMAGE, OPEN DOORS')
    print(LOG[len(LOG)-1])

def constitution(CO):
    LOG.append(str(CO) + '\N{tab}- CONSTITUTION')
    print(LOG[len(LOG)-1])

def intelligence(IN):
    LOG.append(str(IN) + '\N{tab}- INTELLIGENCE')
    print(LOG[len(LOG)-1])

    # LITERACY MODIFIER
    if IN==3:
        LOG.append('\N{tab} * DIFFICULT SPEECH-ILLITERATE.')
    if IN>3 and IN<6:
        LOG.append('\N{tab} * EASY SPEECH BUT ILLITERATE')
    if IN>5 and IN<9:
        LOG.append('\N{tab} * BARELY LITERATE')
    if IN>8 and IN<13:
        LOG.append('\N{tab} * LITERATE IN NATIVE TONGUE')
    if IN>12 and IN<16:
        LOG.append('\N{tab} * LITERATE AND FLUENT IN 2 LANGUAGES')
    if IN>15 and IN<18:
        LOG.append('\N{tab} * LITERATE AND FLUENT IN 3 LANGUAGES')
    if IN==18:
        LOG.append('\N{tab} * LITERATE AND FLUENT IN 4 LANGUAGES')
    print(LOG[len(LOG)-1])

    # MAGIC USER RESTRICTIONS
    if IN<9:
        LOG.append('\N{tab} * INTELLIGENCE TOO LOW FOR MAGIC USER')
    if IN==9:
        LOG.append('\N{tab} * 35% TO KNOW SPELL-MIN/MAX PER LVL:4/6')
    if IN>9 and IN<13:
        LOG.append('\N{tab} * 45% TO KNOW SPELL-MIN/MAX PER LVL:5/7')
    if IN>12 and IN<15:
        LOG.append('\N{tab} * 55% TO KNOW SPELL-MIN/MAX PER LVL:6/9')
    if IN>14 and IN<17:
        LOG.append('\N{tab} * 65% TO KNOW SPELL-MIN/MAX PER LVL:7/11')
    if IN==17:
        LOG.append('\N{tab} * 75% TO KNOW SPELL-MIN/MAX PER LVL:8/14')
    if IN==18:
        LOG.append('\N{tab} * 85% TO KNOW SPELL-MIN/MAX PER LVL:9/18')
    if IN==3:
        LOG.append('\N{tab} * INTELLIGENCE TOO LOW FOR MAGIC USER')
    print(LOG[len(LOG)-1])

def dexterity(DX):
    LOG.append(str(DX) + '\N{tab}- DEXTERITY')
    print(LOG[len(LOG)-1])

    # DEXTERITY MODIFIER
    if DX==3:
        DF=-3
        LOG.append('\N{tab} * ADD 3 TO ARMOR CLASS')
        print(LOG[len(LOG)-1])
    if DX>3 and DX<6:
        DF=-2
        LOG.append('\N{tab} * ADD 2 TO ARMOR CLASS')
        print(LOG[len(LOG)-1])
    if DX>5 and DX<9:
        DF=-1
        LOG.append('\N{tab} * ADD 1 TO ARMOR CLASS')
        print(LOG[len(LOG)-1])
    if DX>8 and DX<13:
        DF=0
    if DX>12 and DX<16:
        DF=1
        LOG.append('\N{tab} * SUBTRACT 1 FROM ARMOR CLASS.')
        print(LOG[len(LOG)-1])
    if DX>15 and DX<18:
        DF=2
        LOG.append('\N{tab} * SUBTRACT 2 FROM ARMOR CLASS.')
        print(LOG[len(LOG)-1])
    if DX==18:
        DF=3
        LOG.append('\N{tab} * SUBTRACT 3 FROM ARMOR CLASS.')
        print(LOG[len(LOG)-1])
    LOG.append('\N{tab} * ADD'+ str(DF) + 'TO MISSLE FIRE ROLLS \'TO HIT\'')
    print(LOG[len(LOG)-1])

def wisdom(WI):
    LOG.append(str(WI) + '\N{tab}- WISDOM')
    print(LOG[len(LOG)-1])

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
    LOG.append('\N{tab} * ADD' + str(WF) + 'TO MAGIC-BASED SAVING THROW')
    print(LOG[len(LOG)-1])

def charisma(CH):
    LOG.append(str(CH) + '\N{tab}- CHARISMA')
    print(LOG[len(LOG)-1])

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
    LOG.append('\N{tab} * CAN HAVE' + str(CF) + 'RETAINER(S) WITH MORALE OF' + str(CF))
    print(LOG[len(LOG)-1])

def raceclass(CN,DX,CO,IN):
    ACCEPTRACECLASS=True
    if CN==4:
        if DX<9 or CO<9:
            print('')
            print('DEXTERITY AND/OR CONSTITUTION')
            print('TOO LOW FOR HALFLING')
            ACCEPTRACECLASS=False
    if CN==5:
        if IN<9:
            print('')
            print('INTELLIGENCE TOO LOW FOR ELF')
            ACCEPTRACECLASS=False
    if CN==6:
        if CO<9:
            print('')
            print('CONSTITUTION TOO LOW FOR DWARF')
            ACCEPTRACECLASS=False
    return ACCEPTRACECLASS

def chlevel():
    ACCEPTLVL=True
    if LL>5:
        print('NUMBER TOO LARGE: RE-ENTER')
        ACCEPTRACECLASS=False

    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    print('YOUR CHARACTER HAS',LL,', ',HF,'-SIDED HIT DICE')
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
    PT = hitpts(HF,LL,PF)
    return (ACCEPTLVL, PT)

def hitpts(HF,LL,PF):
    PT=LL
    if HF==4:
        for i in range(LL):
            PT=PT + random.randint(1, 4) + PF
    elif HF==6:
        for i in range(LL):
            PT=PT + random.randint(1, 6) + PF
    elif HF==8:
        for i in range(LL):
            PT=PT + random.randint(1, 8) + PF
    print('YOUR CHARACTER WOULD HAVE',PT,'HIT POINTS')
    return PT

def clericskills(LL):
    print('----------------------------------------')
    print('    CLERIC VS. UNDEAD TABLE (1D20)')
    print('SKEL\N{tab}ZOMB\N{tab}GHOU\N{tab}WIGT\N{tab}WRAI\N{tab}MUMM\N{tab}SPEC\N{tab}VAMP')
    Z1='7\N{tab}9\N{tab}11\N{tab}--\N{tab}--\N{tab}--\N{tab}--\N{tab}--'
    Z2='T\N{tab}7\N{tab}9\N{tab}11\N{tab}--\N{tab}--\N{tab}--\N{tab}--'
    Z3='T\N{tab}T\N{tab}7\N{tab}9\N{tab}11\N{tab}--\N{tab}--\N{tab}--'
    Z4='D\N{tab}T\N{tab}T\N{tab}7\N{tab}9\N{tab}11\N{tab}--\N{tab}--'
    Z5='D\N{tab}D\N{tab}T\N{tab}T\N{tab}7\N{tab}9\N{tab}11\N{tab}--'
    if LL==1:
        print(Z1)
    if LL==2:
        print(Z2)
    if LL==3:
        print(Z3)
    if LL==4:
        print(Z4)
    if LL==5:
        print(Z5)

def thiefskills(LL):
    print('----------------------------------------')
    print('    THIEF\'S ABILITIES')
    print('PICK\N{tab}REMV\N{tab}PICK\N{tab}MOVE\N{tab}CLIM\N{tab}HIDE\N{tab}HEAR')
    print('LOCK\N{tab}TRAP\N{tab}PCKT\N{tab}SILT\N{tab}SURF\N{tab}SHDW\N{tab}NOISE')
    Z1='15%\N{tab}10%\N{tab}20%\N{tab}20%\N{tab}87%\N{tab}10%\N{tab}1-2'
    Z2='20%\N{tab}15%\N{tab}25%\N{tab}25%\N{tab}88%\N{tab}15%\N{tab}1-2'
    Z3='25%\N{tab}20%\N{tab}30%\N{tab}30%\N{tab}89%\N{tab}20%\N{tab}1-3'
    Z4='30%\N{tab}25%\N{tab}35%\N{tab}35%\N{tab}90%\N{tab}25%\N{tab}1-3'
    Z5='35%\N{tab}30%\N{tab}40%\N{tab}40%\N{tab}91%\N{tab}30%\N{tab}1-3'
    if LL==1:
        print(Z1)
    if LL==2:
        print(Z2)
    if LL==3:
        print(Z3)
    if LL==4:
        print(Z4)
    if LL==5:
        print(Z5)

def savingthrowtab():
    #print('----------------------------------------')
    #print('    SAVING THROW TABLE                  ')
    print('DEATH\N{tab}\N{tab}PARALYSIS\N{tab}\N{tab}RODS')
    print('RAY OR\N{tab}MAGIC\N{tab}OR TURN \N{tab}DRAGON\N{tab}STAVES')
    print('POISON\N{tab}WANDS\N{tab}TO STONE\N{tab}BREATH\N{tab}OR SPELLS')
    print('------\N{tab}-----\N{tab}--------\N{tab}------\N{tab}---------')
    #print(SR[1],'\N{tab}',SR[2],'\N{tab}',SR[3],'\N{tab}',SR[4],'\N{tab}',SR[5])

def fightersave(LL):
    if LL<4:
        print('12\N{tab}13\N{tab}14\N{tab}\N{tab}15\N{tab}16')
    if LL >3 and LL<6:
        print('10\N{tab}11\N{tab}12\N{tab}\N{tab}13\N{tab}14')
    print('MAY WEAR ANY ARMOR AND USE SHIELD')
    print('MAY USE ANY WEAPON')
    print('NO SPELLS BUT MAY USE ANY MAGIC ARTICLE')

def clericsave(LL):
    if LL<5:
        print('11\N{tab}12\N{tab}14\N{tab}\N{tab}16\N{tab}15')
    if LL==5:
        print('9\N{tab}10\N{tab}12\N{tab}\N{tab}14\N{tab}12')
    print('MAY WEAR ANY ARMOR AND USE SHIELD')
    print('MAY NOT USE EDGED WEAPONS')
    print('MAY USE SLING')
    print('HAS ABILITY TO TURN UNDEAD')
    print('USES CLERICAL SPELLS ONLY')

def halflingsave(LL):
    if LL<4:
        print('8\N{tab}9\N{tab}10\N{tab}\N{tab}13\N{tab}12')
    if LL>3 and LL<6:
        print('6\N{tab}7\N{tab}8\N{tab}\N{tab}10\N{tab}10')
    print('CANNOT USE LONGBOW OR 2 HANDED SWORD')
    print('ADJUST MISSLE ATTACK TO HIT BY +1')
    print('ADJ AC BY -1 VS. MORE THAN MAN-SIZE OPP')
    print('ONLY 10% CHANCE OF DETECTION IN WOODS')
    print('REMAINS UNSEEN IN DUNGEON ON 1-2 (1D6)')

def elfsave(LL):
    if LL<4:
        print('12\N{tab}13\N{tab}13\N{tab}\N{tab}15\N{tab}15')
    if LL>3 and LL<6:
        print('10\N{tab}11\N{tab}11\N{tab}\N{tab}13\N{tab}12')
    print('HAS 60\' INFRA-VISION')
    print('DETECTS OR SECRET DOORS ON 1-2(1D6)')
    print('IMMUNE TO PARALYSIS FROM GHOUL ATTACK')
    print('SPEAKS ELVISH, ORC, HOB-GOBLIN, AND GNOLL')
    print('MAY USE SPELLS AND MAGIC ARTICLES')

def dwarfsave(LL):
    if LL<4:
        print('8\N{tab}9\N{tab}10\N{tab}\N{tab}13\N{tab}12')
    if LL>3 and LL<6:
        print('6\N{tab}7\N{tab}8\N{tab}\N{tab}10\N{tab}10')
    print('HAS 60\' INFRA-VISION')
    print('DETS\' TRAPS, DUNGEON ANOMALIES,@ 1-2(1D6)')
    print('SPEAKS DWARVISH, GNOME, KOBOLD, AND GOBLIN')
    print('MAY NOT USE LONGBOW OR 2 HANDED SWORD')

def thiefsave(LL):
    if LL<5:
        print('13\N{tab}14\N{tab}13\N{tab}\N{tab}16\N{tab}15')
    if LL==5:
        print('12\N{tab}13\N{tab}11\N{tab}\N{tab}14\N{tab}13')
    print('LEATHER ARMOR ONLY-NO SHIELD')
    print('BACKSTABBING ADDS +4 TO \'TO HIT\' ROLL')
    print('BACKSTABBING DOES TWICE NORMAL DAMAGE')
    print('SEE TABLE FOR OTHER SKILLS')

def magicusersave(LL):
    print('13\N{tab}14\N{tab}13\N{tab}\N{tab}16\N{tab}15')
    print('MAY NOT USE SHIELD OR WEAR ARMOR')
    print('MAY ONLY USE DAGGER AS A WEAPON')
    print('CHECK INTELLIGENCE FOR ABILITY TO')
    print('TO LEARN SPELLS AND # OF SPELLS/LEVEL')

def charsheet():
    print('----------------------------------------')
    print('\N{tab}  DUNGEONS & DRAGONS             ')
    print('\N{tab}Character Record Sheet           ')
    print('')
    print('Character Name \N{tab}',NA)
    print('Gold           \N{tab}',GC)
    print('Alignment      \N{tab}',ALT[AL],GET[GE])
    print('Class/Race     \N{tab}',RC[CN])
    print('Level          \N{tab}',LL)
    print('HIT POINTS     \N{tab}',PT)
    print('HIT DICE       \N{tab}','1d',HF)
    print('----------------------------------------')
    print('\N{tab}ABILITIES                        ')
    strength(ST)
    constitution(CO)
    dexterity(DX)
    intelligence(IN)
    wisdom(WI)
    charisma(CH)
    print('----------------------------------------')
    print('\N{tab}SAVING THROWS & SPECIAL ABILITIES')
    savingthrowtab()
    if CN==1:
        fightersave(LL)
    if CN==2:
        magicusersave(LL)
    if CN==3:
        clericsave(LL)
    if CN==4:
        halflingsave(LL)
    if CN==5:
        elfsave(LL)
    if CN==6:
        dwarfsave(LL)
    if CN==7:
        thiefsave(LL)
    print('----------------------------------------')
    print('----------------------------------------')

def writelog(LOG):
    for LINE in LOG:
        fout.write(LINE+'\n')

    with open(NA+'.csv', mode='w') as char_file:
    char_writer = csv.writer(char_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    char_writer.writerow(['John Smith', 'Accounting', 'November'])
    char_writer.writerow(['Erica Meyers', 'IT', 'March'])

# -----------------------------------------------
fout = open('ddcrtlog.txt', 'w')


ACCEPTABILITIES=False
while ACCEPTABILITIES!=True:
    LOG=[]
    LOG.append('             \                  /               ')
    LOG.append('    _________))                ((_________      ')
    LOG.append('   /.-------./\    \    /    //\.-------.\\     ')
    LOG.append('  //#######//##\   ))  ((   //##))#######\\\    ')
    LOG.append(' //#######//###(( ((    ))  ))###\\\########\\\ ')
    LOG.append('((#######((#####\  \\\  //  //#####))########)) ')
    LOG.append(' \##   ###\######\   \)(/  //#####/###`    ##/  ')
    LOG.append('  )      #)    ###\->oo<- /##      (#       (   ')
    LOG.append('         (         \`..` /          )           ')
    LOG.append('                    \\""(                       ')
    LOG.append('                     - )                        ')
    LOG.append('                     / /                        ')
    LOG.append('                    ( /\                        ')
    LOG.append('                    /\| \                       ')
    LOG.append('                   (  \                         ')
    LOG.append('                       )                        ')
    LOG.append('                      /                         ')
    LOG.append('                     (                          ')
    LOG.append('                     `~                         ')

    LOG.append('')
    LOG.append('-------------------------------------------------')
    LOG.append('            DM\'S PERSONNEL SERVICE              ')
    LOG.append('                 Version 1.0                     ')
    LOG.append('')
    LOG.append('        PRODUCES CHAR. ABILITY SCORES            ')
    LOG.append('                     FOR                         ')
    LOG.append('             DUNGEONS & DRAGONS Tm               ')
    LOG.append('          3RD EDITION, DECEMBER 1979             ')
    LOG.append('             AKA THE \'BLUE BOOK\'               ')
    LOG.append('')
    LOG.append('       BY GARY GYGAX AND DAVE ARNESON            ')
    LOG.append('            EDITED BY ERIC HOLMES                ')
    LOG.append('')
    LOG.append('        Dragon ASCII Art by Ed Zahurak           ')
    LOG.append('-------------------------------------------------')

    for LINE in LOG:
        print(LINE)

    """
     GENERATE RANDOM VALUES FOR CHARACTER ABILITIES
    """

    # STRENGTH & CONSTITUTION RATIO CHECK
    A=0
    while A<0.67 or A>1.5:
        ST=roll3d6()
        CO=roll3d6()
        A=ST/CO
    strength(ST)
    constitution(CO)
    DX=roll3d6()
    dexterity(DX)

    # INTELLIGENCE & WISDOM RATIO CHECK
    B=0
    while B<0.67 or B>1.5:
        IN=roll3d6()
        WI=roll3d6()
        B=IN/WI
    intelligence(IN)
    wisdom(WI)
    CH=roll3d6()
    charisma(CH)
    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    LOG.append('PRESS Y TO ACCEPT CHARACTER ABILITIES')
    print(LOG[len(LOG)-1])
    LOG.append('OR ANY OTHER KEY TO RETRY: ')
    print(LOG[len(LOG)-1])
    C = input()
    LOG.append(C)
    print(LOG[len(LOG)-1])

    if C=='Y':
        ACCEPTABILITIES=True

# RACE/CLASS SELECTION & CHECKING
ACCEPTRACECLASS=False
while ACCEPTRACECLASS!=True:
    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    print('          CLASS/RACE LIST               ')
    print('  (1) FIGHTER          (4) HALFLING     ')
    print('  (2) MAGIC USER       (5) ELF          ')
    print('  (3) CLERIC           (6) DWARF        ')
    print('            (7) THIEF                   ')
    print('')
    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    print('SELECT THE RACE/CLASS THAT YOU WISH')
    print('YOUR CHARACTER TO HAVE AND ENTER THE')
    CN=int(input('NUMBER FROM THE TABLE ABOVE:'))
    #print(CN,DX,CO,IN)
    ACCEPTRACECLASS=raceclass(CN,DX,CO,IN)
    #print('ACCEPTRACECLASS=',ACCEPTRACECLASS)

    # HIT DICE ASSIGNED BY RACE/CLASS
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

# CHARACTER LEVEL ASSIGNED AND
# HIT POINTS CALCULATED
ACCEPTLVL=False
while ACCEPTLVL!=True:
    print('CHARACTER LEVEL RANGE..ONE (1) TO FIVE (5)')
    try:
        LL=int(input('AT WHICH LEVEL WITH CHARACTER START:'))
    except:
        print('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 5')
    ACCEPTLVL, PT = chlevel()

# CLERIC SKILLS ASSIGNED BY LEVEL
if CN==3:
    clericskills(LL)

# THIEF'S SKILLS ASSIGNED BY LEVEL
if CN==7:
    thiefskills(LL)

# OTHER CHARACTER DATA IS INPUT
LOG.append('-------------------------------------------------')
print(LOG[len(LOG)-1])
NA=input('WHAT IS CHARACTER\'S NAME: ')

ACCEPTALGN=False
while ACCEPTALGN!=True:
    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    print('CHARACTER CODE OF BEHAVIOR LIST ')
    print('  (1) GOOD     ')
    print('  (2) EVIL    ')
    print('')
    print('SELECT THE CODE THAT YOU WISH')
    print('YOUR CHARACTER TO HAVE AND ENTER THE')
    print('CHARACTER CODE RANGE..ONE (1) TO TWO (2)')
    try:
        GE=int(input('NUMBER FROM THE TABLE ABOVE:'))
    except:
        print('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 2')
        ACCEPTALGN = False
    if GE < 1 or GE > 2:
        print('ERROR: INVALID RANGE, TYPE A VALUE FROM 1 TO 2')
        ACCEPTALGN = False

    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    print('CHARACTER ALIGNMENT LIST ')
    print('  (1) LAWFUL     ')
    print('  (2) NEUTRAL    ')
    print('  (3) CHAOTIC    ')
    print('')
    LOG.append('-------------------------------------------------')
    print(LOG[len(LOG)-1])
    print('SELECT THE ALIGNMENT THAT YOU WISH')
    print('YOUR CHARACTER TO HAVE AND ENTER THE')
    print('CHARACTER ALIGNMENT RANGE..ONE (1) TO THREE (3)')
    try:
        AL=int(input('NUMBER FROM THE TABLE ABOVE:'))
    except:
        print('ERROR: INVALID INPUT, TYPE A VALUE FROM 1 TO 3')
        ACCEPTALGN = False
    if AL < 1 or AL > 3:
        print('ERROR: INVALID RANGE, TYPE A VALUE FROM 1 TO 3')
        ACCEPTALGN = False
    else:
        ACCEPTALGN = True

#RA=input('WHAT IS CHARACTER\'S RACE: ')
#SE=input('WHAT IS CHARACTER\'S GENDER: ')
#CL=input('WHAT IS CHARACTER\'S CLASS: ')

# CHARACTER'S GOLD IS CALCULATED
MT=roll3d6()+3
GC=10*MT

# SEPARATION BY RACE/CLASS FOR
# FINAL DATA CALCULATIONS
"""
savingthrowtab()
if CN==1:
    fightersave(LL)
if CN==2:
    magicusersave(LL)
if CN==3:
    clericsave(LL)
if CN==4:
    halflingsave(LL)
if CN==5:
    elfsave(LL)
if CN==6:
    dwarfsave(LL)
if CN==7:
    thiefsave(LL)
"""
charsheet()

writelog(LOG)
fout.close()
