from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    project_root: Path
    raw_dir: Path
    processed_dir: Path
    logs_dir: Path


def get_paths(project_root: Path | None = None) -> Paths:
    root = project_root or Path(__file__).resolve().parents[1]
    return Paths(
        project_root=root,
        raw_dir=root / "data" / "raw",
        processed_dir=root / "data" / "processed",
        logs_dir=root / "logs",
    )


def configure_logging(log_level: str) -> None:
    level = getattr(logging, log_level.upper(), logging.INFO)
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")


def standardize_column_names(cols: list[str]) -> list[str]:
    def norm(c: str) -> str:
        c = c.strip().lower()
        c = c.replace(" ", "_").replace("-", "_")
        while "__" in c:
            c = c.replace("__", "_")
        return c

    return [norm(c) for c in cols]


def main() -> int:
    parser = argparse.ArgumentParser(description="Capstone ETL pipeline entry point.")
    parser.add_argument(
        "--raw-file",
        type=str,
        default="",
        help="Raw dataset filename inside data/raw/ (example: loans.csv).",
    )
    parser.add_argument(
        "--out-file",
        type=str,
        default="clean_lendingclub.csv",
        help="Output filename inside data/processed/.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR).",
    )
    args = parser.parse_args()

    configure_logging(args.log_level)
    paths = get_paths()
    paths.raw_dir.mkdir(parents=True, exist_ok=True)
    paths.processed_dir.mkdir(parents=True, exist_ok=True)
    paths.logs_dir.mkdir(parents=True, exist_ok=True)

    logging.info("Raw dir: %s", paths.raw_dir)
    logging.info("Processed dir: %s", paths.processed_dir)

    # TODO (Day 4–5): Implement the same cleaning rules as 02_cleaning.ipynb.
    # Keep transformations documented and reproducible.
    if not args.raw_file:
        logging.warning("No --raw-file provided yet. Add dataset to data/raw/ then rerun.")
        return 0

    raw_path = paths.raw_dir / args.raw_file
    out_path = paths.processed_dir / args.out_file
    if not raw_path.exists():
        logging.error("Raw file not found: %s", raw_path)
        return 2

    logging.info("Planned raw input: %s", raw_path)
    logging.info("Planned cleaned output: %s", out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

