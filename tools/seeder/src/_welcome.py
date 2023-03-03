from datetime import datetime, timedelta
from io import BytesIO
import json
import os
import textwrap

from humanize import intcomma, naturaltime
from termcolor import colored


from requests.sessions import Session
from src._session import session


def get_welcome_message(
    base_field_number: int,
    ending_number: int,
    execution_time: int,
    starting_number: int,
    field_name: str,
):
    return textwrap.dedent(
        f"""
        Starting Number : {
            colored(
                text=str(
                    intcomma(
                        base_field_number
                    )
                ),
                color='green'
            )
        }
        Total `{field_name}` to get : {
            colored(
                text=str(
                    intcomma(
                        ending_number
                    )
                ),
                color='green'
            )
        }
        Time to finish : {
            colored(
                text=str(
                    naturaltime(
                        datetime.now()
                        +
                        timedelta(
                            seconds=
                                round(
                                    (
                                        ending_number
                                        -
                                        base_field_number
                                    )
                                    *
                                    (
                                        execution_time
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
