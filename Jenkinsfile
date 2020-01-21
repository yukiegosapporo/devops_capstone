pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'echo "lint"'
                sh 'pylint app/app.py -d C0115,C0103,C0114,R0201,F0401,C0111,R0903'
            }
        }
        stage('Building image') {
            steps {
                script {
                        dockerImage = docker.build("yukiego/rlapp:latest")
                        docker.withRegistry('', 'hub') {
                            dockerImage.push()
                        }
                }
            }
        }
        stage('Deploying to EKS') {
            steps {
                dir('k8s') {
                    withAWS(credentials: 'aws', region: 'us-east-1') {
                        sh "aws eks --region us-east-1 update-kubeconfig --name EKS-iTh8Azxyb9Kf"
                        sh 'ls'
                        sh 'kubectl apply -f k8s/deployment.yaml'
                        sh 'kubectl apply -f k8s/service.yaml'
                        }
                    }
            }
        }
    }
}