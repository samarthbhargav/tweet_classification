import re
import numpy as np
import random
def get_csv_file_names():
    import glob
    return glob.glob("*.csv")


def process_file(filename):

    def process(text):
        text = re.sub(r'^"', '', text)
        return re.sub(r'"$', '', text).strip()

    data = []
    labels = []
    with open(filename, 'r') as read:
        for line in read:
            split = line.split(",", 1)
            labels.append(process(split[0]))
            data.append(process(split[1]))
    return labels, data

if __name__ == "__main__":

    from classify import BayesClassifier
    from classify import SVMClassifier
    filenames = get_csv_file_names()

    if len(filenames) == 0:
        print "No csv files in the current directory, Quitting"
        exit(1)

    target, dataset = [], []
    for filename in filenames:
        labels, data = process_file(filename)
        #print "File:{}\nLabels:{}, Dataset:{}".format(filename, labels, data)
        target.extend(labels)
        dataset.extend(data)

    target = np.array(target)
    dataset = np.array(dataset)
    zipped = zip(target,dataset)
    random.shuffle(zipped)
    target, dataset = zip(*zipped)

    target = np.array(target)
    dataset = np.array(dataset)

    clf = SVMClassifier()
    split_perc = 0.66

    # todo shuffle

    split = int(split_perc * len(dataset))
    for data in dataset:
        clf.append_to_corpus(data)

    clf.train(dataset[:split], target[:split])
    accuracy = 0.0
    for data, label in zip(dataset[split:], target[split:]):

        if clf.predict(data) == label:
            accuracy += 1
    print accuracy / (len(dataset) - split)

