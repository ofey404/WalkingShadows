"""Load rule_python
"""
# Next we load the toolchain from rules_python.
load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")
# To compile the rules_python gazelle extension from source,
# we must fetch some third-party go dependencies that it uses.
load("@rules_python_gazelle_plugin//:deps.bzl", _py_gazelle_deps = "gazelle_deps")

def python_setup(toolchain_name):
    """python_setup sets up the python toolchain and pip dependencies"""
    py_repositories()

    _py_gazelle_deps()

    # We now register a hermetic Python interpreter rather than relying on a system-installed interpreter.
    # This toolchain will allow bazel to download a specific python version, and use that version
    # for compilation.
    python_register_toolchains(
        name = toolchain_name,
        python_version = "3.10",
    )
