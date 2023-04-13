"""Load rules_go ruleset and expose the toolchain and dep rules.
"""

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

def gazelle_setup():
    """gazelle_setup sets up all gazelle dependencies and rules."""

    # go_rules_dependencies is a function that registers external dependencies
    # needed by the Go rules.
    # See: https://github.com/bazelbuild/rules_go/blob/master/go/dependencies.rst#go_rules_dependencies
    go_rules_dependencies()

    # go_rules_dependencies is a function that registers external dependencies
    # needed by the Go rules.
    # See: https://github.com/bazelbuild/rules_go/blob/master/go/dependencies.rst#go_rules_dependencies
    go_register_toolchains(version = "1.19.4")

    # The following call configured the gazelle dependencies, Go environment and Go SDK.
    gazelle_dependencies()
