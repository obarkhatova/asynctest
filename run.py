import click
from click.types import BadParameter

from src.script import run


base_context = {'help_option_names': ['-h', '--help'],
                'allow_extra_args': True,
                'ignore_unknown_options': True}


@click.command(context_settings=base_context)
@click.option('--name', type=click.STRING, default='TestName', help='Your name')
@click.option('--vacancy', type=click.STRING, default='Backend developer',
              help='Vacancy')
@click.option('--salary', type=click.INT, default=100, help='Salary expected')
@click.option('--delay', type=click.FloatRange(0, 9), default=0.3, help='Max '
                                                                             'delay')
@click.option('--count', type=click.IntRange(0, 50), default=3, help='Task count')
def run_script(**kwargs):
   run(**kwargs)


if __name__ == "__main__":
    exit(run_script(standalone_mode=False))


