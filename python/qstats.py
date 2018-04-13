import sys
import numpy as np


class QStats:

    def __init__(self, opts):
        self.opts = opts

    def run(self):

        data = []

        if self.opts.file == "-":

            for line in sys.stdin:
                if self.opts.skip:
                    self.opts.skip = False
                    continue
                else:
                    dline = [d.strip() for d in line.split(self.opts.delim)]
                    data.append(float(dline[int(self.opts.field)]))

        else:
            ff = open( self.opts.file, "r")

            for line in ff.readlines():
                if self.opts.skip:
                    self.opts.skip = False
                    continue
                else:
                    dline = [d.strip() for d in line.split(self.opts.delim)]
                    data.append(float(dline[int(self.opts.field)]))


        data = np.array(data)

        if not self.opts.verbose:
            print "AVG", data.mean(0), "MED", np.median(data), "STD", data.std(), \
                "MIN", data.min(), "MAX", data.max(), "COUNT", data.size



if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="compute first order statistics")
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d', '--delim', default='\t')
    parser.add_argument('-f', '--field', default=1)
    parser.add_argument('-s', '--skip', action='store_false', default=True)
    parser.add_argument("file")
    opts = parser.parse_args()

    so = QStats(opts)
    so.run()