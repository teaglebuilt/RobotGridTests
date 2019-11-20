pipeline {
    agent: any
    stages {
        stage ('build') {
             echo 'Running build automation'
             sh 'docker build -t robottests:1 .'
        }
    }
}