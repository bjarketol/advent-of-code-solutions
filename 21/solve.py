#!/usr/bin/env python
import random

class Player(object):
    
    def __init__(self, player = None):
        ''' '''

        self.name = None
        self.HP = 100
        self.armor = None
        self.weapon = None
        self.rings = []
        self.gold_spent = 0
        self.defense = 0
        self.attack = 0
        
    def buy_weapon(self, weapon):
        '''     '''
        weapons = {"Dagger" : 8,
                   "Shortsword" : 10,
                   "Warhammer" : 25,
                   "Longsword" : 40,
                   "Greataxe" : 74}

        self.gold_spent += weapons[weapon]
        self.weapon = weapon
        self.__update_stats()
        return self

    def buy_armor(self, armor):
        ''' '''
        if armor:
            armors = {"Leather" : 13,
                      "Chainmail" : 31,
                      "Splintmail" : 53,
                      "Bandedmail" : 75,
                      "Platemail" : 102}

            self.gold_spent += armors[armor]
            self.armor = armor
            self.__update_stats()
        return self
    
    def buy_ring(self, ring):
        ''' '''
        if ring:
            rings = {"Damage +1" : 25,
                     "Damage +2" : 50,
                     "Damage +3" : 100,
                     "Defense +1" : 20,
                     "Defense +2" : 40,
                     "Defense +3" : 80}
            self.gold_spent += rings[ring]
            self.rings.append(ring)
            if len(self.rings) > 2:
                self.rings = self.rings[:2]
            self.__update_stats()
        return self
        
    def __update_stats(self):
        ''' '''
        
        if not self.armor:
            self.defense = 0
        else:
            armors = {"Leather" : 1,
                      "Chainmail" : 2,
                      "Splintmail" : 3,
                      "Bandedmail" : 4,
                      "Platemail" : 5}

            self.defense = armors[self.armor]
        
        if not self.weapon:
            self.attack = 0
        else:
            weapons = {"Dagger" : 4,
                       "Shortsword" : 5,
                       "Warhammer" : 6,
                       "Longsword" : 7,
                       "Greataxe" : 8}
            
            self.attack = weapons[self.weapon]
       
        if not self.rings:
            pass
        else:
            rings = {"Damage +1" : 1,
                     "Damage +2" : 2,
                     "Damage +3" : 3,
                     "Defense +1" : 1,
                     "Defense +2" : 2,
                     "Defense +3" : 3}

            for ring in self.rings:
                if "Damage" in ring:
                    self.attack += rings[ring]
                elif "Defense" in ring:
                    self.defense += rings[ring]

        return self

def fight(player, boss):

    turn = "player"
    nturn = 0
    while True:
        nturn += 1

        #print "nturn: %s" % nturn
        #print "Turn: " + turn 
        if turn == "player":
            if not player.attack:
                turn = "boss"
                continue
            dmg = max(player.attack-boss.defense, 1)
            #print "Player did %s to boss" % dmg 
            boss.HP -= dmg
            turn = "boss"

        elif turn == "boss":
            #print "Boss did %s to boss" % dmg 
            if not boss.attack:
                turn = "player"
                continue
            dmg = max(boss.attack-player.defense, 1)
            player.HP -= dmg          
            turn = "player"

        #print "player HP: %s" % player.HP
        #print "Boss HP: %s\n" % boss.HP

        if player.HP < 0:
            #print "Player has died\n"
            return False

        if boss.HP < 0:
            #print "Boss has died\n"
            return True
    
if __name__ == "__main__":


    weapons = ["Dagger", 
               "Shortsword", 
               "Warhammer",
               "Longsword",
               "Greataxe"]

    armors = [None,
              "Leather",
              "Chainmail",
              "Splintmail",
              "Bandedmail",
              "Platemail"]

    rings  = [None,
             "Damage +1",
             "Damage +2",
             "Damage +3",
             "Defense +1",
             "Defense +2",
             "Defense +3"]


    small = 500
    large = 0

    for i in xrange(10000):

        player = Player()
        player.buy_weapon(random.choice(weapons))
        player.buy_armor(random.choice(armors))
        ring1 = random.choice(rings)
        while True:
            ring2 = random.choice(rings)
            if ring1 != ring2:
                break
        player.buy_ring(ring1)
        player.buy_ring(ring2)
        
        boss = Player()
        boss.HP = 109
        boss.attack = 8
        boss.defense = 2
        
        if fight(player, boss) and player.gold_spent <= small:

            print "PLAYER"
            print "Gold spent", player.gold_spent
            print "Armor", player.armor
            print "Weapon", player.weapon
            print "Rings:", player.rings
            print "HP: player: %s, boss: %s" % (player.HP, boss.HP)
            print "Attack", player.attack
            print "Defense %s \n" % player.defense
            
            small = player.gold_spent

        if not fight(player, boss) and player.gold_spent >= large:

            print "PLAYER"
            print "Gold spent", player.gold_spent
            print "Armor", player.armor
            print "Weapon", player.weapon
            print "Rings:", player.rings
            print "HP: player: %s, boss: %s" % (player.HP, boss.HP)
            print "Attack", player.attack
            print "Defense %s \n" % player.defense
            
            large = player.gold_spent
    
print "Cheapest victory: %s gold" % small 
print "Most expensive loss: %s gold" % large

