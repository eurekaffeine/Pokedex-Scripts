import common.poke_apis as poke_apis

def parse_all_move_name_translations():
    res = {}
    for i in range(1, 920):
        res[str(i)] = parse_move_name_translation(i)
    return res


def parse_move_name_translation(id):
    print(f"[START][parse_move_name_translation]{id}")
    res = {}
    move = poke_apis.get_move(id)
    for item in move["names"]:
        lang = item["language"]["name"]
        if lang != "ja-Hrkt":
            res[lang] = item["name"]
    print(f"[END][parse_move_name_translation]{id}")
    return res

def parse_ability_name_translation(id):
    print(f"[START][parse_ability_name_translation]{id}")
    res = {}
    ability = poke_apis.get_ability(id)
    for item in ability["names"]:
        lang = item["language"]["name"]
        if lang != "ja-Hrkt":
            res[lang] = item["name"]
    print(f"[END][parse_ability_name_translation]{id}")
    return res

def parse_all_ability_name_translations():
    res = {}
    for i in range(1, 312):
        res[str(i)] = parse_ability_name_translation(i)
    return res

