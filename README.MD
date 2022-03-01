# MD to Webflow

This script converts markdown code snippets to be usable in webflow.

## Usage

On a Mac

`python3 md_to_webflow.py <path-to-markdown-file>`

The script will create a new file at <path-to-markdown-file>-webflow.md

If you want to test how it works you can run against this readme - the below code snippet will be formatted into markdown that webflow can read.

```js
const add = (p1, p2) => p1 + p2;
```

## Troubleshooting

- Check your code snippets in your markdown file and verify there is some indentation. Webflow is very nitpicky about code inside a block being indented the "right" way.
- Don't have multiple code blocks on top of one another. There has to be something in between code blocks.
