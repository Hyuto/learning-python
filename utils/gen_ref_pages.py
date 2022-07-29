from pathlib import Path

import mkdocs_gen_files

docs = "reference.md"
project_dir = "src"
for path in sorted(Path(project_dir).rglob("*.py")):
    with open(path) as reader:
        data = reader.read()
        if data == "":
            continue

    module_path = path.with_suffix("")
    parts = tuple(path.relative_to(project_dir).with_suffix("").parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
    elif parts[-1] == "__main__":
        continue

    with mkdocs_gen_files.open(docs, "a") as fd:
        ident = ".".join([project_dir, *parts])
        fd.write(
            f"\n::: {ident}"
            + "\n    options:\n      heading_level: 2\n      show_root_heading: false"
        )

    mkdocs_gen_files.set_edit_path(docs, path)
