import sys

if sys.argv[1] == "character":
    from src.character import command

    command()

elif sys.argv[1] == "staff":
    from src.staff import command

    command()
