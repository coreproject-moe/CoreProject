# BORKED

from datetime import datetime, timedelta
import json
import os
import textwrap

from humanize import intcomma, naturaltime
from termcolor import colored


from _session import session

STUDIO_LOCK_FILE_NAME = "Studios.lock"

EXECUTION_TIME: int = 0

JIKAN: dict[int, list[int]] = {}

SUCCESSFUL_KITSU_IDS = []
SUCCESSFUL_ANILIST_IDS = []

SUCCESS_LIST = []
WARNING_LIST = []
ERROR_LIST = []

BACKEND_API_URL = "http://127.0.0.1:8000/api/v1/studios"


def command() -> None:
    global JIKAN, KITSU, ANILIST
    global EXECUTION_TIME
    global SUCCESSFUL_JIKAN_IDS, SUCCESSFUL_ANILIST_IDS

    starting_number = 1
    staff_number = 1
    ending_number: int = get_ending_number(session)

    # Load JSON file and get data from it
    if os.path.exists(STUDIO_LOCK_FILE_NAME):
        print("Lock file found. Do you want to use it?")

        # While loop to ask for data
        while True:
            answer = input("\r").lower()

            if "y" in answer:
                data = json.load(open(STUDIO_LOCK_FILE_NAME, encoding="utf-8"))
                starting_number = int(data.get("STARTING_NUMBER", starting_number))
                staff_number = int(data.get("STAFF_NUMBER", staff_number))

                # Load Lists
                JIKAN = data.get("JIKAN", JIKAN)
                EXECUTION_TIME = data.get("EXECUTION_TIME", EXECUTION_TIME)
                break

            elif "n" in answer:
                break

    welcome_message = textwrap.dedent(
        f"""
            Starting Number : {
                colored(
                    str(
                        intcomma(
                            staff_number
                        )
                    ),
                    color='green'

                )
            }
            Total `studios` to get :  {
                colored(
                    str(
                        intcomma(
                            ending_number
                        )
                    ),
                    color='green'
                )
            }
            Time to finish : {
                colored(
                    str(
                        naturaltime(
                            datetime.now()
                            +
                            timedelta(
                                seconds=
                                    round(
                                        (
                                            ending_number
                                            -
                                            staff_number
                                        )
                                        *
                                        (
                                            EXECUTION_TIME
                                            /
                                            starting_number
                                        )
                                )
                            )
                        )
                    ),
                    color='green'
                )
            }
        """
    )
    print(welcome_message)

    # Magic starts here
    populate_database(
        session=session,
        starting_number=starting_number,
        staff_number=staff_number,
        ending_number=ending_number,
    )

    session.close()

    # Remove lock file
    os.remove(STUDIO_LOCK_FILE_NAME)
