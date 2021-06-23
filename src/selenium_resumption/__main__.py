"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Selenium Resumption."""


if __name__ == "__main__":
    main(prog_name="selenium-resumption")  # pragma: no cover
