from cPickle import dumps, loads, dump, load

def f(): pass

def configure():
    d = {"yo": f}
    with open("yo.pk", "wb") as fid:
        dump(d, fid)

def build():
    with open("yo.pk", "rb") as fid:
        d = load(fid)
        print d

if __name__ == "__main__":
    #configure()
    build()
