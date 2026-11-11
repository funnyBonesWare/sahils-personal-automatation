"""Print theme and small HTML helpers for the array handbook."""

from html import escape


def e(text):
    return escape(str(text), quote=True)


def code(src, caption=None):
    cap = f"<p class='caption'>{e(caption)}</p>" if caption else ""
    return cap + f"<pre><code>{escape(src.strip('\n'))}</code></pre>"


def box(kind, title, inner):
    return (
        f"<aside class='box {kind}'><h3>{e(title)}</h3>{inner}</aside>"
    )


LANE = {
    "stay": "Stay",
    "then": "Then",
    "second": "Second pass",
}


def problem(num, slug, title, diff, lane, why):
    return f"""<li>
      <div class="prow">
        <a href="https://leetcode.com/problems/{slug}/">{num}. {e(title)}</a>
        <span class="tag {diff}">{diff}</span>
        <span class="lane {lane}">{LANE[lane]}</span>
      </div>
      <p class="why">{e(why)}</p>
    </li>"""


def ladder(items, note=None):
    head = f"<p class='ladder-note'>{note}</p>" if note else ""
    rows = "\n".join(problem(*item) for item in items)
    return head + f"<ol class='ladder'>{rows}</ol>"


def chapter(num, title, builds, idea, body, memory, carries):
    return f"""
<section class="chapter" id="ch-{num}">
  <p class="kicker">Chapter {num:02d} · builds on {e(builds)}</p>
  <h2>{e(title)}</h2>
  <p class="idea">{idea}</p>
  {body}
  <aside class="box ready">
    <h3>Rewrite from memory</h3>
    <p>{e(memory)}</p>
  </aside>
  <p class="carry"><strong>Carry forward.</strong> {carries}</p>
</section>
"""


