import os
import click

@click.group()
def cli():
    pass


@cli.command()
@click.argument('src_dir')
@click.option('--min_side', '-m', default=None, type=int, help='Minimum side length of the image.')
def resize(src_dir, min_side, dst_dir, format, quality, exist_ok):

    # resize implementation
    print(f'Resizing directory: {src_dir}')

    if not min_side:
        min_side = click.prompt('- Minimum side length', type=int, default=768)
    if not format:
        format = click.prompt('- File format', default="webp")
    if not dst_dir:
        src_dir_name = os.path.basename(os.path.abspath(src_dir))
        dst_dir = click.prompt('- Destination', default=f"{src_dir_name}_{min_side}_{format}")
    if not quality:
        quality = click.prompt('- Image quality', type=int, default=95)
    if not exist_ok:
        exist_ok = click.prompt('- Keep existing images', type=bool, default=True)

    # Printing the command
    print("\nRunning Command:\n")
    print(f"unibox resize {src_dir} --min_side {min_side} --dst_dir {dst_dir} "
          f"--format {format} --quality {quality} --exist_ok {exist_ok}\n")

    return