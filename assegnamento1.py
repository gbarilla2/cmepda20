#!/usr/bin/env python3
"""First assignment.
"""
import argparse
import logging
import time
import string
import matplotlib.pyplot as plt
logging.getLogger("matplotlib").setLevel(logging.WARNING)

logging.basicConfig(level=logging.DEBUG)


def process(file_path, histo,stat):
    """"Read the text file and compile the letter statistic."""
    start_time = time.time()

    logging.info("Reading input file %s...", file_path)
    with open(file_path) as input_file:
        text = input_file.read()
    num_chars = len(text)
    logging.info("Done, %d characters found.", num_chars)

    #char_dict = {chr(x): 0 for x in range(ord('a'),ord('z')+1)}
    char_dict = {ch: 0 for ch in string.ascii_lowercase}
    for ch in text:
        # try:
        #     char_dict[ch.lower()] += 1
        # except KeyError:
        #     pass
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1
    #letters counter
    num_letters= sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f"{ch} -> {num/num_letters:.3%}")

    if(stat==True):

        logging.info("Done, %d letters found.", num_letters)

        #lines counter it counts also empty lines
        #split separetes every line with \n end
        list_lines=text.split("\n")
        logging.info("Done, %d lines found.", len(list_lines))

        #lines counter it counts only non-empty lines
        #split separates every line with \n end and the filter remove blank line
        list_blank_lines=text.split("\n")
        list_blank_lines=list(filter(None, list_blank_lines))
        logging.info("Done, %d non-empty lines found.", len(list_blank_lines))

        #words counter
        #replace the \n with space and split separates every word between space and the filter remove blank element
        list_words=(text.replace("\n"," ")).split(" ")
        list_words=list(filter(None, list_words))
        logging.info("Done, %d words found.", len(list_words))

    elapsed_time= time.time() - start_time
    logging.info("Done in %.3f s.",elapsed_time)
    if(histo==True):
        plt.bar(list(char_dict.keys()), char_dict.values(), color='blue')
        plt.title("Characters histogram")
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program that prints the relative frequence of each letter of the alphabet (without distinguishing between lower and upper case) in the book.')
    parser.add_argument('infile', type=str, help="Path to the input file")
    parser.add_argument('--histo', action='store_const', default=False, const=True, help="Option to display a histogram of the frequences (set false for default)")
    parser.add_argument('--stat', action='store_const', default=False, const=True, help="Option to display the basic book statistic (set false for default)")
    args = parser.parse_args()

    process(args.infile,args.histo,args.stat)
