pipeline {
    agent {
        docker {
            image 'hadolint/hadolint:latest-debian'
        }
    }
    stages {
        // stage('pip install') {
        //     steps {
        //         sh 'echo "pip install"'
        //         sh 'pip3 install -r requirements.txt'
        //     }
        // }
        stage('Lint') {
            steps {
                sh 'echo "lint"'
                sh 'hadolint dockerfiles/*'
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