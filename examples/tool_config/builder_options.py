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

def pre_configure(ctx):
    ctx.builders["ctasks"].cc_type = "clang"

def configure(ctx):
    ctx.env["CFLAGS"].extend(["-arch", "i386"])
    ctx.env["LINKFLAGS"].extend(["-arch", "i386"])
    return

def post_configure(ctx):
    pass

if __name__ == "__main__":
    ctx = get_cfg()
    pprint("PINK", "Preparing")
    prepare_default(ctx)
    pprint("PINK", "Pre configure")
    pre_configure(ctx)
    pprint("PINK", "Setting up tools")
    ctx.setup_tools()
    pprint("PINK", "Configuring")
    configure(ctx)
    pprint("PINK", "Post configuring")
    post_configure(ctx)
    ctx.store()

    build()
