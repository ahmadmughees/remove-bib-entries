import re


def remove_entries(
        tex_path: str,
        bib_path: str,
        out_path: str,
        citation_keyword: str
):
    with open(tex_path, 'r') as file:
        text = file.read()

    # Regex pattern to match \cite{key1, key2, ...}
    pattern = citation_keyword + r'{([^}]+)}'
    matches = re.findall(pattern, text)

    keys = set()
    for match in matches:
        for key in match.split(","):
            keys.add(key.strip())

    print(f"total keys found: {len(keys)}")

    # Process the BibTeX file
    with open(bib_path, 'r', encoding="cp437") as bib_file:
        bib_content = bib_file.readlines()

    # Keep track of whether we're within an entry that's being used
    keep_entry = False
    counter = 0
    with open(out_path, 'w', encoding="cp437") as out_file:
        for line in bib_content:
            if line.startswith('@'):
                # New entry; decide whether to keep it based on the citation key
                entry_key = line.split('{')[1].split(',')[0]
                keep_entry = entry_key in keys
                counter += not keep_entry
            if keep_entry:
                out_file.write(line)
    print(f"Removed {counter} unused entries from bib file!!")


def main():
    tex_path = "main.tex"
    bib_path = "bib.bib"
    out_path = "output.bib"
    citation_keyword = "cite"  # some journals require citep as well
    remove_entries(tex_path, bib_path, out_path, citation_keyword)


if __name__ == "__main__":
    main()
