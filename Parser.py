"""
Description : A hybrid log parser
Author      : Siyuexi
"""
import os
import re
import yaml
import time
import hashlib
from tqdm import tqdm

class Parser:
    def __init__(self, idir='./', odir='./', config='config.yml'):
        self.idir = idir
        self.odir = odir
        self.config = yaml.load(open(config), Loader=yaml.SafeLoader)

        self.max_length = self.config['max_length']
        self.max_depth = self.config['max_depth']
        self.max_child = self.config['max_child']
        self.t_extract = self.config['t_extract']
        self.t_aggregate = self.config['t_aggregate']
        self.regex = self.config['regex']

    def __sim(self, s1, s2):
        
        l = min((len(s1), len(s2)))
        k = 0
        for i in range(l):
            if s1[i] == s2[i]:
                k += 1
        return k / l

    def __find(self, s1, s2, f): # f=True: find same elements; f=False: find different elements
        l = min((len(s1), len(s2)))
        seq = []
        if f:
            for i in range(l):
                if s1[i] == s2[i]:
                    seq.append(s1[i])
        else:
            for i in range(l):
                if s1[i] != s2[i]:
                    seq.append(s1[i])
        return seq

    def __match(self, seq, group):

        maxsim = self.t_extract
        maxtid = None
        for tid in group.dict.keys():
            templ = group.dict[tid]
            sim = self.__sim(seq, templ)
            if sim >= maxsim:
                maxsim = sim
                maxtid = tid
        return maxtid

    def __flush(self, msg):
        if msg is not None:
            if msg.type == 's':
                ttype = self.single
            elif msg.type == 'm':
                ttype = self.multiple
            else:
                ttype = self.table

                for i in range(1, len(msg.lines)): # recorrect table message's template
                    if len(msg.lines[i]) > 1:
                        msg.template = re.sub(self.regex[0]['re'],'',msg.lines[i-1][0]).split() # get rid of timestamp (if any)
                        break

            if msg.tid not in ttype.dict.keys():
                ttype.dict[msg.tid] = Class()
                ttype.num += 1
                ttype.dict[msg.tid].symbol = msg.type + str(ttype.num)
            cls = ttype.dict[msg.tid]
            cls.list.append((msg.idx, msg.lines)) 
            cls.template = msg.template # always keep template updated

            self.meta.list.append(cls.symbol + ', ' + str(msg.idx) + ', ' + ' '.join(cls.template))
            self.meta.num += 1
        return Msg()

    def parse(self, logname):
        begintime = time.time()
        self.logpath = self.idir + logname
        self.log = open(self.logpath, 'r')

        self.root = Node() # initialate root node
        self.root.child['*'] = Group() # initialate rubbish bucket
        self.single = Type()
        self.multiple = Type()
        self.table = Type()
        self.meta = Meta()

        msg = None
        lastseq = []
        lines = self.log.readlines() 
        for idx, line in tqdm(enumerate(lines)):

            node = self.root
            mf = True # match flag
            nf = False # new msg flag

            """ 
                preprocess line key
            """
            tline = line
            for r in self.regex:
                tline = re.sub(r['re'], r['symbol'], tline) # tokenization line
            kseq = re.findall(r'<\*.+?>', tline) # key sequence
            tseq = tline.split() # token sequence
            pseq = [token for token in tseq if token not in kseq] # prefix sequence

            if tseq == []: # skip the space line
                continue
            if tseq[0] == '<!>': # if this line is a new message's first line, then flush the old message to its Type
                # get rid of timestamp
                tseq = tseq[1 :] 
                kseq = kseq[1 :]
                pseq = pseq[1 :]
                nf = True
            tlen = len(tseq)
            klen = len(kseq)
            if tseq == ['<?>']: # skip the splitter
                continue
            """
                extract line-pattern or aggregate lines
            """
            if nf: # if it is a new line, then extract line pattern
                if tlen > self.max_length: # lost match : too long token length
                    mf = False
                else:
                    # match by token length
                    if str(tlen) not in node.child.keys(): 
                        node.child[str(tlen)] = Node(2)
                    node = node.child[str(tlen)]

                    # match by key length
                    if str(klen) not in node.child.keys():
                        node.child[str(klen)] = Node(3)
                    node = node.child[str(klen)]

                    # search in order of layers 
                    maxdepth = min(self.max_depth, tlen) # for some sentence, it is too short for self.max_depth tree parsing
                    l2d = min(maxdepth, klen)
                    l3d = maxdepth - l2d
                    for depth in range(4, 4+l2d):
                        key = kseq[depth - 4]
                        if key not in node.child.keys():
                            node.child[key] = Node(depth)
                        node = node.child[key]
                    for depth in range(4+l2d, 4+l2d+l3d): 
                        prefix = pseq[depth - 4 - l2d]
                        if prefix not in node.child.keys():
                            if len(node.child.keys()) > self.max_child: # lost match: too many children
                                mf = False
                                break
                            node.child[prefix] = Node(depth)
                        node = node.child[prefix]
                if not mf: # if failed in matching group (because > max_length or > max_child)
                    group = self.root.child['*']
                else: 
                    if len(node.child.keys()) == 0:
                        node.child['*'] = Group()
                    group = node.child['*']
                tid = self.__match(tseq, group)

                if tid is None: # if failed in matching template (because < et or group is empty)
                    tid = hashlib.md5(line.encode('utf-8')).hexdigest()[0:8] # hash to get a new tid
                    group.dict[tid] = tseq
                    group.num += 1
                else: # update template
                    templ = group.dict[tid]
                    for i in range(len(templ)):
                        if templ[i] != tseq[i]:
                            templ[i] = '<*>'
                    group.dict[tid] = templ

                # flush the last message
                msg = self.__flush(msg) 
                msg.idx = idx + 1
                msg.lines.append([line])
                msg.template = group.dict[tid]
                msg.tid = tid
                

            else: # if this line is a inter-line (because it has a timestamp ahead)
                if msg.type == 's':
                    msg.type = 'm'
                if self.__sim(tseq, lastseq) >= self.t_aggregate: # if it can be aggregate, then put them together
                    if line[0] != '\t' and line[0] != ' ': # if it is table message
                        msg.type = 't'
                    msg.lines[-1].append(line)  
                else: # or split them
                    msg.lines.append([line])

            lastseq = tseq

        self.__flush(msg) # last flush
        print("Parsing Done.")
        endtime = time.time()
        print("Parsing running time = {}s".format(endtime-begintime))

    # use the structure to output a parsed log file
    
    def print(self):

        """
            print meta file
        """
        print("Building meta file...")
        f = open(self.odir + "meta.log",'w')
        for item in self.meta.list:
            if item[0] == 't': # if it is a table message, then get rid of splitter output (if any)
               item = re.sub('\|','',item) 
            f.write(item + '\n')
        f.close()

        """
            build directories
        """
        if not os.path.exists(self.odir + "single"):
            os.makedirs(self.odir + "single")
        if not os.path.exists(self.odir + "multiple"):
            os.makedirs(self.odir + "multiple")
        if not os.path.exists(self.odir + "table"):
            os.makedirs(self.odir + "table")

        """
            print parsed log files
        """

        # single line log
        print("Building single line log files...")
        for tid in tqdm(self.single.dict.keys()):
            cls = self.single.dict[tid]
            templseq = cls.template
            templstr = " ".join(cls.template)
            f = open(self.odir + "single/" + cls.symbol + '.log', 'w')
            f.write("symbol: " + cls.symbol + '\n')
            f.write("template: " + templstr + '\n')
            f.write("tid: " + str(tid) + '\n')
            for (idx, msg) in cls.list:
                line = msg[0][0]
                seq = line.split()[1:] # get rid of timestamp
                paramlist = self.__find(seq, templseq, False)
                f.write(str(idx) + ",")
                for p in paramlist:
                    f.write(p + ",")
                f.write('\n')
            f.close()
        
        # multiple line log
        print("Building multiple line log files...")
        for tid in tqdm(self.multiple.dict.keys()):
            cls = self.multiple.dict[tid]
            templseq = cls.template
            templstr = " ".join(cls.template)
            f = open(self.odir + "multiple/" + cls.symbol + '.log', 'w')
            f.write("symbol: " + cls.symbol + '\n')
            f.write("template: " + templstr + '\n')
            f.write("tid: " + str(tid) + '\n')
            for (idx, msg) in cls.list:
                line = msg[0][0]
                seq = line.split()[1:] # get rid of timestamp
                paramlist = self.__find(seq, templseq, False)
                f.write(str(idx) + ",")
                for p in paramlist:
                    f.write(p + ",")
                f.write('\n')
                for lines in msg[1:]:
                    if len(lines) == 1:
                        line = lines[0]
                        f.write('||' + line)
                    else:
                        for line in lines:
                            f.write('|>' + line)
            f.close()

        # table format log
        print("Building table format log files...")
        begintime = time.time()
        for tid in tqdm(self.table.dict.keys()):
            cls = self.table.dict[tid]
            templseq = cls.template
            templstr = re.sub('\|',''," ".join(templseq))
            if '|' in templseq:
                sf = True # splitter flag : depends on wether splitter in template
            else:
                sf = False
            f = open(self.odir + "table/" + cls.symbol + '.log', 'w')
            f.write("symbol: " + cls.symbol + '\n')
            f.write("template: " + templstr + '\n')
            f.write("tid: " + str(tid) + '\n')
            for(idx, msg) in cls.list:
                f.write(str(idx) + "," + '\n')
                for lines in msg:
                    if len(lines) > 1: # only output those table information, ignore those "help" information(in single line format)
                        for line in lines:
                            seq = line.split()
                            paramlist = []
                            if sf:
                                elemlist = []
                                for token in seq:
                                    if token not in templseq:
                                        elemlist.append(token)
                                    elif len(elemlist) != 0: # flush elements to parameter list
                                        
                                        paramlist.append(" ".join(elemlist))
                                        elemlist = []
                                if token not in templseq: # last flush
                                    paramlist.append(" ".join(elemlist))
                            else:
                                for token in seq:
                                    if token not in templseq:
                                        paramlist.append(token)
                            for p in paramlist:
                                f.write(p + ",")
                            f.write('\n')
            f.close()

        print("Printing Done.")
        endtime = time.time()
        print("Printing running time = {}s".format(endtime-begintime))
        
    # show parse tree
    def show(self):
        # Using Queue(FIFO) method to display the parse tree structure
        pass


class Msg:
    def __init__(self):
        self.idx = 0
        self.lines = [] # - lines
        self.type = 's'
        self.template = [] # token list
        self.tid = "" # template id

class Node:
    def __init__(self, depth = 1):
        self.child = {} # key : childNode or prefix : childNode
        self.depth = depth

class Group:
    def __init__(self):
        self.dict = {} # tid: template
        self.num = 0

class Class:
    def __init__(self):
        self.template = [] # template is a sequence (a token list)
        self.list = [] # - msgs
        self.symbol = ""
        self.num = 0

class Type:
    def __init__(self):
        self.dict = {} # tid : class
        self.num = 0

class Meta:
    def __init__(self):
        self.list = [] # "s1, 1"
        self.num = 0