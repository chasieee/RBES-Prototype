from experta import Fact

class Candidate(Fact):
    """Fakta utama kandidat (identitas)"""
    pass

class Screening(Fact):
    """Fakta hasil screening awal"""
    pass

class HardSkill(Fact):
    """Fakta Hard Skill dengan mandatory factor checking"""
    pass

class SoftSkill(Fact):
    """Fakta Soft Skill"""
    pass

class LiveCoding(Fact):
    """Fakta Live Coding"""
    pass

class Tambahan(Fact):
    """Fakta Nilai Tambahan"""
    pass

class Result(Fact):
    """Kesimpulan akhir"""
    pass

# Flag facts untuk kontrol alur dual process
class BinaryFlag(Fact):
    """Flag untuk binary process dan gate checking"""
    pass