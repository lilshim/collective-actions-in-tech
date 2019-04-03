import os
import textwrap
import argparse
from pathlib import Path
from utils.markdown import (
    get_df_from_md_document,
    clean_md_document,
    save_md_data_to_csv,
    MD_PATH
)


def _get_parser():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(
            """
        This script is used to:
        - clean up the passed in markdown file,
        - export the table in the passed in markdown file to a csv
		"""
        ),
        epilog=textwrap.dedent(
            """
        # Convert to CSV file
        $ python convert.py --to-csv --output data.csv

        # Clean up the table in the README file
        $ python convert.py --clean-doc
        """
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--to-csv",
        action="store_true",
        help="Converts the table in the README to a csv file.",
    )
    parser.add_argument("--output", help="Name of the output csv.")
    parser.add_argument(
        "--clean-doc", action="store_true", help="Cleans up the table in the README."
    )
    args = parser.parse_args()
    if args.to_csv and (args.output is None):
        parser.error("--to-csv requires --output.")
    return args


if __name__ == "__main__":
    args = _get_parser()
    if args.clean_doc:
        clean_md_document(Path(MD_PATH))
    if args.to_csv:
        save_md_data_to_csv(Path(MD_PATH), Path(args.output))
