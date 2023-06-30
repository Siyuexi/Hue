import sys
sys.path.append('')
from logparser import Logram
from logparser.utils import evaluatorL
import pandas as pd
import os



benchmark_settings = {
    'HDFS': {
        'log_file': 'HDFS/HDFS_2k.log',
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'],
        't2': 15,
        't3': 15
        },

    'Hadoop': {
        'log_file': 'Hadoop/Hadoop_2k.log',
        'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>', 
        'regex': [r'(\d+\.){3}\d+'],
        't2': 9,
        't3': 6       
        },

    'Spark': {
        'log_file': 'Spark/Spark_2k.log',
        'log_format': '<Date> <Time> <Level> <Component>: <Content>', 
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
        't2': 37,
        't3': 37
        },

    'Zookeeper': {
        'log_file': 'Zookeeper/Zookeeper_2k.log',
        'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
        'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?'],
        't2': 9,
        't3': 9 
        },

    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'regex': [r'core\.\d+'],
        't2': 18,
        't3': 10 
        },

    'HPC': {
        'log_file': 'HPC/HPC_2k.log',
        'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
        'regex': [r'=\d+'],
        't2': 13,
        't3': 11
        },

    'Thunderbird': {
        'log_file': 'Thunderbird/Thunderbird_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        't2': 8,
        't3': 7    
        },

    'Windows': {
        'log_file': 'Windows/Windows_2k.log',
        'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
        'regex': [r'0x.*?\s'],
        't2': 16,
        't3': 16     
        },

    'Linux': {
        'log_file': 'Linux/Linux_2k.log',
        'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'],
        't2': 32,
        't3': 24     
        },

    'Andriod': {
        'log_file': 'Andriod/Andriod_2k.log',
        'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
        'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b'],
        't2': 14,
        't3': 13 
        },

    'HealthApp': {
        'log_file': 'HealthApp/HealthApp_2k.log',
        'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'],
        't2': 23,
        't3': 5
        },

    'Apache': {
        'log_file': 'Apache/Apache_2k.log',
        'log_format': '\[<Time>\] \[<Level>\] <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        't2': 75,
        't3': 32     
        },

    'Proxifier': {
        'log_file': 'Proxifier/Proxifier_2k.log',
        'log_format': '\[<Time>\] <Program> - <Content>',
        'regex': [r'<\d+\ssec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
        't2': 115,
        't3': 95
        },

    'OpenSSH': {
        'log_file': 'OpenSSH/OpenSSH_2k.log',
        'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+'],
        't2': 47,
        't3': 80 
        },

    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
        't2': 16,
        't3': 9
        },

    'Mac': {
        'log_file': 'Mac/Mac_2k.log',
        'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
        'regex': [r'([\w-]+\.){2,}[\w-]+'],
        't2': 11,
        't3': 10
        },
    'HiBench': {
        'log_file': 'HiBench/HiBench_4k.log',
        'log_format': '\[<Time>\] <Content>', 
        'regex': [r'(([A-Z]:)|)(/\S+)+', r'(\S+\.\S+(\.\S+)+(:\d+)?)|(\w+-\w+(-\w+)+)', r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', r'(0x.*?\s)|(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', r'(=*|)(True)|(False)|(true)|(false)', r'[-\+\=\|]+'],
        't2': 35,
        't3': 35
        },

    'CTS': {
        'log_file': 'CTS/CTS_4k.log',
        'log_format': '\[<ThreadID>\]\[<User>\] <Content>', 
        'regex': [r'(([A-Z]:)|)(/\S+)+', r'(\S+\.\S+(\.\S+)+(:\d+)?)|(\w+-\w+(-\w+)+)', r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', r'(0x.*?\s)|(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', r'(=*|)(True)|(False)|(true)|(false)', r'[-\+\=\|]+'],
        't2': 5,
        't3': 2,
        },
}

meanacc = 0
meanf1 = 0
bechmark_result = []
import time
begintime = time.time()
for dataset, setting in benchmark_settings.items():
    doubleDictionaryList, triDictionaryList, allTokenList = Logram.dictionaryBuilder(setting['log_format'], f"logs/{setting['log_file']}", setting['regex'])
    if not os.path.exists(f'results/Logram_result'):
        os.makedirs(f'results/Logram_result')
    Logram.tokenMatch(allTokenList,doubleDictionaryList,triDictionaryList,setting['t2'],setting['t3'],f'results/Logram_result/{dataset}_event.txt')
    if dataset == 'HiBench' or dataset == 'CTS':
        accuracy, precision, recall, F1_measure = evaluatorL.evaluate(f'logs/{dataset}/{dataset}_4k.log_structured_alter.log', f'results/Logram_result/{dataset}_event.txt')
    else:
        accuracy, precision, recall, F1_measure = evaluatorL.evaluate(f'logs/{dataset}/{dataset}_2k.log_structured_alter.log', f'results/Logram_result/{dataset}_event.txt')

    bechmark_result.append([dataset, accuracy, precision, recall, F1_measure])
    meanacc += accuracy
    meanf1 += F1_measure
print("mean accuracy = {}".format(meanacc/len(benchmark_settings)))
print("mean F1-measure = {}".format(meanf1/len(benchmark_settings)))
endtime = time.time()
print("total time = {}s".format(endtime-begintime))

print('\n=== Overall evaluation results ===')
df_result = pd.DataFrame(bechmark_result, columns=['Dataset', 'Accuracy', 'Precision', 'Recall', 'F1_measure'])
df_result.set_index('Dataset', inplace=True)
print(df_result)
