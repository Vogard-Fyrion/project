from ursina import *
import random

app = Ursina()


window.title = 'Game'
window.borderless = False
window.exit_button.visible = False


# background = Entity(model = 'plane', color = color.black, scale_z = 15, scale_x = 20, rotation = (90, 90, 90), origin = (0, 5, 0))
command_frame = Entity(model = 'plane', color = color.black, scale = (3, 1, 3), rotation = (90, 90, 90), origin = (-1.25, 0, -.95))
information_frame = Entity(model = 'plane', color = color.black, scale = (10, 1, 3),rotation = (90, 90, 90), origin = (.3, 0, -.95))

character1 = Entity(model = 'cube', color = color.blue, scale_y = 2, origin = (5, -.25, 0))
# character2 = Entity(model = 'cube', color = color.green, origin = (4.75, -.25, -1))
# character3 = Entity(model = 'cube', color = color.blue, origin = (4.5, -.5, -2))
# character4 = Entity(model = 'cube', color = color.red, origin = (4.25, -.75, -3))

enemy_slot1 = Entity(model = 'cube', color = color.red, scale_y = 2, origin = (-3.5, -.25, 0))
# enemy_slot2 = Entity(model = 'cube', color = color.green , origin = (-3.25, -.25, -1))
# enemy_slot3 = Entity(model = 'cube', color = color.blue , origin = (-3, -.5, -2))
# enemy_slot4 = Entity(model = 'cube', color = color.orange , origin = (-2.75, -.75, -3))

# enemy_slot5 = Entity(model = 'cube', color = color.red , origin = (-5, 0, 0))
# enemy_slot6 = Entity(model = 'cube', color = color.green , origin = (-4.75, -.25, -1))
# enemy_slot7 = Entity(model = 'cube', color = color.blue , origin = (-4.5, -.5, -2))
# enemy_slot8 = Entity(model = 'cube', color = color.orange , origin = (-4.25, -.75, -3))


character = {
    "name": "Blue",
    "health": 100,
    "max_health": 100,
    "attack": 10,
    "defense": 0,
    "speed": 0,
    "speed_regen": 20,
    "guarding": False,
    "resource": 100,
    "resource_max": 100
}

enemy = {
    "name": "Red",
    "health": 100,
    "max_health": 100,
    "attack": 10,
    "defense": 0,
    "speed": 0,
    "speed_regen": 30,
    "guarding": False,
    "resource": 100,
    "resource_max": 100
}

def fight(char, target):
    char['guarding'] = False
    if char["attack"] > target["defense"]:
        damage = char["attack"] - target["defense"]
        if target["guarding"] == True:
            damage = damage // 2
        return damage
    return 0

def defend(char):
    char['guarding'] = True
    if char['health'] <= int(char['max_health'] * .95):
        char['health'] += int(char['max_health'] * .05)
    else:
        char['health'] = char['max_health']

def skill(char, target):
    return fight(char, target) + fight(char, target)

Text.size = 0.04

character_health = Text(text = f"Health {character['health']} / {character['max_health']}")
character_health.x = -.7
character_health.y = -.075

character_resource = Text(text = f"Resource {character['resource']} / {character['resource_max']}")
character_resource.x = -.7
character_resource.y = -.12


enemy_health = Text(text = f"Health {enemy['health']} / {enemy['max_health']}")
enemy_health.x = .2
enemy_health.y = -.075

enemy_resource = Text(text = f"Resource {enemy['resource']} / {enemy['resource_max']}")
enemy_resource.x = .2
enemy_resource.y = -.12


attack = Text(text = 'Attack', color = color.white)
attack.x = -.6
attack.y = -.2
attack.collider = BoxCollider(attack, center = Vec3(.057, -.017, 0), size = Vec3(.115, .032, .1))
# attack.collider.show()

guard = Text(text = "Guard", color = color.white)
guard.x = -.6
guard.y = -.24
guard.collider = BoxCollider(guard, center = Vec3(.057, -.017, 0), size = Vec3(.115, .032, .1))
# guard.collider.show()

skills = Text(text = "Skills", color = color.white)
skills.x = -.6
skills.y = -.28
skills.collider = BoxCollider(skills, center = Vec3(.048, -.017, 0), size = Vec3(.09, .032, .1))
# skills.collider.show()

info = Text(text = "")
info.x = -.2
info.y = -.2

info2 = Text(text = "")
info2.x = -.2
info2.y = -.25


fight_again = Text(text = "Fight again?", color = color.white)
fight_again.collider = BoxCollider(fight_again, center = Vec3(.11, -.017, 0), size = Vec3(.22, .05, .1))
fight_again.x = -.2
fight_again.y = .3
# fight_again.collider.show()
fight_again.visible = False

def update():
    character_health.text = f"Health {character['health']} / {character['max_health']}"
    character_resource.text = f"Resource {character['resource']} / {character['resource_max']}"
    enemy_health.text = f"Health {enemy['health']} / {enemy['max_health']}"
    enemy_resource.text = f"Resource {enemy['resource']} / {enemy['resource_max']}"
    if character['health'] <= 0 or enemy['health'] <= 0:
        fight_again.visible = True
    else:
        fight_again.visible = False

    # character['speed'] += character['speed_regen']
    # enemy['speed'] += enemy['speed_regen']
    # if character['speed'] >= 100 or enemy['speed'] >= 100:
    #     if character['speed'] >= enemy['speed']:
    #         character['speed'] = 0
    #     else:
    #         enemy['speed'] = 0
    #     if character['speed'] >= 100:
    #         character['speed'] = 0


    # background.x += held_keys['d'] * time.dt
    # background.x -= held_keys['a'] * time.dt
    # background.y += held_keys['w'] * time.dt
    # background.y -= held_keys['s'] * time.dt
    # if held_keys['x']:
    #     background.rotation_x += time.dt * 5
    # if held_keys['y']:
    #     background.rotation_y += time.dt * 5
    # if held_keys['z']:
    #     background.rotation_z += time.dt * 5
    # if mouse.hovered_entity == attack:
    #     slash(character, enemy)
    # else:
    #     slash.visible = True
    # if mouse.left == attack:
    #     print('click')
    #     slash(character, enemy)

