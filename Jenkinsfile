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
<<<<<<< Updated upstream
            steps{
                
                sh 'sleep 60'
               
            }
=======
            sh 'sleep 120'
>>>>>>> Stashed changes
        }
        stage('Testing') {
            steps {
                sh 'source venv/bin/activate'
                sh 'coverage run -m pytest ./test/testing.py'
                sh 'coverage report -m'

            }
        }
    }
}
