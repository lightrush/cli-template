#! /usr/bin/env python3

import click

@click.group()
def cli():
    pass

@cli.command()
def sub_command_one():
    click.echo('Sub-command one invoked.')

@cli.command()
def sub_command_two():
    click.echo('Sub-command two invoked.')
    
@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def sub_command_with_options_and_args(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
    
if __name__ == '__main__':
    cli()

