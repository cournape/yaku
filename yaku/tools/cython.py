import os
import sys
import re
import subprocess

from yaku.task_manager \
    import \
        extension, get_extension_hook
from yaku.task \
    import \
        Task
from yaku.compiled_fun \
    import \
        compile_fun
from yaku.utils \
    import \
        ensure_dir

@extension(".pyx")
def cython_task(self, node):
    base = os.path.splitext(node)[0]
    target = os.path.join(self.env["BLDDIR"], base + ".c")
    ensure_dir(target)
    task = Task("cython", inputs=node, outputs=target)
    task.env_vars = []
    task.env = self.env
    task.func = compile_fun("cython", "cython ${SRC} -o ${TGT}",
                            False)[0]
    compile_task = get_extension_hook(".c")
    ctask = compile_task(self, target)
    return [task] + ctask

def find_cython(ctx):
    cython_version = re.compile("Cython version ([0-9\.]+)")
    try:
        p = subprocess.Popen(["cython", "-V"], stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        err = p.communicate()[1]
        m = cython_version.match(err)
        if m:
            vstring = m.group(1)
            ctx.env["CYTHON_VERSION"] = tuple([i for i in vstring.split(".")])
        else:
            ctx.env["CYTHON_VERSION"] = None
        ctx.env["CYTHON"] = "cython"
        return True
    except OSError:
        return False

class CythonTool(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def detect(self):
        sys.stderr.write("Checking for cython ... ")
        if not find_cython(self.ctx):
            sys.stderr.write("no\n")
            return False
        sys.stderr.write("yes\n")
        return True

    def ensure_version(self, minver=None):
        if not self.detect():
            return False
        if minver is None:
            return True
        sys.stderr.write("Checking for cython >= %s ... " % \
                         minver)
        version_info = self.ctx.env["CYTHON_VERSION"]
        minver_info = minver.split(".")
        for i in range(min(len(minver_info), len(version_info))):
            if minver_info[i] > version_info[i]:
                sys.stderr.write("no\n")
                return False
        sys.stderr.write("yes\n")
        return True

def get_builder(ctx):
    return CythonTool(ctx)

