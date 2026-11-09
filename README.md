# AI visibility toolkit

Small, practical files for checking and improving how a website shows up in AI answers (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews). No dependencies, no account needed.

| File | What it's for |
|---|---|
| [`citation_map.py`](citation_map.py) | Turns a CSV of AI-cited URLs into a ranked list of domains: how often each is cited, on how many questions, by which engines |
| [`templates/robots-ai-crawlers.txt`](templates/robots-ai-crawlers.txt) | robots.txt rules for the main AI crawlers, with what each one is for |
| [`templates/llms.txt`](templates/llms.txt) | A starting template for an llms.txt file |
| [`schema/organization.json`](schema/organization.json) | Organization JSON-LD with `sameAs` profiles |
| [`schema/product-woocommerce.json`](schema/product-woocommerce.json) | A complete Product JSON-LD block for an e-commerce product page |
| [`schema/faqpage.json`](schema/faqpage.json) | FAQPage JSON-LD for questions that are visible on the page |

## Citation map

Collect one row per cited URL (question, engine, URL), then run:

```bash
python citation_map.py examples/citations.csv
```

Output:

```
domain                              cites questions  engines
g2.com                                  1         1  chatgpt
reddit.com                              1         1  perplexity
zapier.com                              1         1  gemini
```

Read "questions" before "cites": a domain cited once on each of eight questions matters more than one cited ten times on a single question. Domains cited by every engine are the safest targets.

AI answers vary between runs and locations, so treat the map as a sample and re-run it with the same questions over time.

## What these files will and won't do

- **robots.txt** controls which crawlers may fetch your pages. Blocking a search crawler (like OAI-SearchBot or PerplexityBot) makes it unlikely your pages get cited by that engine. It doesn't control indexing.
- **llms.txt** is a proposal ([llmstxt.org](https://llmstxt.org)), not a standard. The major AI search engines haven't confirmed they use it. It's cheap housekeeping, not a growth lever.
- **JSON-LD** helps engines understand a page. It doesn't make a page worth recommending. Only mark up content that is visible on the page, and only add ratings or reviews that are real.

## Related guides

- [How to add an llms.txt file to WordPress](https://dev.to/citeproof/how-to-add-an-llmstxt-file-to-wordpress-and-what-it-will-and-wont-do-3gmj)
- [robots.txt vs sitemap.xml vs llms.txt](https://citeproof.hashnode.dev/robots-txt-vs-sitemap-xml-vs-llms-txt-what-each-file-does-for-ai-search)
- [Product JSON-LD for WooCommerce](https://dev.to/citeproof/product-json-ld-for-woocommerce-the-fields-ai-shopping-answers-can-actually-use-33o2)
- [Which structured data actually matters for AI search answers](https://citeproof.wordpress.com/2026/11/09/structured-data-for-ai-search/)

## About

Maintained by [CiteProof](https://citeproof.co/?utm_source=github&utm_medium=parasite&utm_campaign=ai-visibility-toolkit), which tracks whether AI engines recommend a business and what to fix. Free tools: [AI citation checker](https://citeproof.co/tools/ai-citation-checker?utm_source=github&utm_medium=parasite&utm_campaign=ai-visibility-toolkit), [llms.txt generator](https://citeproof.co/tools/llms-txt-generator?utm_source=github&utm_medium=parasite&utm_campaign=ai-visibility-toolkit).

Everything here works without CiteProof. MIT licensed.
