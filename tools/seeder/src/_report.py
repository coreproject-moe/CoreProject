def get_report_message(
    base_field_number: int,
    starting_number: int,
    execution_time: int,
    field_name: str,
    success_list: list[str],
    error_list: list[str],
    warning_list: list[str],
):
    return (
        f"[{execution_time:.2f}]"
        " "
        f"Requested `{field_name}` for {base_field_number}"
        " | "
        f"""`starting_number` {
            starting_number
        }"""
        " | "
        f"""[{', '.join(
            sorted(
                    set(
                        success_list
                        + error_list
                        + warning_list
                    ),
                    key=lambda string: string[10],
                )
            )
        }]"""
    )
