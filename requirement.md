# 用户需求表（requirement）

- 日期：2026-09-21 · 会话：`SMS/sessions/2026-09-21`
- 工作空间：`C:\Users\User\.kilocode\skills\frontend-dev`

## 目标

长期复用的「写前端」技能（frontend-dev）：构建与维护静态站点及前端页面；首个落地对象为双语博客 `xianyin69.github.io`。

## 功能范围（用户选 B，全要）

1. 新建/修改页面结构与内容（HTML，含双语目录、Article/News 模板页范式）
2. 样式与响应式布局（CSS、移动端适配、主题一致）
3. 交互脚本（JS：导航、语言切换、组件行为）
4. 框架引入（Vue/React，并与既有原生页面协同）
5. 改后自检：悬空链接检查、本地预览，并衔接 `web-design-guidelines` 审查 + `webapp-testing` 验证

## 约束

- 每 .md / 脚本 ≤ 50 行；悬空链接 = 0；SKILL.md 含 YAML frontmatter；提示词一句话精简
- 安装位置：全局 `C:\Users\User\.kilocode\skills\frontend-dev`
- git：tmp 内仓库，功能分支策略；远端 `https://github.com/XianYin69/frontend-dev.git`（收尾阶段推送前再确认）

## 物理输入交互判断

- 网页交互：**需要**（页面预览与操作验证）→ 脚本构建阶段须包含 `browser_interaction.py`
- 视觉/听觉：不需要

## 期望产出

一个可安装的 skill 目录：`SKILL.md`（含 frontmatter）+ `agent/` 四格式提示词 + `branch/` 流程 + `scripts/` 脚本 + `references/` 知识库 + `resistance/` 约束，收尾后纳入 SMS 注册并参与调度。
