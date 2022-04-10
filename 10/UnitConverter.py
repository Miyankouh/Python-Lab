class UnitConverter:
    def __init__(self, unit_from, unit_to, value_from):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value_from = value_from

    def __convert_cm(self):
        result = 0
        if self.unit_to == 'Centimeter':
            result = self.value_from
        elif self.unit_to == 'Meter':
            result = self.value_from / 100
        elif self.unit_to == 'Kilometer':
            result = (self.value_from / 100) / 1000
        elif self.unit_to == 'Mile':
            result = self.value_from / 160934.3979894787
        elif self.unit_to == 'Yard':
            result = self.value_from * 0.010936132983

        return result

    def __convert_meter(self):
        result = 0
        if self.unit_to == 'Meter':
            result = self.value_from
        elif self.unit_to == 'Centimeter':
            result = self.value_from * 100
        elif self.unit_to == 'Kilometer':
            result = self.value_from / 1000
        elif self.unit_to == 'Mile':
            result = self.value_from / 1609.3439798948
        elif self.unit_to == 'Yard':
            result = self.value_from * 1.0936132983

        return result

    def convert_unit(self):
        if self.unit_from == 'Centimeter':
            return self.convert_cm()
        elif self.unit_from == 'Meter':
            return self.convert_meter()
