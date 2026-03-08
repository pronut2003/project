pipeline {
    agent any

    environment {
        DOCKER_USER = "pranat2004"
        BACKEND_IMAGE = "${DOCKER_USER}/fastapi-backend"
        FRONTEND_IMAGE = "${DOCKER_USER}/react-frontend"
        EC2_IP = "54.242.252.217"
    }

    stages {

        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t $BACKEND_IMAGE:latest .'
                }
            }
        }

        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh 'docker build -t $FRONTEND_IMAGE:latest .'
                }
            }
        }

        stage('Login DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Images') {
            steps {
                sh 'docker push $BACKEND_IMAGE:latest'
                sh 'docker push $FRONTEND_IMAGE:latest'
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ec2-key', keyFileVariable: 'KEYFILE')]) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no -i $KEYFILE ec2-user@54.242.252.217 << EOF
                    docker pull pranat2004/fastapi-backend:latest
                    docker pull pranat2004/react-frontend:latest

                    docker stop backend || true
                    docker stop frontend || true

                    docker rm backend || true
                    docker rm frontend || true

                    docker run -d -p 8000:8000 --name backend pranat2004/fastapi-backend:latest
                    docker run -d -p 80:80 --name frontend pranat2004/react-frontend:latest
                    EOF
                    '''
                }
            }
        }
    }
}