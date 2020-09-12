# from flask import Flask, request, render_template, send_file
# from src import ligand_prep, protein_prep, perform_docking, utils
# import os, shutil
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def form():
#     return render_template("index.html")
#
# @app.route('/dock', methods=["POST"])
# def dock():
#     requested_protein_id = request.form.get('protein_id').lower()
#     requested_ligand = request.form.get('ligand_id').lower()
#     if execute(requested_protein_id, requested_ligand) == 1:
#         return send_file(os.path.dirname(app.instance_path) + '/results.zip', as_attachment=True)
#     else:
#         return render_template("error.html")
#
#
# def execute(protein_id, ligand_id):
#     utils.Utilities().clean()
#     protein_prep.ProteinPreparer(protein_id).prepare_protein()  # prepare protein
#     if os.stat('./workdir/pdb{}.ent'.format(protein_id)).st_size > 750000 :
#         render_template("error.html"), utils.Utilities().clean()
#         return 0
#     else:
#         ligand_prep.LigandPreparer(ligand_id).prepare_ligand()  # prepare ligand
#         perform_docking.VinaDocker(protein_id, ligand_id).prepare_docking_grid_and_dock()
#         shutil.make_archive('results', 'zip', './result/')
#         return 1
