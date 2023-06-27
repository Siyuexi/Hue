import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def update_scale_value(temp, position):
    if np.log(temp / 4000) < 3:
        return "{}K".format(temp / 1000)
    else:
        return "{}M".format(temp / 1000000)

# HiBench /s
Hue = np.array([
    0.7173445224761963,
    6.6099958419799805,
    66.04946208000183,
    610.0830097198486,
])

Drain = np.array([
    2.3951964378356934,
    160.82984113693237,
    16571.922901391983
])

IPLoM = np.array([
    0.7394249439239502,
    6.299373388290405,
    62.41866326332092,
    636.4596939086914,
])

LenMa = np.array([
    1.0296845436096191,
    9.990315198898315,
    103.26927137374878,
    1030.0696482658386,
])

Spell = np.array([
    0.8418087959289551,
    8.058952331542969,
    79.59652876853943,
    837.9946854114532,
])

AEL = np.array([
    1.4362661838531494,
    8.494745254516602,
    75.99238586425781,
    669.6907956600189,
])

x = np.array([4000*10**i for i in range(4)])

plt.axes(xscale='log', yscale='log')
plt.gca().xaxis.set_major_formatter(FuncFormatter(update_scale_value))
plt.xticks(x)
plt.xlabel("Number of log messages")
plt.ylabel("Executing time(sec)")
plt.plot(x, Hue, marker='^',label = 'Hue', markerfacecolor = 'white', markersize='8')
plt.plot(x[:-1], Drain, marker='+',label = 'Drain', markerfacecolor = 'white', markersize='8')
plt.plot(x, IPLoM, marker='v',label = 'IPLoM', markerfacecolor = 'white', markersize='8')
plt.plot(x, LenMa, marker='.',label = 'LenMa', markerfacecolor = 'white', markersize='10')
plt.plot(x, Spell, marker='x',label = 'Spell', markerfacecolor = 'white', markersize='8')
plt.plot(x, AEL, marker='s',label = 'AEL', markerfacecolor = 'white', markersize='6')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# CTS /s
Hue = np.array([
    0.06281495094299316,
    0.5830979347229004,
    5.079625129699707,
    50.037330865859985,
    504.11766719818115
])

Drain = np.array([
    0.053331851959228516,
    0.4530966281890869,
    4.0779664516448975,
    50.723867416381836,
    2457.8618750572205
])

IPLoM = np.array([
    0.11601972579956055,
    0.9911091327667236,
    8.717229843139648,
    84.0777862071991,
    854.2400324344635
])

LenMa = np.array([
    0.10550689697265625,
    1.07523775100708,
    10.46081805229187,
    93.71463131904602,
    952.5543506145477
])

Spell = np.array([
    0.09852075576782227,
    0.90234524168843512,
    5.539639234542847,
    53.079946994781494,
    534.6345660686493
])

AEL = np.array([
    0.069519548416137695,
    0.59260802268981934,
    5.530622720718384,
    54.45802640914917,
    538.81571531295776
])

x = np.array([400*10**i for i in range(5)])

plt.axes(xscale='log', yscale='log')
plt.gca().xaxis.set_major_formatter(FuncFormatter(update_scale_value))
plt.xticks(x)
plt.xlabel("Number of log messages")
plt.ylabel("Executing time(sec)")
plt.plot(x, Hue, marker='^',label = 'Hue', markerfacecolor = 'white', markersize='8')
plt.plot(x, Drain, marker='+',label = 'Drain', markerfacecolor = 'white', markersize='8')
plt.plot(x, IPLoM, marker='v',label = 'IPLoM', markerfacecolor = 'white', markersize='8')
plt.plot(x, LenMa, marker='.',label = 'LenMa', markerfacecolor = 'white', markersize='10')
plt.plot(x, Spell, marker='x',label = 'Spell', markerfacecolor = 'white', markersize='8')
plt.plot(x, AEL, marker='s',label = 'AEL', markerfacecolor = 'white', markersize='6')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# PaaS /s
Hue = np.array([
    0.0824245490410412,
    0.790247864582913,
    7.8853920452014583,
    76.023699405489866,
    750.41058682023868
])

