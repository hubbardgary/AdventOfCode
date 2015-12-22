# --- Day 22: Wizard Simulator 20XX ---
#
# Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a
# wizard. Of course, he gets stuck on another boss and needs your help again.
#
# In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes
# first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first
# character at or below 0 hit points loses.
#
# Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic
# damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor
# (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always
# deal at least 1 damage.
#
# On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose.
# Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and
# its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.
#
# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it
# deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it
# gives you 101 new mana.
#
# Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are
# created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they
# have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell
# that would start an effect which is already active. However, effects can be started on the same turn they end.
#
# For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:
#
# -- Player turn --
# - Player has 10 hit points, 0 armor, 250 mana
# - Boss has 13 hit points
# Player casts Poison.
#
# -- Boss turn --
# - Player has 10 hit points, 0 armor, 77 mana
# - Boss has 13 hit points
# Poison deals 3 damage; its timer is now 5.
# Boss attacks for 8 damage.
#
# -- Player turn --
# - Player has 2 hit points, 0 armor, 77 mana
# - Boss has 10 hit points
# Poison deals 3 damage; its timer is now 4.
# Player casts Magic Missile, dealing 4 damage.
#
# -- Boss turn --
# - Player has 2 hit points, 0 armor, 24 mana
# - Boss has 3 hit points
# Poison deals 3 damage. This kills the boss, and the player wins.
# Now, suppose the same initial conditions, except that the boss has 14 hit points instead:
#
# -- Player turn --
# - Player has 10 hit points, 0 armor, 250 mana
# - Boss has 14 hit points
# Player casts Recharge.
#
# -- Boss turn --
# - Player has 10 hit points, 0 armor, 21 mana
# - Boss has 14 hit points
# Recharge provides 101 mana; its timer is now 4.
# Boss attacks for 8 damage!
#
# -- Player turn --
# - Player has 2 hit points, 0 armor, 122 mana
# - Boss has 14 hit points
# Recharge provides 101 mana; its timer is now 3.
# Player casts Shield, increasing armor by 7.
#
# -- Boss turn --
# - Player has 2 hit points, 7 armor, 110 mana
# - Boss has 14 hit points
# Shield's timer is now 5.
# Recharge provides 101 mana; its timer is now 2.
# Boss attacks for 8 - 7 = 1 damage!
#
# -- Player turn --
# - Player has 1 hit point, 7 armor, 211 mana
# - Boss has 14 hit points
# Shield's timer is now 4.
# Recharge provides 101 mana; its timer is now 1.
# Player casts Drain, dealing 2 damage, and healing 2 hit points.
#
# -- Boss turn --
# - Player has 3 hit points, 7 armor, 239 mana
# - Boss has 12 hit points
# Shield's timer is now 3.
# Recharge provides 101 mana; its timer is now 0.
# Recharge wears off.
# Boss attacks for 8 - 7 = 1 damage!
#
# -- Player turn --
# - Player has 2 hit points, 7 armor, 340 mana
# - Boss has 12 hit points
# Shield's timer is now 2.
# Player casts Poison.
#
# -- Boss turn --
# - Player has 2 hit points, 7 armor, 167 mana
# - Boss has 12 hit points
# Shield's timer is now 1.
# Poison deals 3 damage; its timer is now 5.
# Boss attacks for 8 - 7 = 1 damage!
#
# -- Player turn --
# - Player has 1 hit point, 7 armor, 167 mana
# - Boss has 9 hit points
# Shield's timer is now 0.
# Shield wears off, decreasing armor by 7.
# Poison deals 3 damage; its timer is now 4.
# Player casts Magic Missile, dealing 4 damage.
#
# -- Boss turn --
# - Player has 1 hit point, 0 armor, 114 mana
# - Boss has 2 hit points
# Poison deals 3 damage. This kills the boss, and the player wins.
#
# You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least
# amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative
# mana.)
import itertools
import random

