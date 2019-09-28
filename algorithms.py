from process_tbl import ProcessTable
from timer import Timer


class SchedulingAlgorithm:
    def __init__(self, algoName):
        self.Timer = Timer()
        self.algoName = algoName

    def main(self, ps):
        while not ps.finished():
            self.prepare(ps)
            if ps[0].state in ['ready', 'blocked', 'unstarted']:
                ps[0].start()
            ps.tickAll()




    def print_tbl(self, ps, done ):
        print(f'Активные процессы \n')
        print(f'\n{ps.__str__()}')
        print(f'Завешенные процессы')
        print(f'\n{done.__str__()}')

    def prepare(self, ps_t):
        pass


class FCFS(SchedulingAlgorithm):
    def __init__(self):
        super().__init__('First Come First Serve')


    def prepare(self, ps):
        if ps[0].state == 'terminated':
            ps.insert(len(ps)-1, ps.pop(0))



    def main(self, ps):
        super().main(ps)


class RR(SchedulingAlgorithm):
    def __init__(self, q):
        super().__init__('Round Robin')
        self.quantum = q
        self.c_time = 0
        self.index = 0

    def main(self, ps):
        super().main(ps)

    def index_next(self, ps):
        if len(ps)-1 <= self.index:
            self.index = 0
        else:
            self.index += 1

    def prepare(self, ps):
        if ps[0].state == 'terminated':
            self.c_time = 0
            ps.insert(len(ps) - 1, ps.pop(0))
        elif self.c_time == self.quantum:
            ps[0].block()
            ps.insert(len(ps) - 1, ps.pop(0))
            self.c_time = 0
        self.c_time += 1



