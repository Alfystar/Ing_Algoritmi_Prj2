if __name__ == '__main__':
    """
    script per leggere in chiaro cProfile e magari salvarlo in bash
    sys.argv:
    [1]-> nome file output del profile da visualizzare
    [2]-> modalità di ordinamento dei dati
    ncalls, tottime, percall, cumtime
    """

    import pstats
    import sys
    if(len(sys.argv)==3):
        p = pstats.Stats(sys.argv[1])
        p.strip_dirs().sort_stats(sys.argv[2]).print_stats()
    else:
        print("argomenti errati!!!!! \n <nome_file_profile> <sort per quale parametro>")
