from models.problem import ProblemModel


def save_db(file_path):
    problem_model = ProblemModel(
        raw_dataset_url=file_path[0],
        processed_dataset_url=file_path[1],
        model_url=file_path[2],
        similarity_url=file_path[3],
        date=file_path[4],
    )
    problem_model.save()
    return problem_model
