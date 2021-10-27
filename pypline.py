#!/usr/bin/env python
"""Converts TSV files to binary files for fairseq preprocessing"""

import argparse


def main(args: argparse.Namespace) -> None:
    with open(args.train, "r") as source:
        with open(args.t1, "w") as sink1, open(args.t2, "w") as sink2:
            for pair in source:
                pair_list = pair.split("\t")
                print(" ".join(pair_list[0]), file=sink1)
                print(pair_list[1].rstrip(), file=sink2)

    with open(args.dev, "r") as source:
        with open(args.d1, "w") as sink1, open(args.d2, "w") as sink2:
            for pair in source:
                pair_list = pair.split("\t")
                print(" ".join(pair_list[0]), file=sink1)
                print(pair_list[1].rstrip(), file=sink2)

    with open(args.test, "r") as source:
        with open(args.test1, "w") as sink1, open(args.test2, "w") as sink2:
            for pair in source:
                pair_list = pair.split("\t")
                print(" ".join(pair_list[0]), file=sink1)
                print(pair_list[1].rstrip(), file=sink2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("train", help="Input train file: ice_train.tsv")
    parser.add_argument("t1", help="Output file for Icelandic words: train.ice.g")
    parser.add_argument("t2", help="Output file for IPA transcriptions: train.ice.p")
    parser.add_argument("dev", help="Input dev file: ice_dev.tsv")
    parser.add_argument("d1", help="Output file for Icelandic words: dev.ice.g")
    parser.add_argument("d2", help="Output file for IPA transcriptions: dev.ice.p")
    parser.add_argument("test", help="Input test file: ice_test.tsv")
    parser.add_argument("test1", help="Output file for Icelandic words: test.ice.g")
    parser.add_argument("test2", help="Output file for IPA transcriptions: test.ice.p")
    main(parser.parse_args())
