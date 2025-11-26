# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import os

from zipfile import ZipFile
import argparse
import tarfile
import gdown


# utils #######################################################################


def stage_path(data_dir, name):
    full_path = os.path.join(data_dir, name)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return full_path


def download_and_extract(url, dst, remove=True):
    gdown.download(url, dst, quiet=False)

    if dst.endswith(".tar.gz"):
        tar = tarfile.open(dst, "r:gz")
        tar.extractall(os.path.dirname(dst))
        tar.close()

    if dst.endswith(".tar"):
        tar = tarfile.open(dst, "r:")
        tar.extractall(os.path.dirname(dst))
        tar.close()

    if dst.endswith(".zip"):
        zf = ZipFile(dst, "r")
        zf.extractall(os.path.dirname(dst))
        zf.close()

    if remove:
        os.remove(dst)


# DomainNET ###################################################################


def download_domain_net(data_dir):
    # Original URL: http://ai.bu.edu/M3SDA/
    full_path = stage_path(data_dir, "DomainNet")

    urls = [
        "http://csr.bu.edu/ftp/visda/2019/multi-source/groundtruth/clipart.zip",
        "http://csr.bu.edu/ftp/visda/2019/multi-source/infograph.zip",
        "http://csr.bu.edu/ftp/visda/2019/multi-source/groundtruth/painting.zip",
        "http://csr.bu.edu/ftp/visda/2019/multi-source/quickdraw.zip",
        "http://csr.bu.edu/ftp/visda/2019/multi-source/real.zip",
        "http://csr.bu.edu/ftp/visda/2019/multi-source/sketch.zip",
    ]

    for url in urls:
        download_and_extract(url, os.path.join(full_path, url.split("/")[-1]))

    with open("./misc/domain_net_duplicates.txt", "r") as f:
        for line in f.readlines():
            try:
                os.remove(os.path.join(full_path, line.strip()))
            except OSError:
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download datasets")
    parser.add_argument("--data_dir", type=str, required=True)
    args = parser.parse_args()

    download_domain_net(args.data_dir)
