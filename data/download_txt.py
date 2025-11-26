import os
import shutil

if __name__ == "__main__":
    domains = ["clipart", "infograph", "painting", "quickdraw", "real", "sketch"]
    for d in domains:
        os.system(
            "wget https://csr.bu.edu/ftp/visda/2019/multi-source/domainnet/txt/%s_train.txt" % d
        )
        shutil.move(f"{d}_train.txt", f"./DomainNet/{d}_train.txt")

        os.system(
            "wget https://csr.bu.edu/ftp/visda/2019/multi-source/domainnet/txt/%s_test.txt" % d
        )
        shutil.move(f"{d}_test.txt", f"./DomainNet/{d}_test.txt")
