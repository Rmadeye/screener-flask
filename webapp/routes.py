from webapp import app
from flask import Flask, request, render_template, send_file
from src.utils import DockerScript, Utilities
from src import decode_files
import os, tempfile

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/docking')
def docking_template():
    return render_template("docking.html")

@app.route('/dock', methods=["POST"])
def dock():
    requested_protein_id = request.form.get('protein_id').lower()
    requested_ligand = request.form.get('ligand_id').lower()
    with tempfile.TemporaryDirectory(dir = os.getcwd()) as tmpdir:
        if DockerScript(requested_protein_id, requested_ligand, tmpdir).execute() == 1:
            return send_file(tmpdir + '/result.zip', as_attachment=True)
        else:
            return render_template("error.html")

@app.route('/merger')
def merger():
    return render_template("merger.html")


@app.route('/merge', methods=["POST"])
def merge():
    requested_rigid = request.files['rigid_pdb']
    requested_flex = request.files['flex_pdb']
    utilities = Utilities()
    if not requested_rigid:
        return render_template("no_file.html")
    if not requested_flex:
        return render_template("no_file.html")
    if utilities.check_extensions(requested_rigid.filename):
        if utilities.check_extensions(requested_flex.filename):
            with tempfile.TemporaryDirectory(dir = os.getcwd()) as tmpdir:
                dfprep = decode_files.Decoder(requested_rigid, requested_flex, tmpdir)
                dfprep.bytes_to_pdb()
                return send_file(tmpdir + '/result.pdb', as_attachment=True)
        else:
            return render_template("flex_error.html")
    else:
        return render_template("rigid_error.html")


@app.route("/send_lig", methods = ["GET"])
def send_lig():
    return send_file('./sample/sample_lig_resids.pdb', as_attachment=True)


@app.route("/send_prot", methods = ["GET"])
def send_prot():

    return send_file('./sample/prot.pdb', as_attachment=True)
