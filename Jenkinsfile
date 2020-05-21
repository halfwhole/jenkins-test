pipeline {
    agent {
        node { label 'slave1' }
    }
    stages {
        stage('build') {
            steps {
                sh 'echo "Hello, world!"'
                sh 'python --version'
                sh 'python script.py'
            }
        }
    }
    post {
        always {
            echo 'Always clause'
        }
    }
}
