pipeline {
    agent any
    stages {
        stage('Lint app.py') {
            steps {
                sh 'echo "lint"'
                sh 'pylint app/app.py'
            }
        }
        // stage('Docker build') {
        //     steps {
        //         sh 'echo "docker build"'
        //         sh 'docker build --tag=rlapp .'
        //     }
        // }
        // stage('Upload to AWS') {
        //     steps {
        //         sh 'echo "Hello World"'
        //         withAWS(credentials: 'aws-static', region:'us-east-1') {
        //             s3Upload(file:'index.html', bucket:'yuki-jenkins-devops', path:'index.html')
        //         }
        //     }
        // }
    }
}