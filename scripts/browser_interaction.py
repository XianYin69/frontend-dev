#!/usr/bin/env python3
"""browser_interaction.py — 浏览器取证：多档截图 + console 错误 + 失败请求。
用法: browser_interaction.py <url> [--out DIR] [--shots 375x800,768x1024,1280x800]
依赖 playwright(MIT): pip install playwright && python -m playwright install chromium
缺依赖降级: 输出 URL 提示人工查看, 退出码 2。有错误/失败请求退出码 1。"""
import os, sys, json, argparse


def main(url, out, sizes):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(f"FALLBACK: playwright 未安装, 请人工查看 {url}"); return 2
    os.makedirs(out, exist_ok=True)
    logs, fails = [], []
    with sync_playwright() as p:
        pg = (b := p.chromium.launch()).new_page()
        pg.on("console", lambda m: logs.append(f"{m.type}:{m.text}"))
        pg.on("requestfailed", lambda r: fails.append(r.url))
        pg.goto(url, wait_until="networkidle", timeout=15000)
        for w, h in sizes:
            pg.set_viewport_size({"width": w, "height": h})
            pg.screenshot(path=os.path.join(out, f"{w}x{h}.png"), full_page=True)
        b.close()
    rep = os.path.join(out, "report.json")
    json.dump({"url": url, "console": logs, "failed_requests": fails},
              open(rep, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"OK {rep} console={len(logs)} failed={len(fails)}")
    return 1 if (fails or any(l.startswith("error") for l in logs)) else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("--out", default="tmp/preview")
    ap.add_argument("--shots", default="375x800,768x1024,1280x800")
    a = ap.parse_args()
    sizes = [tuple(map(int, s.lower().split("x"))) for s in a.shots.split(",")]
    sys.exit(main(a.url, a.out, sizes))
