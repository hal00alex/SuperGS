#GS for Super Villains and Super Heroes
#Varaition of Problem 1.4 from Algorithm Design by Jon Kleinberg

def main():
    #set up heroes and villians 
    super_heroes = ["Atom", "Arrow", "Flash", "Supergirl"]
    super_villains = ["Chronos", "Cupid", "Reverse Flash", "Astra In-Ze"]

    #set up preferences
    heroes_pref = {"Atom" : ["Chronos", "Cupid", "Reverse Flash", "Astra In-Ze"], "Arrow" : ["Cupid", "Reverse Flash", "Chronos", "Astra In-Ze"], "Flash" : ["Reverse Flash", "Cupid", "Chronos", "Astr In-Ze"], "Supergirl": ["Astra In-Ze", "Reverse Flash", "Chronos", "Cupid"]}
    villains_pref = {"Chronos": ["Atom" , "Arrow", "Flash", "Supergirl"], "Cupid": ["Arrow", "Atom", "Flash", "Supergirl"], "Reverse Flash" : ["Flash", "Arrow", "Atom", "Supergirl"], "Astra In-Ze": ["Flash", "Supergirl", "Arrow", "Atom"]}

    #Set up empty matching
    #first array is heores, second array is villains
    #same index is the matching/pair 
    matching = [[0,0,0,0], [0,0,0,0]]
    num_matching = []

    heroes_history = {"Atom" : [], "Arrow": [], "Flash": [], "Supergirl": []}
    villains_history = {"Chronos" : [], "Cupid": [], "Reverse Flash": [], "Astra In-Ze": []}

    #while someone is not in battle 
    while (len(num_matching) < 4):

        #go through heroes list
        for i in range (len(super_heroes)):

            #see if hero is battle
            if (super_heroes[i] not in num_matching):

                #go through preferences and history
                for j in range (len(super_villains)):
                    vill = heroes_pref[super_heroes[i]][j]

                    #skip any villian that was already asked
                    if (vill in heroes_history[super_heroes[i]]):
                        continue
                                    
                    #they get paired if villain is not in matching
                    if (vill not in matching):
                        matching[0][i] = super_heroes[i]
                        matching[1][i] = vill
                        num_matching.append(super_heroes[i])
                        #print (matching)
                        break

                    #if in matching check villain preferences
                    else:
                        #if villain prefers hero, remove person from matches
                        pref_list = villains_pref[vill]
                        #print (pref_list) 
                        #if villain does not refer hero, keep looking 

    print (matching)                     
                    
                    #if in matching check villain preferences 
    # syntax note: print(heroes_pref["Supergirl"][0]) 

main()

#Show that there is always a perfect matching of super villains to super heroes
#The set of engaged pairs always forms a matching. Let us suppose that the algortih terminates a free hero h.
#At termination, it must be the case that m had already asked every villain, for otherwise the While loop would have not exited.
#But this contradicts that there cannot be a free hero that asked ever villain to battle.


