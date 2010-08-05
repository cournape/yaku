import os
import sys

from yaku.scheduler \
    import \
        run_tasks
from yaku.context \
    import \
        get_bld, get_cfg
from yaku.task_manager \
    import \
        set_file_hook, get_extension_hook

def configure(ctx):
    ctx.use_tools(["ctasks"])
    c_hook = get_extension_hook(".c")
    def new_c_hook(self, node):
        return c_hook(self, node)
    set_file_hook("src/main.c", new_c_hook)

def build(ctx):
    builder = ctx.builders["ctasks"]
    builder.program("main", ["src/main.c"])

if __name__ == "__main__":
    ctx = get_cfg()
    configure(ctx)
    ctx.store()

    ctx = get_bld()
    build(ctx)
    run_tasks(ctx)
    ctx.store()
