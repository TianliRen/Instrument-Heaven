from app.dev import *
from app import create_app

import argparse

if __name__ == "__main__":
    app = create_app('development')
    parser = argparse.ArgumentParser()

    parser.add_argument('-insert', action="store_true", default=False, help="Database insert mode")
    parser.add_argument('-reset', action="store_true", default=False, help="Reset database first")
    parser.add_argument('-a', action="store_true", default=False, help="Insert all in app/dev/_dev_data.py")

    args = parser.parse_args()

    with app.app_context():
        # Reset
        if args.reset:
            reset()
        # Completely Insert Mode
        if args.insert:
            if args.a:
                insert_all()


