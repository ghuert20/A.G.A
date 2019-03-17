from flask import Flask, render_template
from app import AssaultRifles, TacticalRifile, LightMachineGuns, Shotguns, Melee, Grenades, Pistols

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', assultrifles = Assault Rifles, taticalrifle = RacticalRifle, lightmachinegun = LighrMachineGuns, shotguns = Shotguns, malee = Melee, grenades = Grenades, pistols = Pistols)

if __name__ == "__main__":
    app.run(debug=True, port=5685)