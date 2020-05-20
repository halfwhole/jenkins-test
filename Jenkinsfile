pipeline {
    agent any
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
