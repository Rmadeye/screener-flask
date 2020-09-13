from src import ligand_prep, protein_prep, perform_docking
import os, shutil

class DockerScript:
    def __init__(self, protein_id, ligand_id, tmpdir):
        self.protein_id = protein_id
        self.ligand_id = ligand_id
        self.tmpdir = tmpdir

    def execute(self):
        protein_prep.ProteinPreparer(self.protein_id, self.tmpdir).prepare_protein()  # prepare protein
        if os.stat(self.tmpdir + '/pdb{}.ent'.format(self.protein_id)).st_size > 750000:
            return 0
        else:
            ligand_prep.LigandPreparer(self.ligand_id, self.tmpdir).prepare_ligand()  # prepare ligand
            perform_docking.VinaDocker(self.protein_id, self.ligand_id, self.tmpdir).prepare_docking_grid_and_dock()
            shutil.make_archive(self.tmpdir+'/result', 'zip', self.tmpdir + '/results/')
            return 1

class Utilities:
    def __init__(self):
        pass

    def clean(self):
        for the_file in os.listdir('./workdir/'):
            file_path = os.path.join('./workdir/', the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        for the_file in os.listdir('./result/'):
            file_path = os.path.join('./result/', the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        return None
        pass

    def clean_merger(self):
        folder = './workdir'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        open(folder + "/cleaned.txt", "w")
        return None
        pass

    def check_extensions(self, filename):
        if any(filename.endswith(e) for e in ['.pdb', '.txt', '.pdbqt', '.save']):
            return True
