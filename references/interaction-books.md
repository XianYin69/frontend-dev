# 网页交互设计书籍要点（interaction-books）

原创要点摘要，供 [交互JS](../branch/流程/编码实现/交互JS/交互JS.md) 与 [审查](../branch/流程/审查/审查.md) 引用。

- **《About Face 4》Alan Cooper** — 目标驱动设计；先"用户要完成什么"再定控件；进度指示、撤销、默认值减少负担；防止"死路"交互。
- **《Don't Make Me Think》Steve Krug** — 交互可预测性优先于新颖；点击反馈即时；链接去向明确。
- **《Refactoring UI》** — 状态可见：hover/focus/active/disabled 都要有反馈；用位移/缩放/透明度做微交互，勿用会重排布局的属性。
- **《Designing Interfaces》Jenifer Tidwell** — 复用已验证模式（tabs、accordion、modal、infinite scroll 慎用）；模式一致性优先。
- **WAI-ARIA Authoring Practices + Nielsen Norman 时效研究（公开）** — 加载>1s 给骨架/spinner；>10s 给进度；表单即时校验、错误就近说明；动效须响应 `prefers-reduced-motion`。

## 响应时效参考（Nielsen）

- 0.1s 感觉即时；1s 保持思路连续；>10s 注意力流失——据此决定是否需要反馈/进度态。

## 应用清单

1. 每个可交互元素是否有非颜色可辨的状态反馈？
2. 是否可纯键盘完成核心流程（见 [a11y-checklist](./a11y-checklist.md)）？
3. 动效是否尊重 `prefers-reduced-motion`？
4. 异步操作是否有加载/成功/失败/空四态？
5. 破坏性操作是否二次确认且可撤销？

## 来源评级

权威交互设计著作 + W3C/NN/g 公开指南（A/B 级）；原创转述，无正文复制。
