def without_ensemble_experiment(X_train, y_train, time_limit, dataset_name, tmp_path):
    import autosklearn.classification
    import autosklearn.metrics

    scorer = autosklearn.metrics.f1_weighted

    automl = autosklearn.classification.AutoSklearnClassifier(
        time_left_for_this_task=time_limit,
        tmp_folder=tmp_path,
        seed=1,
        metric=scorer,
        ensemble_size=1
    )
    automl.fit(X_train, y_train, dataset_name=dataset_name)
    return automl