import program

class PCB:
    def __init__ (self, programa, pid):
        self.program = programa
        self.pid = pid
        self.state = 'new'
        self.pc = 0


    def setRunning(self):
        self.state = 'running'

    def setReady (self):
        self.state = 'ready'

    def next_pc(self):
        self.pc = self.pc + 1
