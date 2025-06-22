def write_pickle(obj_in, path_in, file_name):
    #https://docs.python.org/3/library/pickle.html
    import pickle
    # dump information to that file
    pickle.dump(obj_in, open(
        path_in + file_name + '.pk', 'wb'))
    
def read_pickle(path_in, file_name):
    import pickle
    tmp_o = pickle.load(
        open(path_in + file_name + ".pk", 'rb'))
    return tmp_o