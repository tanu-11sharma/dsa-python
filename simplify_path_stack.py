"""
Simplify a Unix-Style File Path
----------------------------------
Given an absolute Unix-style path that may contain redundant
slashes, "." segments (current directory), and ".." segments
(parent directory), collapse it into its simplified canonical form.

Time:  O(n)
Space: O(n) for the stack of directory names
"""


def simplify_path(path: str) -> str:
    stack: list[str] = []
    for part in path.split("/"):
        if part == "" or part == ".":
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)


if __name__ == "__main__":
    print(simplify_path("/home/"))  # expected output: /home
    print(simplify_path("/a/./b/../../c/"))  # expected output: /c
    print(simplify_path("/../"))  # expected output: /
    print(simplify_path("/a//b////c/d//././/.."))  # expected output: /a/b/c
