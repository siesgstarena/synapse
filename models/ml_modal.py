import datetime
from . import db

# pylint: disable=no-member


class MLModal(db.Document):
    _id = db.ObjectIdField()
    raw_dataset_url = db.StringField(required=True)
    processed_dataset_url = db.StringField(required=True)
    model_url = db.StringField(required=True)
    similarity_url = db.StringField(required=True)
    model_number = db.IntField()
    is_current = db.BooleanField(default=False)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)
    # pre save hook

    def pre_save(self):
        last_model = MLModal.objects().order_by("-model_number").first()
        if last_model is None:
            self.model_number = 1
        else:
            self.model_number = last_model.model_number + 1
        # make all other models not current
        MLModal.objects().update(is_current=False)
        self.is_current = True
        # set creation date
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.pre_save()
        # pylint: disable=super-with-arguments
        return super(MLModal, self).save(*args, **kwargs)

    def to_json(self, *args, **kwargs):
        return {
            "raw_dataset_url": self.raw_dataset_url,
            "processed_dataset_url": self.processed_dataset_url,
            "model_url": self.model_url,
            "model_number": self.model_number,
        }

    def __repr__(self):
        return f"MLModal(raw_dataset_url={self.raw_dataset_url}, processed_dataset_url={self.processed_dataset_url}, model_url={self.model_url}, model_number={self.model_number})"

    def __str__(self):
        return self.__repr__()
