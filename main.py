from process import Process
from process_tbl import ProcessTable
from algorithms import *
from copy import deepcopy as copy



def main():
    ps = ProcessTable()
    for i in range(5):
        ps.append(Process(None, i))
    print(f' Исходное состояние \n{ps.__str__()}')
    model = RR(1).main(ps)
    print(f' Исходное состояние \n{ps.__str__()}')

main()