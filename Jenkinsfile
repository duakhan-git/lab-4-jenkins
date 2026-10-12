pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'date +%s > pipeline_start.txt'
                sh 'make build'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 run_tests.py'
            }
        }

        stage('Setup ML Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install pandas scikit-learn joblib
                '''
            }
        }

        stage('Train ML Model') {
            steps {
                sh '.venv/bin/python train_model.py'
            }
        }

        stage('Collect Build Data') {
            steps {
                sh '''
                    export PIPELINE_START_TIME=$(cat pipeline_start.txt)
                    .venv/bin/python collect_build_data.py
                '''
            }
        }

        stage('Predict Build Outcome') {
            steps {
                sh '.venv/bin/python predict_build.py'
            }
        }

        stage('Deploy') {
            steps {
                sh 'make deploy'
            }
        }
    }
}
