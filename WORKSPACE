workspace(name = "walking_shadows")

load("//:bazel/all_http_archive.bzl", "all_http_archive")

all_http_archive()

load("//:bazel/gazelle_setup.bzl", "gazelle_setup")

gazelle_setup()

load("//:bazel/python_setup.bzl", "python_setup")

python_setup(
    toolchain_name = "python310"
)

# Load the interpreter and pip_parse rules.
load("@python310//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

# This macro wraps the `pip_repository` rule that invokes `pip`, with `incremental` set.
# Accepts a locked/compiled requirements file and installs the dependencies listed within.
# Those dependencies become available in a generated `requirements.bzl` file.
# You can instead check this `requirements.bzl` file into your repo.
pip_parse(
    name = "pip",
    # Generate user friendly alias labels for each dependency that we have.
    incompatible_generate_aliases = True,
    # (Optional) You can provide a python_interpreter (path) or a python_interpreter_target (a Bazel target, that
    # acts as an executable). The latter can be anything that could be used as Python interpreter. E.g.:
    # 1. Python interpreter that you compile in the build file.
    # 2. Pre-compiled python interpreter included with http_archive.
    # 3. Wrapper script, like in the autodetecting python toolchain.
    #
    # Here, we use the interpreter constant that resolves to the host interpreter from the default Python toolchain.
    python_interpreter_target = interpreter,
    # Set the location of the lock file.
    requirements_lock = "//:requirements_lock.txt",
    requirements_windows = "//:requirements_windows.txt",
)

# Load the install_deps macro.
load("@pip//:requirements.bzl", "install_deps")

# Initialize repositories for all packages in requirements_lock.txt.
install_deps()
