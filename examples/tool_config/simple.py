import os
import sys

from yaku.pprint \
    import \
        pprint
from yaku.context \
    import \
        get_cfg, get_bld

sys.path.insert(0, os.path.dirname(__file__))

from common \
    import \
        build

def prepare_default(ctx):
    ctx.load_tool("ctasks")

def configure(ctx):
    pass

def post_configure(ctx):
    pass

if __name__ == "__main__":
    ctx = get_cfg()
    pprint("PINK", "Preparing")
    ctx.load_tool("ctasks")
    pprint("PINK", "Configuring")
    configure(ctx)
    pprint("PINK", "Setting up tools")
    ctx.setup_tools()
    pprint("PINK", "Post configuring")
    post_configure(ctx)
    ctx.store()

    build()
