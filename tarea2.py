# DO NOT CHANGE THE FUNCTION SIGNATURE IN THE SOLUTION AREA
import random
power = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']

saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']



# Which sorcerer won the battle - Gandalf or Saruman?
def battle():
    # YOUR SOLUTION HERE
    gandalf_score = 0
    saruman_score = 0
    
    while gandalf_score != 3 and saruman_score != 3:
      gand_spell = gandalf[random.randint(0,len(gandalf) - 1)]    
      saru_spell = saruman[random.randint(0,len(saruman) - 1)]  
      
      gand_power = power[gand_spell]
      saru_power = power[saru_spell]
      
      if gand_power > saru_power:
        gandalf_score += 1
        saruman_score = 0
      else:
        if gand_power < saru_power:
          gandalf_score = 0
          saruman_score += 1
    
    if gandalf_score == 3 or saruman_score == 3:
      if gandalf_score == 3:
        solution1 = "gandalf"
      else:
        solution1 = "saruman"
    else:
      solution1 = "tie"

    
    return solution1