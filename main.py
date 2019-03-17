from flask import Flask, render_template
from assaultr import AssaultRifles
from tacticalr import TacticalRifile
from lmg import LightMachineGuns
from shotgun import Shotguns
from melee import Melee
from nades import Grenades
from pistols import Pistols
from launcher import Launcher

app = Flask(__name__)

AssaultRifles = AssaultRifles()
TacticalRifile = TacticalRifile()
LightMachineGuns = LightMachineGuns()
Shotguns = Shotguns()
Melee = Melee()
Grenades = Grenades()
Pistols = Pistols()
Launcher = Launcher()

@app.route("/")
def index():
    return render_template('index.html', assultrifles = AssaultRifles, taticalrifle = TacticalRifle, lightmachinegun = LightMachineGuns, shotguns = Shotguns, malee = Melee, grenades = Grenades, pistols = Pistols, launcher = Launcher)

if __name__ == "__main__":
    app.run(debug=True, port=5685)