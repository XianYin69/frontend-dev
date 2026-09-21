# 经验查询记录（references/experience.md）

- 日期：2026-09-21 · 查询工具：websearch

## 搜索词条

- `AI coding agent workflow frontend development HTML CSS JavaScript static site 2026`
- `static website broken link checker local preview Playwright accessibility review 2026`

## 来源与要点

- https://medium.com/@jakintemi/...632b65da927d — 2026 前端流变为「Idea→Prompt AI→Review Output→Improve Architecture→Ship」；编码步缩小，审查/架构更值钱。
- https://kayraberktuncer.medium.com/...1f64b1fb9d88 — 上下文策略：单仓+AGENTS.md 让 agent 直达引用；「monorepo 是上下文策略」。
- https://chenguangliang.com/...ai-agent-frontend-workflow-part4 — 多 agent 协作（架构/UI/可访问性分工）；本地跑开源模型可行。
- https://www.developersdigest.tech/blog/ai-developer-workflow-2026 — 并行子 agent：独立任务并发；站点审计四路并发（设计一致/内容缺口/断链/SEO）。
- https://frontman.sh/blog/best-frontend-coding-agent — 前端 agent 须覆盖：组件、设计令牌、浏览器行为、响应式、可访问性、review。
- https://adobe.chromatic.com/frontend-workflow-for-ai — Build/Test 双循环；agent 生成代码+stories，人定意图并 review。
- https://dev.to/kevinccbsg/frontend-with-ai-workflow-first-agent-second-3hmo — TWD：在 dev server 内对同一 DOM 跑测试，结果回传文本供 agent 判定。
- https://playwright.dev/docs/accessibility-testing — axe-core+Playwright 扫可访问性；支持 include/特定规则、WCAG tag。
- https://github.com/hydroo-dev/playwright-website-health-checker — 爬取+断链+HTTP/控制台错误+全页截图+汇总。
- https://github.com/OKlueck/SpecA11y — 交互式 a11y（键盘陷阱/焦点/回流）+语义启发（alt/链接文本质量）。

## 词条频次（学习统计）

agent · workflow · context · review · accessibility · parallel · DOM · preview · broken-link · WCAG · responsive · design-token · AGENTS.md

## 联系与关系

- 均指向同一回路：理解现状→编辑→本地预览→自检→审查→验证→收尾。
- 可访问性与断链/HTTP 错误常由 Playwright 统一驱动；与已注册 webapp-testing 同源。
- 项目上下文（AGENTS.md/结构清单）是 agent 不丢上下文的前提。

## 初步大纲素材

frontend-dev 流程雏形：读项目结构与上下文 → 编辑(HTML/CSS/JS·Vue/React) → 起本地静态服务预览 → 自检(断链/控制台/截图) → 衔接 web-design-guidelines 审查 + webapp-testing(含 axe) → 收尾(create-pull-request)。
