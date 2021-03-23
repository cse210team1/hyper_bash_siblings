class Attack():
    def __init__(self, number):
        self.force = number

    def land_hit(self, atackee):
        atackee.knockback = atackee.damage * self.force

    