"""Small HTML helpers on top of theme.py. Chapter text stays in the part files."""

from html import escape

from theme import box, chapter, code, ladder

__all__ = [
    "box",
    "chapter",
    "code",
    "ladder",
    "P",
    "ul",
    "ol",
    "sec",
    "cost",
    "trace",
    "say",
    "signals",
    "traps",
    "note",
    "table",
]


def P(text):
    return f"<p>{text}</p>"


def ul(items):
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{item}</li>" for item in items) + "</ol>"


def sec(title):
    return f"<h3 class='sec'>{escape(title)}</h3>"


def cost(text):
    return f"<p class='cost'>{escape(text)}</p>"


def trace(text):
    return f"<div class='trace'>{escape(text.strip())}</div>"


def say(text):
    return box("say", "Say this before you code", f"<p>{text}</p>")


def signals(items):
    return box("signals", "Recognition", ul(items))


def traps(items):
    return box("traps", "Traps", ul(items))


def note(title, items):
    return box("else", title, ul(items) if isinstance(items, list) else f"<p>{items}</p>")


def table(headers, rows, chapter_col=None, small=False):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = []
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            cls = " class='ch'" if chapter_col is not None and i == chapter_col else ""
            cells.append(f"<td{cls}>{cell}</td>")
        body.append("<tr>" + "".join(cells) + "</tr>")
    klass = " class='small'" if small else ""
    return f"<table{klass}><thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table>"
