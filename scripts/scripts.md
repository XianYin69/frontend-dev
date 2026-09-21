# scripts（frontend-dev 脚本索引）

三个脚本均为 Python3 标准库实现；`browser_interaction.py` 可选依赖 playwright（MIT）。

| 脚本 | 功能描述 | 输入 → 输出 | 调用节点 |
|---|---|---|---|
| [preview_serve.py](preview_serve.py) | 本地回环静态预览服务，端口占用自动顺延（≤+20） | 站根 [端口] → `PREVIEW http://127.0.0.1:P/` | [本地预览](../branch/流程/本地预览/本地预览.md) |
| [check_site.py](check_site.py) | 断链/资源缺失/重复id/title·lang·alt/双语对应 一次性检查 | 站根 [--pages…] → 问题清单，exit 0/1 | [自检](../branch/流程/自检/自检.md) |
| [browser_interaction.py](browser_interaction.py) | 多档视口全页截图 + console 错误 + 失败请求取证 | url [--out --shots] → 截图 + report.json，exit 0/1/2(降级) | [本地预览](../branch/流程/本地预览/本地预览.md)、[审查](../branch/流程/审查/审查.md) |

## 约定

- 退出码：0 通过 / 1 发现问题 / 2 依赖缺失降级（仅 browser_interaction）。
- 取证产物写调用方 `--out`（默认 `tmp/preview/`），不写入站点目录。
- 脚本不修改站点文件；一切修改发生在编码实现节点由 agent 执行。

## 审核记录（2026-09-21 · 运行时验证）

- `check_site.py` 全站扫描 `xianyin69.github.io`：检出 15 处真实问题（`assets/intro-ClAmIAr9.svg` 缺失、`index/MainPage` 缺 `<title>` 等），exit 1；已修 SKIP 误报模板 `${}`、隐藏目录。50 行。
- `preview_serve.py`：起服 8010 → `urlopen` 返回 200；再起同端口自动顺延至 8011 并 200。移除 `SO_REUSEADDR`（Windows 下会掩盖端口占用）。
- `browser_interaction.py`：本机无 playwright → 打印降级并 `exit 2`，无静默失败。

