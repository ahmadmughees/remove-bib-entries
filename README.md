# Remove unused bibtex entries from bib file. 

I usually export my bib file from Zotero and it conatains 100s of entries, which I have been keeping in my libraries from last decade. And in every academic paper I have written I use subset of these entries. 

So, once I finish my draft of the research paper, I usually want to remove entries which I am not using in the article. I tried to look online and did not find anything simple and then with the help of chatgpt I wrote a simple python function to achieve that it uses regex expression to find the keys in tex file and then create a new bib file and only keeps entries which have been used in the main.tex file.  

You can also use this function for your use cases. 


```python
from remove_entries import remove_entries


tex_path = "main.tex"
bib_path = "bib.bib"
out_path = "output.bib"
citation_keyword = "cite"  # some journals require citep as well
remove_entries(tex_path, bib_path, out_path, citation_keyword)
```
