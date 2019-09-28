class ProcessTable(list):
    def __init__(self):
        super(ProcessTable, self).__init__()
        self.finish_time = None

    def __str__(self):
        result = ''
        for elem in self:
            result += f' {str(elem)}'
        return result

    def tickAll(self):
        for elem in self:
            elem.tick()

    def finished(self):
        for elem in self:
            if elem.state != 'terminated':
                return False
        return True

    def sortByReady(self):
        self.sort(key=lambda p: p.timeEnteredReady)
        return self