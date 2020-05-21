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
# key = ['health', 'mana', 'melee', 'armor']
# value = [490, 334, 550, 18.72]
# lux = dict(zip(key, value))
# print(lux)
# # {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# lux['mana'] = 1000  # update
# lux['power'] = 100  # append
# print(lux)
# # {'health': 490, 'mana': 1000, 'melee': 550, 'armor': 18.72, 'power': 100}
# print('power' in lux)  # True
# print(len(lux))  # 5
#
# camille = {
#     'health': 575.6,
#     'health_regen': 1.7,
#     'mana': 338.8,
#     'mana_regen': 1.63,
#     'melee': 125,
#     'attack_damage': 60,
#     'attack_speed': 0.625,
#     'armor': 26,
#     'magic_resistance': 32.1,
#     'movement_speed': 340
# }
# print(camille['health'], camille['movement_speed'])

# init
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# print(x)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#
# # setdefault, update
# x.setdefault('e', 50)  #
# x.update(a=100, b=200, c=300, d=400)  # {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 50}
# print(x)
#
# # pop, popitem, clear
#
# # get
#
# # items, keys, values
# print(x.items())
# print(x.keys())
# print(x.values())
#
# # list, tuple => dict
# keys = ['a', 'b', 'c', 'd']
# x = dict.fromkeys(keys)  # {'a': None, 'b': None, 'c': None, 'd': None}
# print(x)
#
# # defaultdict()
# from collections import defaultdict as ddict
# y = ddict(int)
# print(y['z'])  # 0
#
# # dict comprehension
# keys = ['a', 'b', 'c', 'd']
# x = {k: v for k, v in dict.fromkeys(keys).items()}
# print(x)
#
# dict in dict
# terrestrial_planet = {
#     'Mercury': {
#         'mean_radius': 2439.7,
#         'mass': 3.3022E+23,
#         'orbital_period': 87.969
#     },
#     'Venus': {
#         'mean_radius': 6051.8,
#         'mass': 4.8676E+24,
#         'orbital_period': 224.70069,
#     },
#     'Earth': {
#         'mean_radius': 6371.0,
#         'mass': 5.97219E+24,
#         'orbital_period': 365.25641,
#     },
#     'Mars': {
#         'mean_radius': 3389.5,
#         'mass': 6.4185E+23,
#         'orbital_period': 686.9600,
#     }
# }
# print(terrestrial_planet['Mercury']['mass'])
#
# # copy
# x = {'a': 10, 'b': {'b': 20, 'c': 30}, 'd': 40}
# y = x
# y['a'] = 100
# print(x)  # {'a': 100, 'b': {'b': 20, 'c': 30}, 'd': 40}
# print(y)  # {'a': 100, 'b': {'b': 20, 'c': 30}, 'd': 40}
# y = x.copy()
# y = x.deepcopy()  # need import

# average
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(sum(maria.values()) / len(maria))
