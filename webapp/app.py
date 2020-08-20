from flask import Flask, request, render_template
from src import ligand_prep, protein_prep, perform_docking
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/dock', methods=["POST"])
def dock():
    requested_protein_id = request.form.get('protein_id')
    requested_ligand = request.form.get('ligand_id')
    execute(requested_protein_id, requested_ligand)
    return render_template("index.html")

def execute(protein_id, ligand_id):
    protein_prep.ProteinPreparer(protein_id).prepare_protein() # prepare protein
    ligand_prep.LigandPreparer(ligand_id).prepare_ligand() # prepare ligand
    perform_docking.VinaDocker(
        protein_id, ligand_id
    ).prepare_docking_grid_and_dock()