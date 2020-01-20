pipeline {
    agent any
    stages {
        stage('Lint dockerfile') {
            steps {
                sh 'echo "lint"'
                sh 'hadolint Dockerfile'
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