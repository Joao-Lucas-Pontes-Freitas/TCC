def with_ensemble_experiment(X_train, y_train, time_limit, dataset_name, tmp_path):
    import autosklearn.classification
    import autosklearn.metrics
    scorer = autosklearn.metrics.f1

    automl = autosklearn.classification.AutoSklearnClassifier(
        time_left_for_this_task=time_limit,
        tmp_folder=tmp_path,
        # get_trials_callback= grava_json,
        seed=1,
        memory_limit=4096,  # 4GB
        metric=scorer
    )
    automl.fit(X_train, y_train, dataset_name=dataset_name)
    return automl