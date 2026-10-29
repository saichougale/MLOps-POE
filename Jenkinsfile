pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv .venv
                .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                bat '.venv\\Scripts\\python.exe hello.py'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v --junitxml=pytest-results.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'pytest-results.xml'
                }
            }
        }

        stage('Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitor.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html',
                             allowEmptyArchive: true
        }
    }
}
