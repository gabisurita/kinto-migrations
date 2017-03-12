import argparse
import logging

import yaml
from kinto_http import cli_utils

from . import migrate_model


def main():
    # Setup parser
    parser = argparse.ArgumentParser(
        description='Migrate Kinto databases from specification files.'
    )

    parser.add_argument('-f', '--file',
                        help='File describing Kinto resources.')

    cli_utils.add_parser_options(parser)
    args = parser.parse_args()

    # Setup logging
    logger = logging.getLogger(__name__)
    cli_utils.setup_logger(logger, args)

    # Create client
    client = cli_utils.create_client_from_args(args)

    # Load models file
    models = yaml.load(open(args.file or 'models.yml'))

    # Run migration
    migrate_model(client, models)


if __name__ == "__main__":
    main()
