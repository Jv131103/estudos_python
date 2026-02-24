import pytest
from src.main import compactar, compactar2


@pytest.mark.parametrize(
    "texto,compactado",
    [
        ("aaabbcdddd", "a3b2c1d4"),
        ("aaaaaaaaaaaaaaaaaabbbbbbbccccddddeeeeeeeeeeeeeeeee", "a18b7c4d4e17"),
        ("abcd", "abcd"),
        ("aabb", "aabb")
    ]
)
class TestCompact:
    def test_compact_version1(self, texto, compactado):
        assert compactar(texto) == compactado

    def test_compact_version2(self, texto, compactado):
        assert compactar2(texto) == compactado
