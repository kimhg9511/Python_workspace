# x = {
#     100: 'hundred',
#     False: 0,
#     3.5: [3.5, 3.5]
# }
# lux = {
#     'health': 490,
#     'health': 690,
#     'mana': 334,
#     'melee': 550,
#     'armor': 18.72
# }
# lux = dict(health=490, mana=334, melee=550, armor=18.72)
# lux = dict(zip(['health', 'mana', 'melee'], [490, 334, 550]))
key = ['health', 'mana', 'melee', 'armor']
value = [490, 334, 550, 18.72]
lux = dict(zip(key, value))
print(lux)
# {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['mana'] = 1000  # update
lux['power'] = 100  # append
print(lux)
# {'health': 490, 'mana': 1000, 'melee': 550, 'armor': 18.72, 'power': 100}
print('power' in lux)  # True
print(len(lux))  # 5

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'], camille['movement_speed'])