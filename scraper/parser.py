from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from models.schemas import Categoria


def parse_category_link(tag: Tag) -> Categoria | None:
    if not isinstance(tag, Tag):
        return None

    href = tag.get("href")
    if not href:
        return None

    nombre = tag.get_text(strip=True)
    if not nombre:
        return None

    slug = href.split(",")[-1]

    return Categoria(
        id_html=tag.get("id"),
        nombre=nombre,
        slug=slug,
        url=f"https://www.rockauto.com{href}",
    )


def extract_categories(html: str) -> list[Categoria]:
    soup = BeautifulSoup(html, "lxml")
    categorias: list[Categoria] = []
    for link in soup.select("a.navlabellink.nvoffset.nnormal"):
        categoria = parse_category_link(link)
        if categoria:
            categorias.append(categoria)
    return categorias
