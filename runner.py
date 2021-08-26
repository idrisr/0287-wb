from wandb import init
import wandb
import os
import yaml
import click
from click import echo


CONTEXT = dict(default_map={})


@click.command(context_settings=CONTEXT, help="create a project")
def log():
    wandb.init()
    wandb.log({'accuracy': 2, 'loss': 10})
    echo("yo")


@click.command(context_settings=CONTEXT, help="list projects")
def projects():
    [echo(o.name) for o in wandb.Api().projects()]
