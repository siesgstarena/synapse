import datetime
from flask_admin.contrib.mongoengine import ModelView
from . import db

# pylint: disable=no-member,protected-access


class ProblemModel(db.Document):
    _id = db.ObjectIdField()
    raw_dataset_url = db.StringField(required=True)
    processed_dataset_url = db.StringField(required=True)
    model_url = db.StringField(required=True)
    similarity_url = db.StringField(required=True)
    model_number = db.IntField()
    is_current = db.BooleanField(default=False)
    date = db.DateTimeField(default=datetime.datetime.now)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)
    # pre save hook

    def pre_save(self):
        last_model = ProblemModel.objects().order_by("-model_number").first()
        # check if updating or creating
        if self._id is not None:
            self.model_number = self.model_number
        # if creating, set model number
        else:
            if last_model is None:
                self.model_number = 1
            else:
                self.model_number = last_model.model_number + 1
        # make all other models not current
        ProblemModel.objects().update(is_current=False)
        self.is_current = True
        # set creation date
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.pre_save()
        # pylint: disable=super-with-arguments
        return super(ProblemModel, self).save(*args, **kwargs)

    def to_json(self, *args, **kwargs):
        return {
            "raw_dataset_url": self.raw_dataset_url,
            "processed_dataset_url": self.processed_dataset_url,
            "model_url": self.model_url,
            "model_number": self.model_number,
        }

    def __repr__(self):
        return f"ProblemModel(raw_dataset_url={self.raw_dataset_url}, processed_dataset_url={self.processed_dataset_url}, model_url={self.model_url}, model_number={self.model_number})"

    def __str__(self):
        return self.__repr__()


class ProblemView(ModelView):
    column_filters = ["is_current"]
    column_list = ["model_number", "is_current", "creation_date", "modified_date"]
    column_sortable_list = [
        "model_number",
        "is_current",
        "creation_date",
        "modified_date",
    ]
    column_labels = dict(
        model_number="Model Number",
        is_current="Is Current",
        creation_date="Creation Date",
        modified_date="Modified Date",
    )
    column_default_sort = ("is_current", True)
    can_create = True
    can_delete = True
    can_edit = True
    can_view_details = True
    can_export = True
    column_display_pk = True
    edit_modal = True
    action_disallowed_list = ["delete"]
    # create form
    form_columns = [
        "raw_dataset_url",
        "processed_dataset_url",
        "model_url",
        "similarity_url",
        "is_current",
    ]
    # edit form
    form_edit_rules = [
        "raw_dataset_url",
        "processed_dataset_url",
        "model_url",
        "similarity_url",
        "is_current",
    ]
    # details form
    form_details_rules = [
        "raw_dataset_url",
        "processed_dataset_url",
        "model_url",
        "similarity_url",
        "is_current",
    ]
    # list form
    column_searchable_list = [
        "raw_dataset_url",
        "processed_dataset_url",
        "model_url",
        "similarity_url",
    ]

    # get id
    def get_pk_value(self, model):
        return str(model._id)

    # get record
    def get_one(self, _id):
        return ProblemModel.objects(_id=_id).first()

    # delete record
    def delete_model(self, model):
        record_id = str(model._id)
        print(record_id)
        ProblemModel.objects(_id=record_id).delete()

    # update record
    def update_model(self, form, model):
        model.raw_dataset_url = form.raw_dataset_url.data
        model.processed_dataset_url = form.processed_dataset_url.data
        model.model_url = form.model_url.data
        model.similarity_url = form.similarity_url.data
        model.save()

    # create record
    def create_model(self, form):
        model = ProblemModel(
            raw_dataset_url=form.raw_dataset_url.data,
            processed_dataset_url=form.processed_dataset_url.data,
            model_url=form.model_url.data,
            similarity_url=form.similarity_url.data,
        )
        model.save()
        return model
