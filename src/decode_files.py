from src.system_preparation import PDBQTprep

class Decoder:
    def __init__(self, protein, flex, tmpdir):
        self.protein = protein
        self.flex = flex
        self.tmpdir = tmpdir

    def bytes_to_pdb(self) -> str:

        for line in self.flex:
            strline = str(line, 'utf-8')
            with open(self.tmpdir+'/flex.tmp.pdb', 'a+') as clnout:
                clnout.write(strline)

        for line in self.protein:
            strline = str(line, 'utf-8')
            with open(self.tmpdir+'/rigid.tmp.pdb', 'a+') as rgout:
                rgout.write(strline)

        dfp = PDBQTprep(self.tmpdir+'/rigid.tmp.pdb',
                                    self.tmpdir+'/flex.tmp.pdb', self.tmpdir)

        return dfp.files_preparation()
