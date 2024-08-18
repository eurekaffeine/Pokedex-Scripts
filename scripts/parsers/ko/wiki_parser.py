import common.fetcher as fetcher
import common.translations as translations
import re, os
import utils.json_utils as json_utils

BASE_URL = "https://pokemon.fandom.com/ko/wiki/"


def pokemon_url(pokemon_name):
    return f"{BASE_URL}{pokemon_name}_(포켓몬)?action=raw"


# find the first match of the pattern in the text 
# e.g. "{{도감/설명1|버전=바이올렛|글자색=fff|설명=복숭아처럼 생긴 껍질은 그야말로 맹독의 저장고다. 독이 든 떡을 만들어서 사람과 포켓몬에게 대접한다.}}" => "복숭아처럼 생긴 껍질은 그야말로 맹독의 저장고다. 독이 든 떡을 만들어서 사람과 포켓몬에게 대접한다."

def find_sv_flavor_text(text):
    pattern1 = r"\{\{도감/설명1\|버전=스칼렛\|글자색=[^|]+\|설명=([^}]+)\}\}"
    pattern2 = r"\{\{도감/설명1\|버전=바이올렛\|글자색=[^|]+\|설명=([^}]+)\}\}"

    match1 = re.search(pattern1, text)
    if match1 and len(match1.groups(1)) > 0:
        return match1.groups(1)[0]
    match2 = re.search(pattern2, text)
    if match2 and len(match2.groups(1)) > 0:
        return match2.groups(1)[0]
    pattern3 = r"\|스칼렛 도감=([^|]+)" 
    match3 = re.search(pattern3, text)
    if match3 and len(match3.groups(1)) > 0:
        return match3.groups(1)[0]
    pattern4 = r"\|바이올렛 도감=([^}]+)"
    match4 = re.search(pattern4, text)
    if match4 and len(match4.groups(1)) > 0:
        return match4.groups(1)[0]

def find_all_sv_flavor_text():
    pokemons = translations.pokemons()
    for i in range(902, 1026):
        print(f"Processing {i}")
        pokemon_name = pokemons.get(str(i))["ko"]
        res = []
        url = pokemon_url(pokemon_name)
        for line in fetcher.fetch_html(url).split("\n"):
            flavor_text = find_sv_flavor_text(line)
            if flavor_text is not None:
                res.append(flavor_text)
        
        if len(res) > 0:
            json_utils.save_json(res, os.path.join(os.path.dirname(__file__), f"../../../intermediate/translations/{i}.json"))
        

def find_invalid_flavor_text():
    root, _, files = next(os.walk(os.path.join(os.path.dirname(__file__), "../../../intermediate/translations/")))
    for file in files:
        data = json_utils.open_json(os.path.join(root, file))
        if len(data) != 2:
            print(file)
        for item in data:
            if "|" in item or "{" in item or "}" in item:
                print(file)
                
def merge_into_flavor_text():
    sv_flavor_text_path = os.path.join(os.path.dirname(__file__), "../../../assets/translations/sv-flavor-texts/")
    root, _, files = next(os.walk(os.path.join(os.path.dirname(__file__), "../../../intermediate/translations/")))
    for file in files:
        print(f"Processing {file}")
        output_path = os.path.join(sv_flavor_text_path, file)
        to_write = json_utils.open_json(os.path.join(root, file))
        written_to = json_utils.open_json(output_path)
        written_to["ko"] = to_write
        json_utils.save_json(written_to, output_path)
               

if __name__ == "__main__":
    merge_into_flavor_text()
