from models.ml_modal import MLModal


def save_db(file_path):
    ml_modal = MLModal(
        raw_dataset_url=file_path[0],
        processed_dataset_url=file_path[1],
        model_url=file_path[2],
        similarity_url=file_path[3],
    )
    ml_modal.save()
    return ml_modal
