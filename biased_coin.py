import random

def flip_biased_coin(p):
    return random.choice(["panna", "orel"])

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