Drain = np.array([
    0.052331851959228516,
    0.5830966281890869,
    6.479664516448975,
    122.723867416381836,
    5121.5432905200239,
])

IPLoM = np.array([
    0.1623149547891042,
    1.6123450058812365,
    15.405681053023951,
    145.9452392319012,
    1322.0246923052317
])

LenMa = np.array([
    0.15692345230065,
    1.83205850293891,
    21.1243034299658,
    249.23543901237,
    2740.29507602578
])

Spell = np.array([
    0.08852075576782227,
    0.8723490542023845,
    8.8239124054991202,
    85.034175034347821,
    837.79034108212755
])

AEL = np.array([
    0.08954371802485523,
    0.87293123954045302,
    8.7023854392199013,
    81.102503491238952,
    802.114532965023991
])

x = np.array([700*10**i for i in range(5)])

plt.axes(xscale='log', yscale='log')
plt.gca().xaxis.set_major_formatter(FuncFormatter(update_scale_value))
plt.xticks(x)
plt.xlabel("Number of log messages")
plt.ylabel("Executing time(sec)")
plt.plot(x, Hue, marker='^',label = 'Hue', markerfacecolor = 'white', markersize='8')
plt.plot(x, Drain, marker='+',label = 'Drain', markerfacecolor = 'white', markersize='8')
plt.plot(x, IPLoM, marker='v',label = 'IPLoM', markerfacecolor = 'white', markersize='8')
plt.plot(x, LenMa, marker='.',label = 'LenMa', markerfacecolor = 'white', markersize='10')
plt.plot(x, Spell, marker='x',label = 'Spell', markerfacecolor = 'white', markersize='8')
plt.plot(x, AEL, marker='s',label = 'AEL', markerfacecolor = 'white', markersize='6')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# HDFS /s
Hue = np.array([
    0.16644573211669922,
    0.9219551086425781,
    9.039134979248047,
    92.46109080314636,
    1048.7018630504608
])

Drain = np.array([
    0.15797662734985352,
    1.3674871921539307,
    12.924535036087036,
    134.80971455574036,
    1714.6522829532623
])

IPLoM = np.array([
    0.1659395694732666,
    1.3044850826263428,
    13.157779455184937,
    137.07380437850952,
    10464.451024055481
])

LenMa = np.array([
    0.4070091247558594,
    4.294086933135986,
    42.29481029510498,
    429.04945397377014,
    4493.907831907272,
])

Spell = np.array([
    0.1879253387451172,
    1.3501505851745605,
    13.955895900726318,
    146.09300875663757,
    1759.6563289165497,
])

AEL = np.array([
    0.14288997650146484,
    0.9508366584777832,
    9.677146911621094,
    103.72887682914734,
    1250.5800619125366,
])

x = np.array([2000*10**i for i in range(5)])
plt.axes(xscale='log', yscale='log')
plt.gca().xaxis.set_major_formatter(FuncFormatter(update_scale_value))
plt.xticks(x) 
plt.xlabel("Number of log messages")
plt.ylabel("Executing time(sec)")
plt.plot(x, Hue, marker='^',label = 'Hue', markerfacecolor = 'white', markersize='8')
plt.plot(x, Drain, marker='+',label = 'Drain', markerfacecolor = 'white', markersize='8')
plt.plot(x, IPLoM, marker='v',label = 'IPLoM', markerfacecolor = 'white', markersize='8')
plt.plot(x, LenMa, marker='.',label = 'LenMa', markerfacecolor = 'white', markersize='10')
plt.plot(x, Spell, marker='x',label = 'Spell', markerfacecolor = 'white', markersize='8')
plt.plot(x, AEL, marker='s',label = 'AEL', markerfacecolor = 'white', markersize='6')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# Spark /s
Hue = np.array([
    0.12976837158203125,
    1.236786127090454,
    10.431347846984863,
    105.26473093032837,
    1058.1526293754578
    
])

