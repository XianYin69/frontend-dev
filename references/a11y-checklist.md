# 可访问性清单（a11y-checklist）

依据 WCAG 2.1 AA 与 axe-core 规则（公开标准）整理，供 [审查](../branch/流程/审查/审查.md) 与样式/交互分支自检。

## 静态可查（对应 check_site.py）

1. `<html lang>` 存在且与页面语言一致。2. 每页唯一 `<title>` 且描述性。
3. 所有 `<img>` 有意义 alt（装饰图 alt=""）。4. 无重复 id。
5. 站内链接/资源无死链。6. 表单控件有关联 `<label>`。

## 浏览器/axe 可查（webapp-testing + @axe-core/playwright）

7. 文本对比 ≥4.5:1，大字 ≥3:1。8. 仅靠颜色传达信息时要加文本/图标冗余。
9. 键盘可达：Tab 顺序合理，焦点可见，无 tabindex 正值。
10. 交互控件有可访问名（aria-label 或内容）。11. 地标唯一：一个 `<main>`、导航 `<nav>`。
12. 标题层级不跳级；语言切换链接 `hreflang` 正确。

## 降级说明

无 Playwright/axe 时，人工过 1–6 + 抽查 7–9；不得静默跳过，需在收尾报告标注「未做自动 a11y 验证」。

## 来源评级

W3C WCAG、Deque axe、Playwright 官方文档（A 级，见 [references 索引](./references.md)）。
