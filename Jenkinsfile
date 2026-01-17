pipeline {
    agent any

    environment {
        REGISTRY = "naveenkrishna02"
        IMAGE_NAME = "test"
        DOCKER_CREDENTIALS = credentials('docker-hub')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Naveenkrishna2002/kubernetescode-main.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        docker build -t ${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER} .
                        docker tag ${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER} ${REGISTRY}/${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('Unit Tests') {
            steps {
                echo "Unit tests would run here (placeholder for now)"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh '''
                        echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                        docker push ${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}
                        docker push ${REGISTRY}/${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('Trigger Update Manifest Job') {
            steps {
                build job: 'update-manifest', parameters: [
                    string(name: 'docker_tag', value: "${BUILD_NUMBER}")
                ]
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
        failure {
            echo "Pipeline failed! Check logs above."
        }
        success {
            echo "✓ Pipeline succeeded! New image pushed: ${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}"
        }
    }
}