Drain = np.array([
    0.14486932754516602,
    1.331913948059082,
    11.639890193939209,
    114.21220827102661,
    1151.8913221359253
])

IPLoM = np.array([
    0.18399930000305176,
    1.6912260055541992,
    15.879069089889526,
    165.24964833259583,
    1689.1745007038116
])

LenMa = np.array([
    0.525550127029419,
    6.670309543609619,
    67.49793219566345,
    674.9444720745087,
    6749.501349558435
])

Spell = np.array([
    0.14548182487487793,
    1.3792598247528076,
    12.194605112075806,
    120.6290819644928,
    1219.6065692901611
])

AEL = np.array([
    0.18556294441223145,
    1.6657941341400146,
    15.79395866394043,
    158.88955855369568,
    1595.4094698429108
])

x = np.array([2000*10**i for i in range(5)])
plt.axes(xscale='log', yscale='log')
plt.gca().xaxis.set_major_formatter(FuncFormatter(update_scale_value))
plt.xticks(x) 
plt.xlabel("Number of log messages")
plt.ylabel("Executing time(sec)")
plt.plot(x, Hue, marker='^',label = 'Hue', markerfacecolor = 'white', markersize='8')
plt.plot(x, Drain, marker='+',label = 'Drain', markerfacecolor = 'white', markersize='8')
plt.plot(x, IPLoM, marker='v',label = 'IPLoM', markerfacecolor = 'white', markersize='8')
plt.plot(x, LenMa, marker='.',label = 'LenMa', markerfacecolor = 'white', markersize='10')
plt.plot(x, Spell, marker='x',label = 'Spell', markerfacecolor = 'white', markersize='8')
plt.plot(x, AEL, marker='s',label = 'AEL', markerfacecolor = 'white', markersize='6')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# BGL /s
Hue = np.array([
    0.21837263107299805,
    1.250802707672119,
    12.240452909469604,
    121.2838077545166,
    1212.71910405159
])

Drain = np.array([
    0.1761007308959961,
    1.648118019104004,
    15.154645919799805,
    143.75057935714722,
    1323.4621138572693
])

IPLoM = np.array([
    0.15963387489318848,
    1.440270185470581,
    13.035352945327759,
    136.31580567359924,
    1495.1291723251343
])

LenMa = np.array([
    1.0408106327056885,
    10.4679632186892,
    146.6298940181732,
    5397.532905432855
])

Spell = np.array([
    0.35978055000305176,
    1.6040904521942139,
    15.974141120910645,
    157.80683588981628,
    1573.9503571987152
])

AEL = np.array([
    0.12854100227355957,
    1.0732048511505127,
    9.633987426757812,
    97.42971062660217,
    972.9516339302063
])

