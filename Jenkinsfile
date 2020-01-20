pipeline {
    agent any
    stages {
        stage('Lint app.py') {
            steps {
                sh 'echo "lint"'
                sh 'pylint app/app.py -d C0115,C0103,C0114,R0201,F0401,C0111,R0903'
            }
        }
        stage('Docker build') {
            steps {
                sh 'echo "docker build"'
                sh 'docker build -t 976324526436.dkr.ecr.us-east-1.amazonaws.com/rlapp:latest .'
            }
        }
        stage('Docker push') {
            steps {
                sh 'echo "docker push"'
                sh 'docker push 976324526436.dkr.ecr.us-east-1.amazonaws.com/rlapp:latest'
            }
        }
        stage('Docker rmi') {
            steps {
                sh 'echo "docker push"'
                sh 'docker rmi 976324526436.dkr.ecr.us-east-1.amazonaws.com/rlapp:latest'
            }
        }
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