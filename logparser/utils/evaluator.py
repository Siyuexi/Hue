
import sys
import pandas as pd
from collections import defaultdict
import scipy.special


def evaluate(groundtruth, parsedresult):
    """ Evaluation function to benchmark log parsing accuracy
    
    Arguments
    ---------
        groundtruth : str
            file path of groundtruth structured csv file 
        parsedresult : str
            file path of parsed structured csv file

    Returns
    -------
        f_measure : float
        accuracy : float
    """ 
    df_groundtruth = pd.read_csv(groundtruth)
    df_parsedlog = pd.read_csv(parsedresult)
    # Remove invalid groundtruth event Ids
    non_empty_log_ids = df_groundtruth[~df_groundtruth['EventId'].isnull()].index
    # print("non_empty_log_ids:{}".format(non_empty_log_ids))
    df_groundtruth = df_groundtruth.loc[non_empty_log_ids]
    # print("df_groundtruth:{}".format(df_groundtruth))
    df_parsedlog = df_parsedlog.loc[non_empty_log_ids]
    # print("df_parsedlog:{}".format(df_parsedlog))
    (precision, recall, f_measure, accuracy) = get_accuracy(df_groundtruth['EventId'], df_parsedlog['EventId'])
    print('Precision: %.4f, Recall: %.4f, F1_measure: %.4f, Parsing_Accuracy: %.4f'%(precision, recall, f_measure, accuracy))
    return accuracy, precision, recall, f_measure

def get_accuracy(series_groundtruth, series_parsedlog, debug=False):
    """ Compute accuracy metrics between log parsing results and ground truth
    
    Arguments
    ---------
        series_groundtruth : pandas.Series
            A sequence of groundtruth event Ids
        series_parsedlog : pandas.Series
            A sequence of parsed event Ids
        debug : bool, default False
            print error log messages when set to True

    Returns
    -------
        precision : float
        recall : float
        f_measure : float
        accuracy : float
    """
    EVENT = [0, 0]
    TEXT  = [0, 0]
    TABLE = [0, 0]

    series_groundtruth_valuecounts = series_groundtruth.value_counts()
    # print("series_groundtruth_valuecounts:{}".format(series_groundtruth_valuecounts))
    real_pairs = 0
    for count in series_groundtruth_valuecounts:
        if count > 1:
            real_pairs += scipy.special.comb(count, 2)
    # print("real_pairs:{}".format(real_pairs))
    series_parsedlog_valuecounts = series_parsedlog.value_counts()
    # print("series_parsedlog_valuecounts:{}".format(series_parsedlog_valuecounts))
    parsed_pairs = 0
    for count in series_parsedlog_valuecounts:
        if count > 1:
            parsed_pairs += scipy.special.comb(count, 2)
    # print("parsed_pairs:{}".format(parsed_pairs))
    accurate_pairs = 0
    accurate_events = 0 # determine how many lines are correctly parsed
    accurate_templates = 0
    for parsed_eventId in series_parsedlog_valuecounts.index:
        logIds = series_parsedlog[series_parsedlog == parsed_eventId].index
        # print("logIds:{}".format(logIds))
        series_groundtruth_logId_valuecounts = series_groundtruth[logIds].value_counts()
        # print("series_groundtruth_logId_valuecounts:{}".format(series_groundtruth_logId_valuecounts))
        error_eventIds = (parsed_eventId, series_groundtruth_logId_valuecounts.index.tolist())
        error = True
        if series_groundtruth_logId_valuecounts.size == 1:
            groundtruth_eventId = series_groundtruth_logId_valuecounts.index[0]
            # print("groundtruth_eventId:{}".format(groundtruth_eventId))
            if logIds.size == series_groundtruth[series_groundtruth == groundtruth_eventId].size:
                # print("series_groundtruth:{}".format(series_groundtruth))
                # print("WTF:{}".format( series_groundtruth[series_groundtruth == groundtruth_eventId]))
                # print("logIds.size:{}".format(logIds.size))

                if groundtruth_eventId[0] == 's':
                    EVENT[0] += 1
                    EVENT[1] += logIds.size
                elif groundtruth_eventId[0] == 'm':
                    TEXT[0] += 1
                    TEXT[1] += logIds.size
                else:
                    TABLE[0] += 1
                    TABLE[1] += logIds.size
                    

                accurate_events += logIds.size
                accurate_templates += 1
                error = False
        if error and debug:
            print('(parsed_eventId, groundtruth_eventId) =', error_eventIds, 'failed', logIds.size, 'messages')
        for count in series_groundtruth_logId_valuecounts:
            if count > 1:
                accurate_pairs += scipy.special.comb(count, 2)

    precision = float(accurate_templates) / len(series_parsedlog_valuecounts)
    recall = float(accurate_templates) / len(series_groundtruth_valuecounts)
    f_measure = 2 * precision * recall / (precision + recall)
    accuracy = float(accurate_events) / series_groundtruth.size

    print(EVENT, TEXT, TABLE)
    return precision, recall, f_measure, accuracy

# evaluate("results/Drain_result/HDFS_2k.log_structured.csv", "logs/HDFS/HDFS_2k.log_structured.csv")