x = np.array([2000*10**i for i in range(5)])
plt.axes(xscale='log', yscale='log')
plt.gca().xaxis.set_major_formatter(FuncFormatter(update_scale_value))
plt.xticks(x) 
plt.xlabel("Number of log messages")
plt.ylabel("Executing time(sec)")
plt.plot(x, Hue, marker='^',label = 'Hue', markerfacecolor = 'white', markersize='8')
plt.plot(x, Drain, marker='+',label = 'Drain', markerfacecolor = 'white', markersize='8')
plt.plot(x, IPLoM, marker='v',label = 'IPLoM', markerfacecolor = 'white', markersize='8')
plt.plot(x[:-1], LenMa, marker='.',label = 'LenMa', markerfacecolor = 'white', markersize='10')
plt.plot(x, Spell, marker='x',label = 'Spell', markerfacecolor = 'white', markersize='8')
plt.plot(x, AEL, marker='s',label = 'AEL', markerfacecolor = 'white', markersize='6')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# HiBench/components
import numpy as np
labels = ["AEL", "LenMa", "Spell", "IPLoM", "Drain", "Hue"]
total = np.array([1879,64,2057,92,18,7])
width = 0.3
x = np.arange(len(labels))
eventMessage = np.array([1198,913,1383,1138,1732,1650])/total[0]
textMessage = np.array([17,24,24,28,20,21])/total[1]
tableMessage = np.array([16,16,32,32,16,2057])/total[2]
eventTemplate = np.array([77,54,62,63,80,80])/total[3]
textTemplate = np.array([12,12,12,14,9,10])/total[4]
tableTemplate = np.array([1,1,2,2,1,7])/total[5]
plt.bar(x - 0.15, eventMessage, width=width, label='Event log message', color = '#2878b5')
plt.bar(x - 0.15, textMessage, width=width, label='Text log message', bottom=eventMessage, color='#9ac9db')
plt.bar(x - 0.15, tableMessage, width=width, label='Table log message', bottom=eventMessage+textMessage, color='#f8ac8c')
plt.bar(x + 0.15, eventTemplate, width=width, label='Event log template', color='#c82423')
plt.bar(x + 0.15, textTemplate, width=width, label='Text log template', bottom=eventTemplate, color='#ff8884')
plt.bar(x + 0.15, tableTemplate, width=width, label='Table log template', bottom=eventTemplate+textTemplate, color='#f7e1ed')
plt.xlabel("Parsers")
plt.ylabel("Correctness Ratio")
plt.xticks(x, labels=labels)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# CTS/components
import numpy as np
labels = ["AEL", "LenMa", "Spell", "IPLoM", "Drain", "Hue"]
total = np.array([260,101,17,93,43,7])
width = 0.3
x = np.arange(len(labels))
eventMessage = np.array([162,80,141,111,196,233])/total[0]
textMessage = np.array([69,73,67,73,79,79])/total[1]
tableMessage = np.array([6,12,10,12,10,12])/total[2]
eventTemplate = np.array([59,29,52,39,70,83])/total[3]
textTemplate = np.array([31,33,28,33,36,36])/total[4]
tableTemplate = np.array([3,6,5,6,5,6])/total[5]
plt.bar(x - 0.15, eventMessage, width=width, label='Event log message', color = '#2878b5')
plt.bar(x - 0.15, textMessage, width=width, label='Text log message', bottom=eventMessage, color='#9ac9db')
plt.bar(x - 0.15, tableMessage, width=width, label='Table log message', bottom=eventMessage+textMessage, color='#f8ac8c')
plt.bar(x + 0.15, eventTemplate, width=width, label='Event log template', color='#c82423')
plt.bar(x + 0.15, textTemplate, width=width, label='Text log template', bottom=eventTemplate, color='#ff8884')
plt.bar(x + 0.15, tableTemplate, width=width, label='Table log template', bottom=eventTemplate+textTemplate, color='#f7e1ed')
plt.xlabel("Parsers")
plt.ylabel("Correctness Ratio")
plt.xticks(x, labels=labels)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# PaaS/components
import numpy as np
labels = ["AEL", "LenMa", "Spell", "IPLoM", "Drain", "Hue"]
total = np.array([386,255,86,129,93,6])
width = 0.3
x = np.arange(len(labels))
eventMessage = np.array([159,139,54,149,242,363])/total[0]
textMessage = np.array([57,50,30,70,66,75])/total[1]
tableMessage = np.array([5,14,5,14,33,72])/total[2]
eventTemplate = np.array([82,55,38,69,95,111])/total[3]
textTemplate = np.array([50,52,24,46,43,46])/total[4]
tableTemplate = np.array([1,2,1,2,3,5])/total[5]
plt.bar(x - 0.15, eventMessage, width=width, label='Event log message', color = '#2878b5')
plt.bar(x - 0.15, textMessage, width=width, label='Text log message', bottom=eventMessage, color='#9ac9db')
plt.bar(x - 0.15, tableMessage, width=width, label='Table log message', bottom=eventMessage+textMessage, color='#f8ac8c')
plt.bar(x + 0.15, eventTemplate, width=width, label='Event log template', color='#c82423')
plt.bar(x + 0.15, textTemplate, width=width, label='Text log template', bottom=eventTemplate, color='#ff8884')
plt.bar(x + 0.15, tableTemplate, width=width, label='Table log template', bottom=eventTemplate+textTemplate, color='#f7e1ed')
plt.xlabel("Parsers")
plt.ylabel("Correctness Ratio")
plt.xticks(x, labels=labels)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# Linux+Comparison/feedback(GA)
x1 = [0, 2, 4, 7, 8, 11, 13]
x2 = [0, 3, 5, 6, 10, 14, 15]
x3 = [0, 3, 6, 7, 10]
ga1 = [0.6780, 0.8535, 0.9230, 0.9845, 0.9950, 0.9955, 0.9980]
ga2 = [0.6760, 0.8500, 0.8600, 0.9205, 0.9250, 0.9355, 0.9370]
ga3 = [0.3560, 0.9245, 0.9860, 0.9965, 0.998]
maxlen = 16
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([0.0 for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x1):
        y1[i] = y1[i-1]
        continue
    if i == x1[j]:
        y1[i] = ga1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
j = 0
for i in range(maxlen):
    if j == len(x2):
        y2[i] = y2[i-1]
        continue
    if i == x2[j]:
        y2[i] = ga2[j]
        j += 1
    else:
        y2[i] = y2[i-1]
j = 0
for i in range(maxlen):
    if j == len(x3):
        y3[i] = y3[i-1]
        continue
    if i == x3[j]:
        y3[i] = ga3[j]
        j += 1
    else:
        y3[i] = y3[i-1]
plt.plot(xx, y3, linestyle='-.', label='Hue')
plt.plot(xx, y2, linestyle='-.', label='SPINE')
plt.xlabel("Number of Merge Queries")
plt.ylabel("Grouping Accuracy")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


# # Linux/feedback
x = [0, 3, 6, 7, 10]
ga = [0.7490, 0.9245, 0.9860, 0.9965, 0.9975]
f1 = [0.9258, 0.9304, 0.9437, 0.9569, 0.9700]
gabase = 0.7490
f1base = 0.9258

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# # Android/feedback
x = [0, 3, 4, 5, 6, 7, 8, 9, 11, 15, 17, 19]
ga = [0.7860, 0.8710, 0.8780, 0.9105, 0.9165, 0.9185, 0.9195, 0.9255, 0.9285, 0.9310, 0.9340, 0.9370]
f1 = [0.7975, 0.8075, 0.8173, 0.8272, 0.8369, 0.8466, 0.8563, 0.8659, 0.8754, 0.8848, 0.8943, 0.9036]
gabase = 0.826
f1base = 0.834

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# # BGL/feedback
x = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]
ga = [0.5545, 0.5690, 0.5730, 0.5755, 0.5760, 0.9365, 0.9395, 0.9405, 0.9440, 0.9495, 0.9515, 0.9530, 0.9560, 0.9565, 0.9575, 0.9585]
f1 = [0.7306, 0.7455, 0.7511, 0.7568, 0.7623, 0.7679, 0.7733, 0.7788, 0.7930, 0.8070, 0.8210, 0.8348, 0.8485, 0.8534, 0.8670, 0.8803]
gabase = 0.849
f1base = 0.700

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# # OpenSSH/feedback
x = [0, 9, 10]
ga = [0.7885, 0.9955, 0.9970]
f1 = [0.8148, 0.8727, 0.9286]

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# # HiBench/feedback
x = [0, 1, 3, 13, 17]
ga = [0.9320, 0.9477, 0.9590, 0.9600, 0.9605]
f1 = [0.8362, 0.8684, 0.8821, 0.8957, 0.9091]
gabase = 0.9320
f1base = 0.8362

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# PaaS/feedback
x = [0, 2, 3, 4, 5, 10, 13, 16]
ga = [0.7542, 0.8336, 0.8456, 0.8852, 0.8927, 0.9019, 0.9041, 0.9062]
f1 = [0.8014, 0.8228, 0.8314, 0.8392, 0.8558, 0.8606, 0.8663, 0.8722]
gabase = 0.7542
f1base = 0.8014

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# CTS/feedback
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
ga = [0.6675, 0.6780, 0.6885, 0.6937, 0.6990, 0.7120, 0.7356, 0.7408, 0.7461, 0.7513, 0.7565, 0.7618, 0.7670, 0.7723, 0.7827, 0.7880, 0.7932, 0.7984, 0.8089, 0.8246, 0.8403, 0.8534, 0.8639]
f1 = [0.7399, 0.7445, 0.7491, 0.7536, 0.7581, 0.7626, 0.7670, 0.7714, 0.7758, 0.7801, 0.7845, 0.7887, 0.7930, 0.7972, 0.8014, 0.8056, 0.8097, 0.8138, 0.8179, 0.8288, 0.8396, 0.8503, 0.8610]
gabase = 0.848
f1base = 0.839

