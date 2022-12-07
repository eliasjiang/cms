from app import db


class Tag(db.Model):
    __tablename__ = 't_tag'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='标签名')

    # tag = db.relationship('Post', secondary=t_post_tag, backref=db.backref('t_tag'), lazy='dynamic')

    def __init__(self, **kwargs):
        super(Tag, self).__init__(**kwargs)

    def __repr__(self):
        return '<Tag %r>' % self.name
