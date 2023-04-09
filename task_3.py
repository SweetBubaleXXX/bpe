import mdutils

from urllib import request

URL = "https://www.python.org/"


def count_symbols(url: str) -> dict[str, int]:
    res = request.urlopen(url)
    html = res.read().decode("utf-8")
    unique_symbols = set(html)
    return {symbol: html.count(symbol) for symbol in unique_symbols}


if __name__ == "__main__":
    symbols = count_symbols(URL)
    symbols["\\n"] = symbols.pop("\n")
    symbols["\\r"] = symbols.pop("\r")
    table_cells = ["Symbol", "Count"]
    for symbol, count in symbols.items():
        table_cells.extend((f"`'{symbol}'`", str(count)))
    mdFile = mdutils.MdUtils("README.md")
    mdFile.new_table(columns=2, rows=len(symbols)+1, text=table_cells)
    mdFile.create_md_file()
