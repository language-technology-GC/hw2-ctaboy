#!/usr/bin/env python
"""Computes WER for Icelandic G2P"""

import argparse


def main(args: argparse.Namespace) -> None:
    with open(args.predictions, "r") as file:
        target_list = []
        hypo_list = []
        for sent in file:
            if sent[:2] == "T-":
                target_list.append(sent.split("\t")[1].rstrip())
            if sent[:2] == "H-":
                hypo_list.append(sent.split("\t")[2].rstrip())

        wrong_counts = 0
        for (target, predicted) in zip(target_list, hypo_list):
            if target != predicted:
                wrong_counts += 1

        wer = round((wrong_counts / len(target_list)) * 100)
        print(
            f"{wrong_counts} incorrect predictions out of {len(target_list)} examples"
        )
        print(f"WER: {wer}%")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", help="Input file path: predictions.txt")
    main(parser.parse_args())
