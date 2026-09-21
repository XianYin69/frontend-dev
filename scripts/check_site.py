#!/usr/bin/env python3
"""check_site.py — 站点自检：断链/资源/重复id/title·lang·alt/双语对应。
用法: check_site.py <站根> [--pages 相对页 ...]（缺省全站；跳过.目录/node_modules；0=过 1=问题）"""
import os, re, sys, argparse
from collections import Counter

SKIP = ("http:", "https:", "mailto:", "tel:", "data:", "#", "javascript:", "${")


def target_ok(base, root, url):
    u = url.split("?")[0].split("#")[0]
    if not u: return True
    p = os.path.join(root, u.lstrip("/")) if u.startswith("/") else os.path.normpath(os.path.join(base, u))
    if os.path.isdir(p): p = os.path.join(p, "index.html")
    return os.path.exists(p)


def walk(root):
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x[0] != "." and x != "node_modules"]
        yield from (os.path.join(d, f) for f in fs if f.endswith(".html"))


def check_html(path, root):
    html = open(path, encoding="utf-8", errors="ignore").read()
    base, errs = os.path.dirname(path), []
    for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
        v = m.group(1)
        if not v.startswith(SKIP) and "${" not in v and not target_ok(base, root, v):
            errs.append(f"死链: {v}")
    ids = Counter(re.findall(r'id="([^"]+)"', html))
    errs += [f"重复id: {k}" for k, c in ids.items() if c > 1]
    if "<title" not in html: errs.append("缺<title>")
    if not re.search(r"<html[^>]+lang=", html): errs.append("html缺lang")
    if re.search(r"<img(?![^>]*alt=)[^>]*>", html): errs.append("有无alt图片")
    zh = os.path.relpath(path, root).replace("\\", "/")
    for a_, b_ in (("zh-CN/", "en-US/"), ("en-US/", "zh-CN/")):
        if zh.startswith(a_) and not os.path.exists(os.path.join(root, b_ + zh[len(a_):])):
            errs.append(f"双语缺对应: {b_ + zh[len(a_):]}")
    return errs


if __name__ == "__main__":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    ap = argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--pages", nargs="*")
    a = ap.parse_args(); root = os.path.abspath(a.root); bad = 0
    pages = [os.path.join(root, p) for p in a.pages] if a.pages else list(walk(root))
    for p in sorted(pages):
        for e in check_html(p, root): print(f"[{os.path.relpath(p, root)}] {e}"); bad += 1
    print("OK: 0 问题" if not bad else f"共 {bad} 处问题"); sys.exit(1 if bad else 0)
