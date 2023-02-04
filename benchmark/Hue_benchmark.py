

import sys
sys.path.append('')
import time
import os
from logparser import Hue
from logparser.utils.utils import *

traditional_logs = ['HDFS', 'Spark', 'BGL', 'Windows', 'Linux', 'Andriod', 'Mac', 'Hadoop', 'HealthApp', 'OpenSSH', 'Thunderbird', 'Proxifier', 'Apache', 'HPC', 'Zookeeper', 'OpenStack']
hybrid_logs = ['HiBench', 'CTS']


feedback = False # whether to enable feedback query
analysis = False # whether to analysis for all templates

feedback_target = 'Linux' # choose a dataset for feedback experiment

acclist = []
meanacc = 0
meanf1 = 0

begintime = time.time()
for logs in traditional_logs:

    #debug
    if feedback and logs != feedback_target:
        continue

    print("Parsing log dataset: {}".format(logs))

    idir = 'logs/' + logs +'/'
    odir = 'results/Hue_result/' + logs + '/'

    parser = Hue.Parser(idir, odir, config=idir + 'config.yml',feedback=feedback)
    parser.parse(logs + '_2k.log')
    parser.print()

    gt = idir + logs + '_2k.log_structured_alter.log'
    pd = odir + 'meta.log'
    ans = evaluate(gt, pd, analysis=analysis)
    meanacc += ans[0]
    meanf1 += ans[3]
    acclist.append("Dataset: {}\tAccuracy: {:.4f}\tRecall: {:.4f}\tPrecision: {:.4f}\tF1-Score: {:.4f}".format(logs, ans[0], ans[1], ans[2], ans[3]))

for logs in hybrid_logs:

    #debug
    if feedback and logs != feedback_target:
        continue

    print("Parsing log dataset: {}".format(logs))

    idir = 'logs/' + logs +'/'
    odir = 'results/Hue_result/' + logs + '/'

    parser = Hue.Parser(idir, odir, config=idir + 'config.yml',feedback=feedback)
    parser.parse(logs + '_4k_alter.log')
    parser.print()

    gt = idir + logs + '_4k.log_structured_alter.log'
    pd = odir + 'meta.log'

    ans = evaluate(gt, pd, analysis=analysis)
    meanacc += ans[0]
    meanf1 += ans[3]
    acclist.append("Dataset: {}\tAccuracy: {:.4f}\tRecall: {:.4f}\tPrecision: {:.4f}\tF1-Score: {:.4f}".format(logs, ans[0], ans[1], ans[2], ans[3]))

endtime = time.time()
print("Total time = {}s".format(endtime-begintime))

for acc in acclist:
    print(acc)
