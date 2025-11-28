import argparse
from trainer import train


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="domainnet", type=str, choices=["domainnet"])

    parser.add_argument("--shuffle", default=True, type=bool)
    parser.add_argument("--model_name", default="adapter", type=str, choices=["adapter", "ssf"])
    parser.add_argument(
        "--convnet_type",
        default="pretrained_vit_b16_224_adapter",
        type=str,
        choices=["pretrained_vit_b16_224_adapter", "pretrained_vit_b16_224_ssf"],
    )

    parser.add_argument("--init_cls", default=240, type=int)
    parser.add_argument("--increment", default=35, type=int)

    parser.add_argument("--seed", default=1998, type=int)
    parser.add_argument("--batch_size", default=48, type=int)
    parser.add_argument("--tuned_epoch", default=20, type=int)
    parser.add_argument("--follow_epoch", default=15, type=int)

    parser.add_argument("--body_lr", default=0.01, type=float)
    parser.add_argument("--head_lr", default=0.01, type=float)
    parser.add_argument("--weight_decay", default=0.0005, type=float)
    parser.add_argument("--min_lr", default=0.0, type=float)

    parser.add_argument("--use_RP", default=True, type=bool)
    parser.add_argument("--M", default=768, type=int)
    parser.add_argument("--use_input_norm", default=False, type=bool)
    parser.add_argument("--fast_disf", default=0.5, type=float)
    parser.add_argument("--slow_diag", default=5e-10, type=float)
    parser.add_argument("--slow_rdn", default=5e-9, type=float)

    parser.add_argument("--merge_result", default=1, type=float)
    parser.add_argument("--fast_cc", default=1, type=float)
    parser.add_argument("--scalar_val", default=1, type=float)

    parser.add_argument("--device", default=[0], type=int, nargs="+")
    parser.add_argument("--save_path", default="./logs", type=str)

    return parser.parse_args()


def main():
    args = parse_argument()
    args = vars(args)
    args["seed"] = [args["seed"]]
    args["do_not_save"] = False

    train(args)


if __name__ == "__main__":
    main()
