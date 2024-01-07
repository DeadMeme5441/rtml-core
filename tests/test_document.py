from rtml_core.document import Document


class TestDocument:
    def test_init(self):
        doc = Document("files/perfect_file.txt")
        assert doc.path == "files/perfect_file.txt"
        assert doc.name == "perfect_file.txt"

    def test_tags(self):
        doc = Document("files/perfect_file.txt")
        print(doc.tags)

    def test_pairs(self):
        doc = Document("files/perfect_file.txt")
        print(doc.tags)

    def test_error_check(self):
        doc = Document("files/ramayana.txt")
        assert doc.total_errors != 0
