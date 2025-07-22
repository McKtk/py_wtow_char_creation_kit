import pickle

def read_bin(filename):
    filename = "./bin/"+filename+".bin"
    with open(filename, "rb") as f:
        return(pickle.load(f))
    