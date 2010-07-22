import os

from yaku.pprint \
    import \
        pprint
from yaku.context \
    import \
        get_cfg, get_bld
from yaku.conftests \
    import \
        check_compiler

def configure(ctx):
    pass

def prepare_default(ctx):
    #for t in ["ctasks", "pyext"]:
    for t in ["ctasks"]:
        ctx.load_tool(t)

def post_configure(ctx):
    cc = ctx.builders["ctasks"]
    #for arch in ["i386", "x86_64", "ppc"]:
    #    ctx.env["CFLAGS"].extend(["-arch", arch])
    #    check_compiler(cc)

    #pyext = ctx.builders["pyext"]
    #pyext.compiler_type = "clang"
    #pyext.use_distutils = False
    return

if __name__ == "__main__":
    ctx = get_cfg()
    pprint("PINK", "Preparing")
    prepare_default(ctx)
    pprint("PINK", "Configuring")
    configure(ctx)
    pprint("PINK", "Setting up tools")
    ctx.setup_tools()
    pprint("PINK", "Post configuring")
    post_configure(ctx)
    ctx.store()

    def build(ctx):
        #ctx.builders["pyext"].extension("_bar", 
        #        [os.path.join("src", "hellomodule.c")])
        ctx.builders["ctasks"].program("main", 
                [os.path.join("src", "main.c")])
        from yaku.scheduler import SerialRunner
        from yaku.task_manager import TaskManager
        runner = SerialRunner(ctx, TaskManager(ctx.tasks))
        runner.start()
        runner.run()

    pprint("PINK", "Getting bld")
    ctx = get_bld()
    pprint("PINK", "Building")
    build(ctx)
    ctx.store()
