from JumpScale import j

class Cmds():

    def new(self, **args):
        return 'User created successfully.'

    def error(self):
        raise RuntimeError("just an error")

    def list(self,**args):       
        out=""
        for i in range(10):
            out+=self.get()
            out+="\n"
                
        return out


    def get(self, **args):    
        out="""
name=aperson
tel=atel
emails=1,2
"""
        return out

    def check(self,**args):
        return "OK"

