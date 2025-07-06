def without_ensemble_experiment(X_train, y_train, time_limit, dataset_name):
    import autosklearn.classification
    automl = autosklearn.classification.AutoSklearnClassifier(
        time_left_for_this_task=time_limit,
        tmp_folder="without_ensemble_tmp",
        # get_trials_callback= grava_json,
        ensemble_size=1
    )
    automl.fit(X_train, y_train, dataset_name=dataset_name)
    return automl