import yaml
from io import StringIO


def write_specs(md_file, specs):
    # Table header
    md_file.write(
        "| **Name** | **Description** | **Working Group** | **Status** | **Links** |\n"
    )
    md_file.write("| --- | --- | --- | --- | --- |\n")

    # Table rows
    for s in specs:
        links = "&nbsp;".join([f"[{name}]({url})" for name, url in s["links"].items()])
        md_file.write(
            f"| **{s['name']}** | {s['description']} | {s['working_group']} | {s['status']} | {links} |\n"
        )

    md_file.write("\n\n")


def write_section(md_file, section, level=1):
    md_file.write(f"{'#' * level} {section['name']}\n\n")

    if "specs" in section:
        write_specs(md_file, section["specs"])

    if "subsections" in section:
        for subsection in section["subsections"]:
            write_section(md_file, subsection, level=level + 1)

        md_file.write("\n\n")


def main():
    with open("data.yml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open("template.md", "r") as template_file:
        template = template_file.read()

        output = StringIO()
        for section in data:
            write_section(output, section)

        with open("output.md", "w") as md_file:
            md_file.write(template.replace("{{specs}}", output.getvalue()))


if __name__ == "__main__":
    main()
