from models.problem import ProblemModel

# pylint: disable=no-member


def load_current_model():
    ml_modal = ProblemModel.objects(is_current=True).first()
    return ml_modal
