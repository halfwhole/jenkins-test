pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'master' }
            steps {
                sh 'echo "Hello, world!"'
            }
        }
        stage('Test') {
            parallel {
                stage('Wait 5s') {
                    agent { label 'agent' }
                    steps {
                        sh 'python script.py 5'
                    }
                }
                stage('Wait 10s') {
                    agent { label 'master' }
                    steps {
                        sh 'python script.py 10'
                    }
                }
            }
        }
        stage('Deploy') {
            agent { label 'agent' }
            steps {
                sh 'echo "Deployment stage"'
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
