from flask import Flask, render_template, request

from data.bosses import ALL_BOSSES
from data.shields import ALL_SHIELDS
from models import DamageType, Shield

app = Flask(__name__)

damage_mapping = {
    DamageType.lightning_damage.name: "lightning_damage",
    DamageType.fire_damage.name: "fire_damage",
    DamageType.magic_damage.name: "magic_damage",
    DamageType.holy_damage.name: "holy_damage",
}


def rank_shields(boss):
    shield_resistances = []
    for key, value in ALL_SHIELDS.items():
        shield_resistances.append((value.name, getattr(value, boss.damage_type.name)))
    return shield_resistances


@app.route("/")
def index():
    bosses = ALL_BOSSES.keys()
    print(bosses)
    return render_template("index.html", bosses=bosses)


@app.route("/shields", methods=["POST"])
def shields():
    boss = ALL_BOSSES.get(request.form["boss_id"])
    results = rank_shields(boss)
    featured = ALL_SHIELDS["guardians_greatshield"]
    return render_template(
        "shields.html", boss=boss, shields=results, featured=featured
    )


if __name__ == "__main__":
    app.run(debug=True)
