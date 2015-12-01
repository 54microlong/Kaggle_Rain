__author__ = 'chenlong'

import sys

class ML_Raining():

    def __init__(self, inp, out='../data/sample.result'):
        self.inp = open(inp, 'r')
        self.out = open(out, 'w')

    def Marshall_palmer(self, ref, minutes_past):

        #print "Estimating rainfall from {0} observations".format(len(minutes_past))
        # how long is each observation valid?
        valid_time = [0 for _ in xrange(len(minutes_past))]
        valid_time[0] = float(minutes_past[0])
        for n in xrange(1, len(minutes_past)):
            valid_time[n] = float(minutes_past[n]) - float(minutes_past[n-1])
        valid_time[-1] = valid_time[-1] + 60 - sum(valid_time)
        valid_time = [item/60.0 for item in valid_time]

        # sum up rainrate * validtime
        su = 0
        for dbz, hours in zip(ref, valid_time):
            # See: https://en.wikipedia.org/wiki/DBZ_(meteorology)
            if dbz and dbz not in ['NaN', 'nan', '', ' ']:
                mmperhr = pow(pow(10, float(dbz)/10.0)/200.0, 0.625)
                su = su + mmperhr * hours
        return su


    def ProcessSample(self, sample):
        sorted(sample, key=lambda x: x[1])
        ref = [item[3] for item in sample]
        minutes_past = [item[1] for item in sample]
        est = self.Marshall_palmer(ref, minutes_past)
        return est

    def Processing(self):
        pre = 0
        samples = []
        lineNum = 0
        for line in self.inp:
            lineNum += 1
            if lineNum % 100000 == 0:
                sys.stderr.write('Processing => ' + str(lineNum) + ' lines...\n')
            cur = line.strip().split(',')[0]
            # Filter head line 
            if not cur.isdigit():
                # This line is for debug
                #sys.stderr.write('[Warn] Format error => ' + line + '\n')
                continue
            if cur != pre and len(samples) > 0:
                # new sample
                res = self.ProcessSample(samples)
                
                # Output Result
                self.out.write(cur + ' ' + str(res) + '\n')

                samples = []
                samples.append(line.strip().split(','))
            else:
                samples.append(line.strip().split(','))
            pre = cur


if __name__ == "__main__":
    # Input file path
    
    rain = ML_Raining("../data/train_1w.csv")
    if len(sys.argv) > 1:
        if sys.argv[1]: rain.inp = open(sys.argv[1], 'r')
    else:
        sys.stderr.write('Usage =>  python SampleDask.py [inputFile] \n')   
    sys.stderr.write("Output => output file are located in '../data/sample.result' \n")   
    rain.Processing()
