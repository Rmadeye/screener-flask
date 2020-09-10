from Bio.PDB import *
import os, shutil

# set preparation pathways
prepare_protein_path = '~/MGLTools-1.5.6/mgltools_x86_64Linux2_1.5.6/bin/pythonsh ~/MGLTools-1.5.6/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -A bonds_hydrogens -U nphs_lps_waters_nonstdres -r'

"""Class inheriting from Select checking if the residue is aminoacid"""


class ResSelect(Select):
    def accept_residue(self, residue):
        if is_aa(residue):
            return 1
        else:
            return 0


class ProteinPreparer:

    def __init__(self, protein: str):
        self.protein = protein
        self.filename = './workdir/pdb{}.ent'.format(self.protein)

    def prepare_protein(self):
        parser = PDBParser()
        io = PDBIO()
        PDBList().retrieve_pdb_file(pdb_code=self.protein, pdir='./workdir/',
                                    file_format='pdb')  # saves pdb in a form of ent file
        ipdb = parser.get_structure('ipdb', self.filename)  # Input pdb as a self.filename
        io.set_structure(ipdb)  # Setting structure for input pdb
        io.save('./workdir/' + self.protein + '.pdb', ResSelect(),
                preserve_atom_numbering=True)  # saves the cleaned pdb
        os.system(prepare_protein_path + './workdir/{}.pdb'.format(
            self.protein))  # prepares the structure by adding polar hydrogens and adding gesteiger charges
        shutil.move(self.protein + '.pdbqt', './workdir/')
