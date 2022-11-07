"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """House Sales."""


if __name__ == "__main__":
    main(prog_name="house-sales")  # pragma: no cover
