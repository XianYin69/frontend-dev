# update 接口（frontend-dev 自更新）

对本技能的修改一律走 Skill_Generator 的「修改路径」（初始化→修改流程），禁止直接改本体：

1. 由 skill_manage_system 识别「修改 frontend-dev」意图。
2. 委托 Skill_Generator：在 `tmp/` 镜像本技能 → 修改 → 九项审查 → `compare` → `release` 覆盖回本目录。
3. 红线区（`resistance/`、本文件）变更需用户显式批准。
4. 每次 release 后由 SMS `init_registry.py --write` 重新注册接口描述。
