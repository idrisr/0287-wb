from wandb import init
import wandb
import os
import yaml
import click
from click import echo


CONTEXT = dict(default_map={})


with open('env.yaml') as f:
    for k, v in yaml.safe_load(f).items():
        os.environ[k] = v


@click.command(context_settings=CONTEXT, help="create a project")
def log():
    wandb.init()
    wandb.log({'accuracy': 1, 'loss': 2})
    echo("yo")


@click.command(context_settings=CONTEXT, help="list projects")
def projects():
    [echo(o.name) for o in wandb.Api().projects()]
