import sys

from yaku.scheduler \
    import \
        run_tasks
from yaku.context \
    import \
        get_bld, get_cfg

def configure(ctx):
    ctx.use_tools(["pyext"])
    ctx.load_tool("cython")
    cython_tool = ctx.builders["cython"]
    if not cython_tool.ensure_version("0.12.1"):
        if ctx.env.has_key("CYTHON_VERSION"):
            raise ValueError("You need cython >= %s (detected %s)" % \
                             ("0.12.1", ".".join(ctx.env["CYTHON_VERSION"])))
        else:
            raise ValueError("You need cython >= %s" % "0.12.1")
    #ctx.load_tool("ctasks")
    #ctasks_tool = ctx.builders["ctasks"]
    #ctasks_tool.detect_compiler()

def build(ctx):
    pyext = ctx.builders["pyext"]
    pyext.extension("_von", ["src/vonmises_cython.pyx"])

if __name__ == "__main__":
    ctx = get_cfg()
    configure(ctx)
    ctx.store()

    ctx = get_bld()
    build(ctx)
    run_tasks(ctx)
    ctx.store()
