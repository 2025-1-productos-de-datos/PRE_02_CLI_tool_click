"""Command line interface (CLI) tool"""

import click

#
# Estructura:
#
# mycli +--- command_1
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#       |
#       +--- command_2
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#



@click.group()
def mycli():
    "Herramienta de linea de comandos"
    pass



# =========================================================================
# COMMAND1 Group
# =========================================================================
@mycli.group()
def command1():
    """Comandos relacionados con COMMAND1"""
    pass


@command1.command("run")
@click.option("--a", required=True, help="Valor del parametro a")
def command_1_subcommand_1(a):
    """Ejecuta un subcomando 1-1"""
    click.echo(f"\n---> Ejecutando command 1 subcommand 1: a = {a}\n")


@command1.command("stop")
@click.option("--b", required=True, help="Valor del parametro b")
def command_1_subcommand_2(b):
    """Ejecuta un subcomando 1-2"""
    click.echo(f"\n---> Ejecutando command 1 subcommand 2: b = {b}\n")


# =========================================================================
# COMMAND2 Group
# =========================================================================
@mycli.group()
def command2():
    """Comandos relacionados con COMMAND2"""
    pass


@command2.command("jump")
@click.option("--c", required=True, help="Valor del parametro c")
def command_2_subcommand_1(c):
    """Ejecuta un subcomando 2-1"""
    click.echo(f"\n---> Ejecutando command 2 subcommand 1: c = {c}\n")


@command2.command("cry")
@click.option("--d", required=True, help="Valor del parametro d")
def command_2_subcommand_2(d):
    """Ejecuta un subcomando 2-2"""
    click.echo(f"\n---> Ejecutando command 2 subcommand 2: d = {d}\n")




if __name__ == "__main__":
    mycli()

