# from sha import db
#
#
# class Car(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     car_name = db.Column(db.Text, nullable=False)
#     image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
#     price = db.Column(db.REAL, nullable=False)
#
#     def __repr__(self):
#         return f"Car('{self.car_name}', '{self.price}')"
#
#
# class Specifications(db.Model):
#     specification_id = db.Column(db.Text, nullable=False)
#     car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
#     engine = db.Column(db.Text, nullable=False)
#     transmission = db.Column(db.Text, nullable=False)
#     acceleration = db.Column(db.Text, nullable=False)
#     top_speed = db.Column(db.Text, nullable=False)
#     footprint_measure = db.Column(db.REAL, nullable=False)
#
#     def __repr__(self):
#         return f"Specifications('{self.engine}', '{self.transmission}','{self.acceleration}','{self.top_speed}', " \
#                f"'{self.footprint_measure}')"
#