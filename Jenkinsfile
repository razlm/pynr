pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', description: 'Branch name', defaultValue: 'master')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the source code from the specified branch
                    checkout([$class: 'GitSCM', branches: [[name: "*/${params.BRANCH}"]], userRemoteConfigs: [[url: 'your-repo-url']]])
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    // Build and deploy your service here
                    // You might use Docker, npm, etc., depending on your service
                    // Example: sh 'npm install && npm run build'
                    // Example: sh 'docker build -t counter-service . && docker run -p 80:80 counter-service'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests if applicable
                }
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

