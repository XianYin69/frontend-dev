#!/usr/bin/env python3
"""preview_serve.py — 本地回环静态预览服务。用法: preview_serve.py <站根> [端口]
端口被占用自动顺延(最多+20)。仅绑定 127.0.0.1，Ctrl+C 停止。"""
import os, sys, functools, http.server, socketserver


def serve(root, port):
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
    for p in range(port, port + 20):
        try:
            with socketserver.TCPServer(("127.0.0.1", p), h) as httpd:  # 勿开 SO_REUSEADDR：Windows 下允许重复绑定
                print(f"PREVIEW http://127.0.0.1:{p}/ root={root}", flush=True)
                httpd.serve_forever()
                return
        except OSError:
            print(f"port {p} busy, next", flush=True)
    print("ERROR: 无可用端口"); sys.exit(1)


if __name__ == "__main__":
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    if not os.path.isdir(root):
        print("ERROR: 站根不存在", root); sys.exit(1)
    serve(root, port)
