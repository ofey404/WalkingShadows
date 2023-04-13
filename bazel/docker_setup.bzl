"""Load rules_docker
"""
load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
load(
    "@io_bazel_rules_docker//python3:image.bzl",
    _py_image_repos = "repositories",
)
load("@io_bazel_rules_docker//toolchains/docker:toolchain.bzl",
    docker_toolchain_configure="toolchain_configure"
)
load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")


def docker_setup():
    docker_toolchain_configure(
        name = "docker_config",
        # OPTIONAL: List of additional flags to pass to the docker command.
        docker_flags = [
            "--log-level=info",
        ],
    )

    container_repositories()
    _py_image_repos()
    container_deps()