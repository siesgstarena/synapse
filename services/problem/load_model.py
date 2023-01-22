from models.ml_modal import MLModal

# pylint: disable=no-member


def load_current_model():
    ml_modal = MLModal.objects(is_current=True).first()
    return ml_modal
