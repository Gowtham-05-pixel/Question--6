pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                // checkout scm
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        echo 'Starting Frontend Check...'
                        // Simulates frontend_check.py sleeping 4s and creating the report file
                        sh 'python3 -c "import time; time.sleep(4); open(\'frontend_report.txt\', \'w\').write(\'Frontend Success\\n\')"'
                    }
                }
                stage('Backend Check') {
                    steps {
                        echo 'Starting Backend Check...'
                        // Simulates backend_check.py sleeping 4s and creating the report file
                        sh 'python3 -c "import time; time.sleep(4); open(\'backend_report.txt\', \'w\').write(\'Backend Success\\n\')"'
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                echo 'Archiving report files...'
                archiveArtifacts artifacts: '*_report.txt', allowEmptyArchive: false
            }
        }
    }
}
