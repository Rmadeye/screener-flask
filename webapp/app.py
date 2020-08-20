from flask import Flask, request, render_template, send_file
from src import ligand_prep, protein_prep, perform_docking, utils
import os, shutil

app = Flask(__name__)


@app.route('/')
def form():
    return render_template("index.html")


@app.route('/dock', methods=["POST"])
def dock():
    requested_protein_id = request.form.get('protein_id')
    requested_ligand = request.form.get('ligand_id')
    try:
        execute(requested_protein_id, requested_ligand)
        return send_file(os.path.dirname(app.instance_path) + '/results.zip', as_attachment=True)
    except:
        return render_template("error.html")


def execute(protein_id, ligand_id):
    utils.Utilities().clean()
    protein_prep.ProteinPreparer(protein_id).prepare_protein()  # prepare protein
    ligand_prep.LigandPreparer(ligand_id).prepare_ligand()  # prepare ligand
    perform_docking.VinaDocker(protein_id, ligand_id).prepare_docking_grid_and_dock()
    return shutil.make_archive('results', 'zip', './result/')
