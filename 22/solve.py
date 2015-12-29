#!/usr/bin/env python
import random 

class Wizard(object):

    def __init__(self):
        ''' '''

        self.HP = 50
        self.MP = 500
        self.armor = 0
        self.mana_spent = 0
        self.recharge = 0
        self.shield = 0
        self.actions_taken = []

class Boss(object):

    def __init__(self):
        ''' '''
        self.HP = 71
        self.attack = 10
        self.poison = 0


if __name__ == "__main__":
    
    print "..................................\
           \n..................................\
           \n...Welcome to wizardfighter 1.0...\n"
    print "...The fight is about to start...\n"

    wizard = Wizard()
    boss = Boss()

    options = {"1" : "Magic Missile",
               "2" : "Drain",
               "3" : "Shield",
               "4" : "Poison",
               "5" : "Recharge"}

    turn = "wizard"

    while wizard.HP > 0 and boss.HP > 0:

        actions = ["Magic Missile", "Drain"]

        # Evaluate effects
        if boss.poison:
            boss.HP -= 3
            if boss.HP <= 0:
                print "...Boss is dead..."
            boss.poison -= 1

        if wizard.recharge:
            wizard.MP += 101
            wizard.recharge -= 1

        if wizard.shield:
            wizard.armor = 7
        else:
            wizard.armor = 0

        # add actions that can take place
        if not boss.poison:
            actions.append("Poison")
        if not wizard.shield:
            actions.append("Shield")
        if not wizard.recharge:
            actions.append("Recharge")

        if turn == "wizard":

            if wizard.MP < 53:
                print "...Cant cast any spells... You are dead..."
            #action = random.choice(actions)
            message = "...Decide your action:... \ 
                       \n... 1 = Magic Missile ... \
                       \n... 2 = Drain ... \
                       \n... 3 = Shield ... \
                       \n... 4 = Poison ... \
                       \n... 5 = Recharge ..."
            action = options[str(input(message))]
            #print actions,action
            if action == "Magic Missile":
                boss.HP -= 4
                wizard.MP -= 53
                wizard.mana_spent += 53
            if action == "Drain":
                boss.HP -= 2
                wizard.HP += 2
                wizard.MP -= 73
                wizard.mana_spent += 73
            if action == "Shield":
                wizard.shield = 7
                wizard.MP -= 113
                wizard.mana_spent += 113
            if action == "Poison":
                boss.poison = 6
                wizard.MP -= 173
                wizard.mana_spent += 173
            if action == "Recharge":
                wizard.recharge = 6
                wizard.MP -= 229
                wizard.mana_spent += 229

            turn = "boss"
            wizard.actions_taken.append(action)

        elif turn == "boss":
            dmg = max(boss.attack - wizard.armor, 1)
            wizard.HP -= dmg
            turn = "wizard"
       
        if wizard.shield:
            wizard.shield -= 1
        
        if wizard.HP <= 0:
            print "...Wizard is dead..."
        if boss.HP <= 0:
            print "...Boss is dead..."
    






