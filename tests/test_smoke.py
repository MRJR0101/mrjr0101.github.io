from pathlib import Path


def test_repo_has_readme() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    assert (repo_root / "README.md").exists()


def test_index_html_has_basic_closing_tags() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    html = (repo_root / "index.html").read_text(encoding="utf-8")

    assert "</footer>" in html
    assert "</body>" in html
    assert "</html>" in html


def test_index_html_avoids_cloudflare_email_link() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    html = (repo_root / "index.html").read_text(encoding="utf-8")

    assert "/cdn-cgi/l/email-protection" not in html