def enemy_turn(char, target):
    chance = random.randint(1, 100)
    if char['health'] >= 70:
        if char['resource'] >= 60:
            if chance > 50:
                damage = skill(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    char['resource'] -= 30
                    info2.text = f"{char['name']} used skill, dealing {damage} damage to {target['name']}."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
        elif char['resource'] >= 30:
            if chance > 80:
                damage = skill(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    char['resource'] -= 30
                    info2.text = f"{char['name']} used skill, dealing {damage} damage to {target['name']}."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
        else:
            damage = fight(char, target)
            if target['health'] > damage:
                target['health'] -= damage
                info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
            else:
                target['health'] = 0
                info2.text = f"{char['name']} wins!"
    elif char['health'] >= 30:
        if char['resource'] >= 60:
            if chance > 80:
                damage = skill(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    char['resource'] -= 30
                    info2.text = f"{char['name']} used skill, dealing {damage} damage to {target['name']}."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            elif chance > 50:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                defend(char)
                info2.text = f"{char['name']} puts up their guard."
        elif char['resource'] >= 30:
            if chance > 80:
                damage = skill(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    char['resource'] -= 30
                    info2.text = f"{char['name']} used skill, dealing {damage} damage to {target['name']}."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            elif chance > 50:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                defend(char)
                info2.text = f"{char['name']} puts up their guard."
        else:
            if chance > 50:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                defend(char)
                info2.text = f"{char['name']} puts up their guard."
    else:
        if char['resource'] >= 60:
            if chance > 80:
                damage = skill(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    char['resource'] -= 30
                    info2.text = f"{char['name']} used skill, dealing {damage} damage to {target['name']}."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            elif chance > 70:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                defend(char)
                info2.text = f"{char['name']} puts up their guard."
        elif char['resource'] >= 30:
            if chance > 80:
                damage = skill(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    char['resource'] -= 30
                    info2.text = f"{char['name']} used skill, dealing {damage} damage to {target['name']}."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            elif chance > 70:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                defend(char)
                info2.text = f"{char['name']} puts up their guard."
        else:
            if chance > 70:
                damage = fight(char, target)
                if target['health'] > damage:
                    target['health'] -= damage
                    info2.text = f"{char['name']} attacks {target['name']}, dealing {damage} damage."
                else:
                    target['health'] = 0
                    info2.text = f"{char['name']} wins!"
            else:
                defend(char)
                info2.text = f"{char['name']} puts up their guard."
    if enemy['resource'] <= int(enemy['resource_max'] * .95):
        enemy['resource'] += int(enemy['resource_max'] * .05)
    else:
        enemy['resource'] = enemy['resource_max']








def input(key):
    if key == 'left mouse down' and mouse.hovered_entity == fight_again:
        character['health'] = character['max_health']
        character['resource'] = character['resource_max']
        enemy['health'] = enemy['max_health']
        enemy['resource'] = enemy['resource_max']
        info.text = ""
        info2.text = ""

    if key == 'left mouse down' and mouse.hovered_entity == guard:
        defend(character)
        info.text = f"{character['name']} puts up their guard."
        if enemy['health'] > 0:
            invoke(Func(enemy_turn, enemy, character), delay = 2)
        if character['resource'] <= int(character['resource_max'] * .95):
            character['resource'] += int(character['resource_max'] * .05)
        else:
            character['resource'] = character['resource_max']
        if enemy['resource'] <= int(enemy['resource_max'] * .95):
            enemy['resource'] += int(enemy['resource_max'] * .05)
        else:
            enemy['resource'] = enemy['resource_max']

    if key == 'left mouse down' and mouse.hovered_entity == skills and character['resource'] >= 30:
        damage = skill(character, enemy)
        character['resource'] -= 30
        if enemy['health'] > damage:
            enemy['health'] -= damage
            info.text = f"{character['name']} used skill, dealing {damage} damage to {enemy['name']}."
        else:
            enemy['health'] = 0
            info.text = f"{character['name']} wins!"
        if enemy['health'] > 0:
            invoke(Func(enemy_turn, enemy, character), delay = 2)
        if character['resource'] <= int(character['resource_max'] * .95):
            character['resource'] += int(character['resource_max'] * .05)
        else:
            character['resource'] = character['resource_max']
        if enemy['resource'] <= int(enemy['resource_max'] * .95):
            enemy['resource'] += int(enemy['resource_max'] * .05)
        else:
            enemy['resource'] = enemy['resource_max']

    if key == 'left mouse down' and mouse.hovered_entity == attack:
        damage = fight(character, enemy)
        if enemy['health'] > damage:
            enemy['health'] -= damage
            info.text = f"{character['name']} attacks {enemy['name']}, dealing {damage} damage."
        else:
            enemy['health'] = 0
            info.text = f"{character['name']} wins!"
        if enemy['health'] > 0:
            invoke(Func(enemy_turn, enemy, character), delay = 2)
            if character['resource'] <= int(character['resource_max'] * .95):
                character['resource'] += int(character['resource_max'] * .05)
            else:
                character['resource'] = character['resource_max']


app.run()

