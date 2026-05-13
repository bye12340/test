from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = r"}</\\/script></body></html>`;"
new = r"}</scr` + `ipt></body></html>`;"
if old not in text:
    raise SystemExit('OLD string not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
print('patched')
