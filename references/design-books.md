# 视觉/UI 设计书籍要点（design-books）

原创要点摘要，供 [样式CSS](../branch/流程/编码实现/样式CSS/样式CSS.md) 引用；不含原书正文。

- **《写给大家看的设计书》Robin Williams** — CRUD 四原则：对比 Contrast、重复 Repetition、对齐 Alignment、亲密性 Proximity。站点改造先套这四条再谈细节。
- **《Refactoring UI》Adam Wathan & Steve Schoger** — 用字号阶梯(12/14/16/20/24/32)与灰度阶而非任意值；间距取 4/8 倍数栅格；强调色稀有化(≤10%)；阴影靠低透明度多层，勿硬黑。
- **《The Design of Everyday Things》Don Norman** — 视觉层级引导注意流；示能(affordance)让"可点"看起来可点；错误要可逆且信息充分。
- **《网格系统》Josef Müller-Brockmann** — 内容优先定列数；跨断点保持基线节奏，正文行高 1.5–1.7。
- **《Don't Make Me Think》Steve Krug** — 每屏自明；导航可预测、当前页高亮；砍掉一半文字再砍一半。
- **Material Design 3 / Ant / shadcn 规范（公开）** — 取语义令牌(color roles、elevation、state layer)，勿硬编码十六进制。

## 应用清单（改动时逐条自检）

1. 是否用了统一字号/间距阶，而非零散像素？
2. 主行动点是否唯一且高对比，次要项是否降级？
3. 相邻相关信息是否用留白成组（亲密性）？
4. 颜色是否走 CSS 变量/令牌，暗色是否有对应？
5. 触控目标 ≥44px、正文对比 ≥4.5:1（详见 [a11y-checklist](./a11y-checklist.md)）？

## 来源评级

均取自权威设计著作与官方设计规范（A/B 级，见 [references 索引](./references.md)）；未抓取受版权保护正文。
