# README

## !!!Declarition

T**he algorithm implementation of Hue is in `logparser/Hue/Hue.py`,** 

If you want to ***re-run*** the parser for all log files and ***re-produce*** all accuracy results in the paper, just run `python benchmark/Hue_benchmark.py`. It is not only output the accuracy of parsed log files, but also parse all log files each time.

You can also delete the `results` directory and re-run the benchmark files to get new parsed files.

## Directory

- benchmark: the **program entries** for each parser
- logparser: the **algorithm implementation** for each parser
- logs: all log files and their labels, including **16** LogPAI single-line datasets, and **2** open-accessed hybrid log datasets.

## Environment

- Python 3.9
- Libs:
  - yaml
  - hashlib
  - numpy
  - matplotlib
  - pandas
  - tqdm

Run:

```python
pip install xxx # xxx is the name of libs
```

for setting up the environments.

## Tutorial

1. All implementations of the parser (except Hue), logs (except HiBench and CTS), and tools are from LogPAI (https://github.com/logpai).
2. We offer reproduction of the following experiments：
   1. Experiments on parser accuracy in RQ1 and RQ2.
   2. Experiments on Hue's feedback mechanism in RQ3.
3. We also provide the source code for generating figures in paper.
4. We do not offer experiments on SPINE because SPINE is not yet open source.
5. We do not provide reproduction of the experiment about execution time. This is because the experiment requires a large number of logs, which are difficult to upload to the support material.  And the results vary considerably from one device to another.

## Reproduction

To reproduce the experiment, you first need to go to the "artifact" path.

```shell
cd artifact
```

### 1. Accuracy in RQ1&RQ2

just run these command for all parsers:

```shell
python benchmark/AEL_benchmark.py
python benchmark/Lenma_benchmark.py
python benchmark/Spell_benchmark.py
python benchmark/IPLoM_benchmark.py
python benchmark/Drain_benchmark.py
python benchmark/Hue_benchmark.py
```

and you will get the results like these:

- Hue's results format:

```
Dataset: HDFS   Accuracy: 0.9975        Recall: 0.9286  Precision: 0.8125       F1-Score: 0.8667
Dataset: Spark  Accuracy: 0.9415        Recall: 0.8333  Precision: 0.9091       F1-Score: 0.8696
Dataset: BGL    Accuracy: 0.8490        Recall: 0.8167  Precision: 0.6125       F1-Score: 0.7000
Dataset: Windows        Accuracy: 0.9900        Recall: 0.9000  Precision: 0.7377       F1-Score: 0.8108
Dataset: Linux  Accuracy: 0.3560        Recall: 0.9068  Precision: 0.9469       F1-Score: 0.9264
Dataset: Andriod        Accuracy: 0.8260        Recall: 0.8614  Precision: 0.8079       F1-Score: 0.8338
Dataset: Mac    Accuracy: 0.9005        Recall: 0.9150  Precision: 0.8571       F1-Score: 0.8851
Dataset: Hadoop Accuracy: 0.9655        Recall: 0.8333  Precision: 0.9314       F1-Score: 0.8796
Dataset: HealthApp      Accuracy: 0.9025        Recall: 0.9467  Precision: 0.9726       F1-Score: 0.9595
Dataset: OpenSSH        Accuracy: 0.8040        Recall: 0.8519  Precision: 0.6970      F1-Score: 0.7667
Dataset: Thunderbird    Accuracy: 0.9620        Recall: 0.8523  Precision: 0.7175       F1-Score: 0.7791
Dataset: Proxifier      Accuracy: 1.0000        Recall: 1.0000  Precision: 1.0000       F1-Score: 1.0000
Dataset: Apache Accuracy: 1.0000        Recall: 1.0000  Precision: 1.0000       F1-Score: 1.0000
Dataset: HPC    Accuracy: 0.9505        Recall: 0.8913  Precision: 0.8542       F1-Score: 0.8723
Dataset: Zookeeper      Accuracy: 0.9865        Recall: 0.8200  Precision: 0.8913       F1-Score: 0.8542
Dataset: OpenStack      Accuracy: 0.9925        Recall: 0.9767  Precision: 0.9767       F1-Score: 0.9767
Dataset: HiBench        Accuracy: 0.9320        Recall: 0.8584  Precision: 0.8151       F1-Score: 0.8362
Dataset: CTS    Accuracy: 0.8482        Recall: 0.8865  Precision: 0.7962       F1-Score: 0.8389
```

- other parsers' results: (for example, Drain)

```
             Accuracy  Precision    Recall  F1_measure
Dataset
HDFS         0.997500   0.812500  0.928571    0.866667
Hadoop       0.947500   0.864078  0.780702    0.820276
Spark        0.920000   0.862069  0.694444    0.769231
Zookeeper    0.966500   0.891304  0.820000    0.854167
BGL          0.962500   0.879630  0.791667    0.833333
HPC          0.887000   0.744681  0.760870    0.752688
Thunderbird  0.955000   0.703297  0.859060    0.773414
Windows      0.997000   0.905660  0.960000    0.932039
Linux        0.690000   0.955357  0.906780    0.930435
Andriod      0.911000   0.812865  0.837349    0.824926
HealthApp    0.780000   0.217949  0.906667    0.351421
Apache       1.000000   1.000000  1.000000    1.000000
Proxifier    0.526500   0.388889  0.875000    0.538462
OpenSSH      0.787500   0.875000  0.777778    0.823529
OpenStack    0.732500   0.066890  0.465116    0.116959
Mac          0.786500   0.743655  0.859238    0.797279
HiBench      0.442000   0.714286  0.796460    0.753138
CTS          0.746073   0.781690  0.787234    0.784452
```

**The top 16 datasets are single row log datasets, while the last two datasets are open source hybrid log datasets.**

### 2. Feedback in RQ3

Before starting, you need to change some settings first:

1. You need to open "Hue.py" in the directory "logparser/Hue" first:

   ```
   vim logparser/Hue/Hue.py
   ```
2. Adjust the feedback switch on line **14** from "False" to "True".

   From:

   ```python
   feedback = False # whether to enable feedback query
   ```

   To:

   ```python
   feedback = True # whether to enable feedback query
   ```
3. Change the feedback_target in line **17** to the dataset you want to reproduce

   ```python
   feedback_target = 'Linux' # choose a dataset for feedback experiment
   ```
4. Re-run the benchmark script:

   ```python
   python benchmark/Hue_benchmark.py
   ```

You can then interact with the command line to guide the parser through feedback.

Specifically, each time you enter "Enter" or "y", you will accept the merge, while entering 'n' means you reject the merge.

The following is an example of the feedback results for Linux. You need to enter 'n' at the **3rd, 6th, 7th, 10th** feedback query and just enter "Enter" at other queries:

```shell
Parsing log dataset: Linux

Old S_T:        session opened for user cyrus by (uid<?><*>)
New S_ID:       session opened for user news by (uid<?><*>)
Are they belong to the same template? [y] or n.

S_T merged to:  session opened for user <*> by (uid<?><*it>)
17it [00:03,  5.20it/s]
Old S_T:        session closed for user cyrus
New S_ID:       session closed for user news
Are they belong to the same template? [y] or n.

S_T merged to:  session closed for user <*>
18it [00:03,  5.06it/s]
Old S_T:        authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>root
New S_ID:       authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>guest
Are they belong to the same template? [y] or n.
n
91it [00:03,  7.12it/s]
Old S_T:        connection from <*> <*> at Fri Jun <*> <*>:<*>:<*> <*>
New S_ID:       connection from <*> <*> at Sat Jun <*> <*>:<*>:<*> <*>
Are they belong to the same template? [y] or n.

S_T merged to:  connection from <*ul> <*ul> at <*> Jun <*it> <*it>:<*it>:<*it> <*it>
121it [00:04,  9.54it/s]
Old S_T:        connection from <*> <*> at <*> <*>:<*>:<*> <*>
New S_ID:       connection from <*> () at Fri Jul <*> <*>:<*>:<*> <*>
Are they belong to the same template? [y] or n.

S_T merged to:  connection from <*ul> <*> at <*> <*> <*it> <*it>:<*it>:<*it> <*it>
628it [00:04, 13.61it/s]
Old S_T:        session opened for user <*><*>)
New S_ID:       session opened for user root by LOGIN(uid<?><*>)
Are they belong to the same template? [y] or n.
n
898it [00:06, 18.86it/s]
Old S_T:        authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>guest
New S_ID:       authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>test
Are they belong to the same template? [y] or n.
n
1675it [00:06, 35.87it/s]
Old S_T:        <*>: <*> <?> 00000000000a0000 (usable)
New S_ID:       <*>: <*> <?> 0000000007eae000 (usable)
Are they belong to the same template? [y] or n.

S_T merged to:  <*ul>: <*it> <?> <*> (usable)

Old S_T:        <*>: 00000000000f0000 <?> <*> (reserved)
New S_ID:       <*>: 0000000007eae000 <?> <*> (reserved)
Are they belong to the same template? [y] or n.

S_T merged to:  <*ul>: <*> <?> <*it> (reserved)
1923it [00:07, 48.31it/s]
Old S_T:        usbcore: registered new driver usbfs
New S_ID:       usbcore: registered new driver hub
Are they belong to the same template? [y] or n.
n

Old S_T:        <*> hash table entries: <*> (order: <*>, <*> bytes)
New S_ID:       <*> hash table entries: <*> (order <*>, <*> bytes)
Are they belong to the same template? [y] or n.

S_T merged to:  <*ul> hash table entries: <*it> <*> <*it>, <*it> bytes)


Total time = 8.948465347290039s
Dataset: Linux  Accuracy: 0.9975        Recall: 0.9576  Precision: 0.9826       F1-Score: 0.9700
```

If you give all the correct feedback, then the final Grouping Accuracy will be 0.9975. However, you can also give only some of the partial feedback. For example, in the example above, you could give guidance until the **3rd** feedback and then enter all the spaces after it. This would give you the following result：

```
Old S_T:        session opened for user cyrus by (uid<?><*>)
New S_ID:       session opened for user news by (uid<?><*>)
Are they belong to the same template? [y] or n.

S_T merged to:  session opened for user <*> by (uid<?><*it>)
17it [00:01,  9.97it/s]
Old S_T:        session closed for user cyrus
New S_ID:       session closed for user news
Are they belong to the same template? [y] or n.

S_T merged to:  session closed for user <*>
18it [00:02,  5.92it/s]
Old S_T:        authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>root
New S_ID:       authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>guest
Are they belong to the same template? [y] or n.
n
91it [00:03,  8.00it/s]
Old S_T:        connection from <*> <*> at Fri Jun <*> <*>:<*>:<*> <*>
New S_ID:       connection from <*> <*> at Sat Jun <*> <*>:<*>:<*> <*>
Are they belong to the same template? [y] or n.

S_T merged to:  connection from <*ul> <*ul> at <*> Jun <*it> <*it>:<*it>:<*it> <*it>
121it [00:04, 10.87it/s]
Old S_T:        connection from <*> <*> at <*> <*>:<*>:<*> <*>
New S_ID:       connection from <*> () at Fri Jul <*> <*>:<*>:<*> <*>
Are they belong to the same template? [y] or n.

S_T merged to:  connection from <*ul> <*> at <*> <*> <*it> <*it>:<*it>:<*it> <*it>
628it [00:04, 15.51it/s]
Old S_T:        session opened for user <*><*>)
New S_ID:       session opened for user root by LOGIN(uid<?><*>)
Are they belong to the same template? [y] or n.

S_T merged to:  session opened for user <*> by <*>
898it [00:04, 22.08it/s]
Old S_T:        authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>guest
New S_ID:       authentication failure; logname<?> uid<?><*> euid<?><*> tty<?>NODEVssh ruser<?> <*> user<?>test
Are they belong to the same template? [y] or n.

S_T merged to:  authentication failure; logname<?> uid<?><*it> euid<?><*it> tty<?>NODEVssh ruser<?> <*ul> <*>
1733it [00:04, 44.40it/s]
Old S_T:        <*>: <*> <?> 00000000000a0000 (usable)
New S_ID:       <*>: <*> <?> 0000000007eae000 (usable)
Are they belong to the same template? [y] or n.

S_T merged to:  <*ul>: <*it> <?> <*> (usable)

Old S_T:        <*>: 00000000000f0000 <?> <*> (reserved)
New S_ID:       <*>: 0000000007eae000 <?> <*> (reserved)
Are they belong to the same template? [y] or n.

S_T merged to:  <*ul>: <*> <?> <*it> (reserved)

Old S_T:        usbcore: registered new driver usbfs
New S_ID:       usbcore: registered new driver hub
Are they belong to the same template? [y] or n.
S_T merged to:  usbcore: registered new driver <*>

Old S_T:        <*> hash table entries: <*> (order: <*>, <*> bytes)
New S_ID:       <*> hash table entries: <*> (order <*>, <*> bytes)
Are they belong to the same template? [y] or n.

S_T merged to:  <*ul> hash table entries: <*it> <*> <*it>, <*it> bytes)

Dataset: Linux  Accuracy: 0.9245        Recall: 0.9068  Precision: 0.9554       F1-Score: 0.9304
```

The results of **Fig. 10 (a)** in the paper can be obtained by stopping the feedback after the **3rd, 6th and 7th** feedback respectively (i.e. by using the input "Enter" instead for all of them).

For other datasets, all the results of Fig.9, Fig.10 can be reproduced by entering **'n'** in the **x-th** feedback as below and 'Enter' elsewhere. The accuracy results should be as follows

```
Linux:
x = [0, 3, 6, 7, 10]
ga = [0.7490, 0.9245, 0.9860, 0.9965, 0.9975]
f1 = [0.9258, 0.9304, 0.9437, 0.9569, 0.9700]

Android:
x = [0, 3, 4, 5, 6, 7, 8, 9, 11, 15, 17, 19]
ga = [0.7860, 0.8710, 0.8780, 0.9105, 0.9165, 0.9185, 0.9195, 0.9255, 0.9285, 0.9310, 0.9340, 0.9370]
f1 = [0.7975, 0.8075, 0.8173, 0.8272, 0.8369, 0.8466, 0.8563, 0.8659, 0.8754, 0.8848, 0.8943, 0.9036]

BGL:
x = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]
ga = [0.5545, 0.5690, 0.5730, 0.5755, 0.5760, 0.9365, 0.9395, 0.9405, 0.9440, 0.9495, 0.9515, 0.9530, 0.9560, 0.9565, 0.9575, 0.9585]
f1 = [0.7306, 0.7455, 0.7511, 0.7568, 0.7623, 0.7679, 0.7733, 0.7788, 0.7930, 0.8070, 0.8210, 0.8348, 0.8485, 0.8534, 0.8670, 0.8803]

HiBench:
x = [0, 1, 3, 13, 17]
ga = [0.9320, 0.9477, 0.9590, 0.9600, 0.9605]
f1 = [0.8362, 0.8684, 0.8821, 0.8957, 0.9091]

CTS:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
ga = [0.6675, 0.6780, 0.6885, 0.6937, 0.6990, 0.7120, 0.7356, 0.7408, 0.7461, 0.7513, 0.7565, 0.7618, 0.7670, 0.7723, 0.7827, 0.7880, 0.7932, 0.7984, 0.8089, 0.8246, 0.8403, 0.8534, 0.8639]
f1 = [0.7399, 0.7445, 0.7491, 0.7536, 0.7581, 0.7626, 0.7670, 0.7714, 0.7758, 0.7801, 0.7845, 0.7887, 0.7930, 0.7972, 0.8014, 0.8056, 0.8097, 0.8138, 0.8179, 0.8288, 0.8396, 0.8503, 0.8610]
```

You can also check template corresponding to all datasets from the **'log/'** directory and provide feedback according to your preferences.

### Figures

just run the 'draw.py' for all results.

```
python draw.py
```
