pipeline {
    environment {
        registry = "docker_hub_account/repository_name"
        registryCredential = 'dockerhub'
    }

    agent any
    stages {
        stage('Lint app.py') {
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

        // stage('Building image') {
        //     steps {
        //         echo 'Building Docker image...'
        //         withCredentials([
        //             usernamePassword(credentialsId: 'hub',
        //                             passwordVariable: 'hubPassword',
        //                             usernameVariable: 'hubUser')]) {
        //             sh "docker login -u ${env.hubUser} -p ${env.hubPassword}"
        //             sh "docker build -t ${registry} ."
        //             sh "docker tag ${registry} ${registry}"
        //             sh "docker push ${registry}"
        //         }
        // }
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