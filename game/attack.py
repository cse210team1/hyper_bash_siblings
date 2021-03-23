class Attack():
    def __init__(self):
        self.force = None

    def land_hit(self, atackee):
        atackee.knockback = atackee.damage * self.force

    