import typer
from ssg.site import Site

def main(source="content", dest="dist"):
    config={
        "source":source,
        "dest": dest
    }
    mySite = Site(**config)
    mySite.build()


typer.run(main)