maxlen = 25
xx = np.arange(maxlen)
y1 = np.array([0.0 for i in range(maxlen)])
y2 = np.array([0.0 for i in range(maxlen)])
y3 = np.array([gabase for i in range(maxlen)])
y4 = np.array([f1base for i in range(maxlen)])
j = 0
for i in range(maxlen):
    if j == len(x):
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
        continue
    if i == x[j]:
        y1[i] = ga[j]
        y2[i] = f1[j]
        j += 1
    else:
        y1[i] = y1[i-1]
        y2[i] = y2[i-1]
plt.plot(xx, y1, color = 'C0', linestyle='-.', label='GA')
plt.plot(xx, y2, color = 'C1', linestyle='-.', label='F1')
# plt.plot(xx, y3, color = 'C0', linestyle='--', label='GA base without elastic threshold', linewidth=0.5)
# plt.plot(xx, y4, color = 'C1', linestyle='--', label='F1 base without elastic threshold', linewidth=0.5)
plt.xlabel("Number of Merge Queries")
plt.ylabel("Metrics")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

import matplotlib.patches as mp
# Composition of industrial evalutaion

color = ['r','m','c', 'C0', 'C1']
label = ['Event log', 'Text log', 'Table log', 'Correctly parsed', 'Incorrectly parsed']
data = np.array([[25.7,6.6],[16.9,9.2],[37.9,3.7]])
plt.pie(data.flatten(), radius=1, pctdistance=0.7, wedgeprops=dict(width=0.5, edgecolor='w'), autopct='%1.1f%%', colors=['C0','C1','C0','C1','C0','C1'])
plt.pie(data.sum(axis=1), radius=0.5, pctdistance=0.8, wedgeprops=dict(width=0.5, edgecolor='w'), colors=color)
patch = [mp.Patch(color=color[i], label="{:s}".format(label[i])) for i in range(5)]
plt.legend(handles=patch)
plt.show()

# Line plot of industrial evalutaion
x = range(8)
ra = [0.922, 0.912, 0.872, 0.853, 0.842, 0.801, 0.796, 0.794]
rq = [0.950, 0.982, 0.967, 0.979, 0.978, 0.960, 0.957, 0.965]
ua = [0.936, 0.924, 0.901, 0.891, 0.863, 0.857, 0.853, 0.829]
uq = [0.972, 0.996, 0.982, 0.993, 0.981, 0.980, 0.982, 0.983]
plt.plot(x, ra, marker='o', linestyle='-', color='C0', label='Auto updating + Root cause analysis')
plt.plot(x, rq, marker='o', linestyle='-', color='C1', label='Guided updating + Root cause analysis')
plt.plot(x, ua, marker='o', linestyle='--', color='C0', label='Auto updating + User profile construction')
plt.plot(x, uq, marker='o', linestyle='--', color='C1', label='Guided updating + User profile construction')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.xlabel("Time(Weeks)")
plt.ylabel("Group Accuracy")