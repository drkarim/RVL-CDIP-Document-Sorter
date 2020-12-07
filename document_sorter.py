import pandas as pd
import time
from progress.bar import Bar
import argparse
import os


class Document2Label:

    '''
        From the dataset readme.txt 
    '''
    label_dictionary = {
        3  :  "handwritten",
        4  :  "advertisement",
        5  :  "scientific report",
        6  :  "scientific publication",
        7  :  "specification",
        8  :  "file folder",
        9  :  "news article",
        10  :  "budget",
        11  :  "invoice",
        12  :  "presentation",
        13  :  "questionnaire",
        14  :  "resume",
        15  :  "memo",
    }

    def __init__(self):
        self.label_filename = None

        self.label_map = {}

        for label in self.label_dictionary:
            self.label_map[label] = []


    def SetLabelFile(self, filename):
        self.label_filepath = filename



    def ReadLabelFile(self):

        # count number of lines in file for progress bar
        total_lines = sum(1 for line in open(self.label_filepath))

        with Bar('Processing', max=total_lines) as bar:
            with open(self.label_filepath, 'r') as file_object:
                line = file_object.readline()
                stop = True
                line_count = 0

                while line_count < total_lines:
                    fn_and_label = line.split(" ")
                    filename = fn_and_label[0]
                    label_value = int(fn_and_label[1].rstrip("\n"))

                    if label_value in self.label_dictionary:
                        self.label_map[label_value].append(filename)


                    line_count = line_count + 1
                    bar.next()
        bar.finish()

    def QueryLabel(self, label_key):

        if label_key in self.label_map:
            filename_list = self.label_map[label_key]

        return filename_list



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", help="The path to the file containing mapping of filename to label", required=True)
    args = parser.parse_args()


    if args.filename is None:
        label_filename = './data/labels/train.txt'
    else:
        label_filename = args.filename

    doc2label = Document2Label()
    doc2label.SetLabelFile(label_filename)
    doc2label.ReadLabelFile()

    invoices_list = doc2label.QueryLabel(11)

