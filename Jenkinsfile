pipeline{
    agent any
    stages{
        stage('Development Environment'){
            steps{
                sh 'chmod 775 ./script/*'
                sh './script/before_installation.sh'
                sh './script/make_service.sh'
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 20'
               
            }
        }
        stage('Testing') {
            steps {
                sh './script/testing.sh'

            }
        }
    }
}