spell_names = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
spell_cost = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}
spell_damage = {
    "Magic Missile": 0,
    "Drain": 0,
    "Shield": 0,
    "Poison": 3,
    "Recharge": 0
}
spell_instant_damage = {
    "Magic Missile": 4,
    "Drain": 2,
    "Shield": 0,
    "Poison": 0,
    "Recharge": 0
}
spell_heal = {
    "Magic Missile": 0,
    "Drain": 0,
    "Shield": 0,
    "Poison": 0,
    "Recharge": 0
}
spell_instant_heal = {
    "Magic Missile": 0,
    "Drain": 2,
    "Shield": 0,
    "Poison": 0,
    "Recharge": 0
}
spell_armour = {
    "Magic Missile": 0,
    "Drain": 0,
    "Shield": 7,
    "Poison": 0,
    "Recharge": 0
}
spell_mana = {
    "Magic Missile": 0,
    "Drain": 0,
    "Shield": 0,
    "Poison": 0,
    "Recharge": 101
}
spell_duration = {
    "Magic Missile": 0,
    "Drain": 0,
    "Shield": 6,
    "Poison": 6,
    "Recharge": 5
}
spell_remaining = {
    "Magic Missile": 1,
    "Drain": 0,
    "Shield": 6,
    "Poison": 6,
    "Recharge": 5
}


def damage(spells, new_spell):
    d = 0
    for s in spells:
        d += spell_damage[s]
    d += spell_instant_damage[new_spell] if new_spell is not "" else 0
    return d


def armour(spells):
    a = 0
    for s in spells:
        a += spell_armour[s]
    return a


def heal(spells, new_spell):
    h = 0
    for s in spells:
        h += spell_heal[s]
    h += spell_instant_heal[new_spell] if new_spell is not "" else 0
    return h


def mana(spells):
    m = 0
    for s in spells:
        m += spell_mana[s]
    return m


def update_spell_remaining(spells):
    spells_still_active = []
    for s in spells:
        if spell_remaining[s] == 1:
            spell_remaining[s] = spell_duration[s]
        else:
            spell_remaining[s] -= 1
            spells_still_active.append(s)
    spells = list(spells_still_active)
    return spells


active_spells = list()

boss_health_points = 51
boss_attack_points = 9

player_health_points = 50
player_mana_points = 500
spent_mana = 0
moves = []
cheapest_win = 9999
cheapest_moves = []

# spell_prods = list(itertools.product(spell_names, repeat=6))
# print(spell_prods)

# These are to test the example on website
#order = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile', 'Magic Missile', 'Magic Missile']
#a = 0
for i in range(0, 100000):
    #print(i)
    while boss_health_points > 0 and player_health_points > 0:
        # If you can't afford to cast any spells, you lose
        if player_mana_points < min(spell_cost.values()):
            player_health_points = 0
            break

        # Hard mode
        player_health_points -= 1
        if player_health_points < 1:
            break

        # Player turn - existing spells
        boss_health_points -= damage(active_spells, "")
        player_health_points += heal(active_spells, "")
        player_mana_points += mana(active_spells)
        active_spells = update_spell_remaining(active_spells)

        # cast new spell

        random.shuffle(spell_names)
        current_spell = spell_names[0]
        while current_spell in active_spells:
            random.shuffle(spell_names)
            current_spell = spell_names[0]
        #current_spell = order[a]
        #a += 1
        if player_mana_points >= spell_cost[current_spell] and current_spell not in active_spells:
            player_mana_points -= spell_cost[current_spell]
            spent_mana += spell_cost[current_spell]
            boss_health_points -= damage([], current_spell)
            player_health_points += heal([], current_spell)
            # Add current spell so effect is applied next time
            if spell_duration[current_spell] > 0:
                active_spells.append(current_spell)
            moves.append(current_spell)


        # Boss turn
        boss_health_points -= damage(active_spells, "")
        player_mana_points += mana(active_spells)
        active_spells = update_spell_remaining(active_spells)

        if boss_health_points < 1:
            break

        # Boss attacks
        player_health_points -= max(1, boss_attack_points - armour(active_spells))

    if boss_health_points < 1:
        #print("Boss dead: {0} - {1}".format(spent_mana, moves))
        if spent_mana < cheapest_win:
            cheapest_win = spent_mana
            cheapest_moves = moves
    # elif player_health_points < 1:
    #     print("Player dead: {0} - {1}".format(spent_mana, moves))

    # Resurrect and reset
    boss_health_points = 51
    player_health_points = 50
    player_mana_points = 500
    spent_mana = 0
    active_spells = []
    moves = []
    for s in spell_names:
        spell_remaining[s] = spell_duration[s]

print("Cheapest win is {0} with {1}".format(cheapest_win, cheapest_moves))
