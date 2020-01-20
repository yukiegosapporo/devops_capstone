pipeline {
    agent any
    stages {
        stage('Lint app.py') {
            steps {
                sh 'echo "lint"'
                sh 'pylint app/app.py -d C0115,C0103,C0114,R0201,F0401'
            }
        }
    }
}