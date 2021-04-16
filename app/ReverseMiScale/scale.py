class Scale():
    def __init__(self, **kwargs):
        self.UUID = kwargs.get("UUID", "")
        self.manufacturerData = kwargs.get("manufacturerData", bytes())

        self.address = kwargs.get("address", "")
        self.rawData = kwargs.get("rawData", bytes())
        self.unit = kwargs.get("unit", "")
        self.weight = kwargs.get("weight", "")
        self.sequence = kwargs.get("sequence", "")
        self.isStabilized = kwargs.get("isStabilized", False)
        self.loadRemoved = kwargs.get("loadRemoved", False)
        self.impedance = kwargs.get("impedance","")
        self.height = kwargs.get("height","")
        self.body_fat =  kwargs.get("body_fat","")
        self.water =  kwargs.get("water","")
        self.bone_mass =  kwargs.get("bone_mass","")
        self.muscle_mass =  kwargs.get("muscle_mass","")
        self.proteine =  kwargs.get("proteine","")
        self.body_type =  kwargs.get("body_type","")
        self.metab_age =  kwargs.get("metab_age","")
        self.lean_mass =  kwargs.get("lean_mass","")
        self.metab_basal = kwargs.get("metab_basal","")
        self.visceral_fat = kwargs.get("visceral_fat","")
        self.bmi = kwargs.get("bmi","")

    
    def __str__(self):
        """Override the default print behavior"""
        import json
        vars = dict(self.__dict__)
        # Convert bytes to a hex string for a better lisibility
        vars["manufacturerData"] = self.manufacturerData.hex()
        vars["rawData"] = self.rawData.hex()
        return json.dumps(vars, indent=4, sort_keys=True)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return \
            self.UUID == other.UUID and \
            self.manufacturerData == other.manufacturerData and \
            self.address == other.address and \
            self.rawData == other.rawData and \
            self.unit == other.unit and \
            self.weight == other.weight and \
            self.sequence == other.sequence and \
            self.isStabilized == other.isStabilized and \
            self.loadRemoved == other.loadRemoved and \
            self.impedance == other.impedance and \
            self.height == other.height and \
            self.body_fat == other.body_fat and \
            self.water == other.water and \
            self.bone_mass == other.bone_mass and \
            self.muscle_mass == other.muscle_mass and \
            self.proteine == other.proteine and \
            self.body_type == other.body_type and \
            self.metab_age == other.metab_age and \
            self.lean_mass == other.lean_mass and \
            self.metab_basal == other.metab_basal and \
            self.visceral_fat == other.visceral_fat and \
            self.bmi == other.bmi  



       
                
