import pcb

class Loader:
    def __init__ (self, disk, memory):
        self.disk = disk
        self.memory = memory
        self.pcb_list = []

    def execute(self, program_name):
        for program in self.disk.programs:
            if program_name == program.name:
                self.memory.append(program)
                self.generate_pcb(program)

    def generate_pcb (self, program):
        self.pcb_list.append(PCB(program, self.next_pid()))

    def next_pid(self):
        return len(self.pcb_list)
