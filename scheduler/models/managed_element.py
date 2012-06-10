from scheduler import db

class ManagedElement(db.Model):
    """
        Basically anything which can have Permissions
    """
    id = db.Column(db.Integer, db.Sequence("managed_element_id"), primary_key = True)

    discriminator = db.Column("type", db.String(50))
    __mapper_args__ = {"polymorphic_on" : discriminator,
    				   "polymorphic_identity" : None}

    def __repr__(self):
        return "<ManagedElement %r>" % self.id