CSS = r"""
@page {
  size: A4;
  margin: 22mm 12mm 16mm 12mm;
  @top-center {
    content: "Sahil Siddiqui   ·   https://www.linkedin.com/in/sahil-siddiqui-8416b8195/";
    font-family: "Avenir Next", "Gill Sans", "Trebuchet MS", sans-serif;
    font-size: 9pt;
    font-weight: 600;
    color: #1c1915;
  }
  @bottom-left {
    content: "From zero  ·  arrays and matrices  ·  JavaScript";
    font-family: "Avenir Next", "Gill Sans", sans-serif;
    font-size: 8pt;
    color: #5e584e;
  }
  @bottom-right {
    content: counter(page);
    font-family: "Avenir Next", "Gill Sans", sans-serif;
    font-size: 8pt;
    color: #5e584e;
  }
}
* { box-sizing: border-box; }
html, body {
  margin: 0;
  padding: 0;
  background: white;
  color: #1c1915;
  font-family: Palatino, "Palatino Linotype", "Iowan Old Style", Georgia, serif;
  font-size: 10.5pt;
  line-height: 1.42;
}
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1, h2, h3, .kicker, .prow, .tag, .lane, .cover, .path, .meta {
  font-family: "Avenir Next", "Gill Sans", "Trebuchet MS", sans-serif;
}
a { color: #1d4e89; text-decoration: underline; text-underline-offset: 2px; }
p { margin: 0 0 8px; }
strong { font-weight: 700; }
ul, ol { margin: 4px 0 10px; padding-left: 18px; }
li { margin: 0 0 4px; }
.cover { min-height: 250mm; }
.cover h1 {
  font-size: 32pt;
  line-height: 1.02;
  font-weight: 700;
  letter-spacing: -0.03em;
  margin: 18mm 0 8px;
}
.eyebrow {
  margin: 0;
  color: #1b4332;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  font-size: 9pt;
  font-weight: 600;
}
.deck { font-size: 13pt; line-height: 1.35; max-width: 42em; margin: 0 0 14px; }
.byline {
  font-family: "Avenir Next", "Gill Sans", "Trebuchet MS", sans-serif;
  font-size: 11pt;
  font-weight: 650;
  line-height: 1.45;
  color: #1c1915;
  margin: 0 0 10px;
}
.byline a {
  font-weight: 600;
  font-size: 10.5pt;
  color: #1a365d;
}
.meta { color: #5e584e; font-size: 9.5pt; margin-bottom: 16px; }
.path {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px 18px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.path li {
  break-inside: avoid;
  border-top: 1px solid #e4ddd0;
  padding: 5px 0 6px;
  margin: 0;
}
.path .n {
  display: inline-block;
  width: 1.6em;
  color: #1b4332;
  font-weight: 700;
  font-size: 9pt;
}
.path .t { font-weight: 650; font-size: 9.5pt; }
.path .d { display: block; color: #5e584e; font-family: Palatino, Georgia, serif; font-size: 9pt; margin-top: 1px; }
.rule { height: 4px; width: 42px; background: #1b4332; margin: 14px 0; }
.chapter { break-before: page; }
.kicker {
  margin: 0 0 3px;
  color: #1b4332;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-size: 8pt;
  font-weight: 600;
}
h2 {
  font-size: 20pt;
  line-height: 1.12;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  font-weight: 700;
}
h3.sec {
  font-family: "Avenir Next", "Gill Sans", sans-serif;
  font-size: 12pt;
  margin: 12px 0 4px;
}
.idea { font-size: 11.5pt; line-height: 1.38; margin: 0 0 10px; }
.box {
  border-radius: 8px;
  padding: 8px 11px 4px;
  margin: 8px 0 10px;
  break-inside: avoid;
}
.box h3 {
  margin: 0 0 4px;
  font-size: 8pt;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 700;
}
.box p:last-child, .box ul:last-child, .box ol:last-child { margin-bottom: 6px; }
.signals { background: #f8f1e2; }
.signals h3 { color: #6b4a0e; }
.traps { background: #f8ebe6; }
.traps h3 { color: #7c2d12; }
.say { background: #e7f2ec; }
.say h3 { color: #1b4332; }
.ready { background: #f4f1ea; }
.ready h3 { color: #3f3a32; }
.else { background: #eef3f8; }
.else h3 { color: #1d4e89; }
pre {
  background: #f4f0e6;
  border-left: 3px solid #1b4332;
  padding: 8px 10px;
  margin: 4px 0 10px;
  white-space: pre-wrap;
  word-break: break-word;
  font-family: "SF Mono", ui-monospace, Menlo, Consolas, monospace;
  font-size: 8pt;
  line-height: 1.38;
}
.caption {
  font-family: "Avenir Next", "Gill Sans", sans-serif;
  font-size: 8pt;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #5e584e;
  margin: 8px 0 2px;
}
.cost {
  font-family: "Avenir Next", "Gill Sans", sans-serif;
  font-size: 8.5pt;
  color: #1b4332;
  margin: -4px 0 10px;
}
.trace {
  font-family: "SF Mono", ui-monospace, Menlo, monospace;
  font-size: 8pt;
  line-height: 1.4;
  background: #f7f6f3;
  padding: 8px 10px;
  margin: 0 0 10px;
  white-space: pre-wrap;
  break-inside: avoid;
}
.ladder { list-style: none; padding: 0; margin: 6px 0 10px; }
.ladder > li {
  break-inside: avoid;
  border-top: 1px solid #e6e0d4;
  padding: 6px 0 5px;
  margin: 0;
}
.prow { font-size: 10.5pt; font-weight: 600; }
.why {
  font-family: Palatino, Georgia, serif;
  font-weight: 400;
  color: #3f3a32;
  margin: 2px 0 0;
  font-size: 10pt;
}
.tag, .lane {
  display: inline-block;
  font-size: 7.5pt;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  border-radius: 99px;
  padding: 1px 6px;
  margin-left: 4px;
  font-weight: 700;
  vertical-align: 1px;
}
.tag.easy { background: #e5f3ea; color: #1b4332; }
.tag.medium { background: #f8f1e2; color: #6b4a0e; }
.tag.hard { background: #f8ebe6; color: #7c2d12; }
.lane.stay { background: #1b4332; color: white; }
.lane.then { background: #e4ddd0; color: #1c1915; }
.lane.second { background: white; color: #7c2d12; border: 1px solid #e2c8c0; }
.ladder-note { color: #5e584e; font-size: 10pt; }
.carry { margin-top: 8px; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 6px 0 12px;
  font-size: 9.5pt;
  break-inside: auto;
}
th, td {
  border-top: 1px solid #e0d9cc;
  text-align: left;
  vertical-align: top;
  padding: 4px 6px 4px 0;
}
th {
  font-family: "Avenir Next", "Gill Sans", sans-serif;
  font-size: 8pt;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #5e584e;
  font-weight: 700;
}
td.ch { white-space: nowrap; font-family: "Avenir Next", sans-serif; font-weight: 650; color: #1b4332; }
.night { break-before: page; }
.night h2 { font-size: 18pt; }
.small td, .small th { font-size: 8.4pt; padding: 3px 5px 3px 0; }
"""
