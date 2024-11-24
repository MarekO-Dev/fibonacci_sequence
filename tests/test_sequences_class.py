import src.fibonacci_sequence_copy as fs_file

class TestSequencesClass:

    def test_sequence_class_has_all_instances_attr(self):
        print("what", self)
        assert fs_file.Sequences._all_instances == []