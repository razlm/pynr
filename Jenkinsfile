pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', description: 'Branch name', defaultValue: 'main')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/razlm/pynr', credentialsId: 'git-pat']]])
            }
        }

        stage('Build and Deploy') {
            steps {
                // Build and deploy your service here
                // You might use Docker, npm, etc., depending on your service
                // Example: sh 'npm install && npm run build'
                // Example: sh 'docker build -t counter-service . && docker run -p 80:80 counter-service'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests if applicable
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded. Service is ready for production.'
            // Additional steps if needed
        }

        failure {
            echo 'Pipeline failed. Take necessary actions.'
            // Additional steps if needed
        }
    }
}
