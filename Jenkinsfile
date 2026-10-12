pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }

        stage('Test') {
            steps {
                sh 'make test'
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
