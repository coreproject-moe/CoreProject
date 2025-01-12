import re


def parse_version(version: str):
    """Parse a version string into a tuple with pre-release handling."""
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-([\w\.]+))?(?:\+([\w\.]+))?$", version)
    if not match:
        raise ValueError(f"Invalid version format: {version}")
    major, minor, patch, prerelease, build = match.groups()
    return (
        int(major),
        int(minor),
        int(patch),
        tuple(prerelease.split(".")) if prerelease else (),
        tuple(build.split(".")) if build else (),
    )


def compare_versions(version1: str, version2: str) -> int:
    """
    Example Usage
    -------------
    result = compare_versions("7.3.5", "7.4.2-alpha")
    if result == -1:
        print("Version 7.3.5 is less than 7.4.2-alpha.")
    elif result == 1:
        print("Version 7.3.5 is greater than 7.4.2-alpha.")
    else:
        print("Version 7.3.5 is equal to 7.4.2-alpha.")
    """
    v1 = parse_version(version1)
    v2 = parse_version(version2)
    return (v1 > v2) - (v1 < v2)
