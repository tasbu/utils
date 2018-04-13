import sys


a = sys.argv


class SetOps:

    def __init__(self, opts):
        self.opts = opts
        self.default_delim = '\t'

    def to_set(self, f, field):
        s = set()
        delim = self.get_delim(f)
        ff = open(f, "r")
        count = 0
        for fl in ff.readlines():
            fd = fl.split(delim)
            fd = [ t.strip() for t in fd]
            s.add( fd[field - 1])
            count += 1
        ff.close()
        return s, count

    def get_delim(self, fn):
        if self.opts.delim is not None:
            return self.opts.delim
        delim = self.default_delim
        if len(fn < 3 ):
            if self.opts.file1[-4:] == '.csv':
                delim = ','
            elif self.opts.file1[-4:] == '.tsv':
                delim = '\t'
        return delim

    def run(self):
        print "run"

        a, acount = self.to_set(self.opts.file1, self.opts.f1)
        b, bcount = self.to_set(self.opts.file2, self.opts.f2)

        print "A:", self.opts.file1, len(a), "from", acount, "lines"
        print "B:", self.opts.file2, len(b), "from", bcount, "lines"

        sd  = a ^ b
        if not len(sd):
            print "sets are equal"
            sys.exit(0)

        print "Union:", len(a | b)
        print "Intersection:", len(a & b)
        if a.issubset(b):
            print "A is contained in B"
        else:
            print "In A not in B:", len(a-b)
        if a.issuperset(b):
            print "B is contained in A"
        else:
            print "In B not in A:", len(b-a)



if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="compute set operations")
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-d', '--delim', default='\t')
    parser.add_argument('--f1', default=1)
    parser.add_argument('--f2', default=1)
    parser.add_argument("file1")
    parser.add_argument("file2")
    opts = parser.parse_args()


    so = SetOps(opts)
    so.run()