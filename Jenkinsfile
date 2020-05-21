pipeline {
    agent any
    stages {
        stage('Build') {
            agent any
            steps {
                sh 'echo "Hello, world!"'
            }
        }
        stage('Test') {
            parallel {
                stage('Wait 5s') {
                    agent { label 'slave1' }
                    steps {
                        sh 'python --version'
                        sh 'python script.py 5'
                    }
                }
                stage('Wait 10s') {
                    agent { label 'slave2' }
                    steps {
                        sh 'python --version'
                        sh 'python script.py 10'
                    }
                }
            }
        }
        stage('Deploy') {
            agent { label 'slave1' }
            steps {
                sh 'echo "Deployment stage!"'
                sh 'ansible --version'
            }
        }
    }
    post {
        always {
            echo 'Always clause'
        }
        success {
            echo 'Success clause'
        }
    }
}
