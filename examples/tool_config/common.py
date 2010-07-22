import os

from yaku.pprint \
    import \
        pprint
from yaku.context \
    import \
        get_bld

def build():
    def _build(ctx):
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
    _build(ctx)
    ctx.store()
