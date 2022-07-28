from pathlib import Path

import mkdocs_gen_files

project_dir = "src"
nav = mkdocs_gen_files.Nav()
for path in sorted(Path(project_dir).rglob("*.py")):
    with open(path) as reader:
        data = reader.read()
        if data == "":
            continue

    module_path = path.with_suffix("")
    doc_path = path.relative_to(project_dir).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(path.relative_to(project_dir).with_suffix("").parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()  #

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join([project_dir, *parts])
        fd.write(f"::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:  #
    nav_file.writelines(nav.build_literate_nav())
